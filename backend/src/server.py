import grpc
import psycopg2
import logging
import sys
import os
import json

from concurrent import futures

from xml.etree.ElementTree import Element, SubElement, tostring
import xml.dom.minidom

import gpxtracker_pb2
import gpxtracker_pb2_grpc

PORT = os.getenv("SERVER_PORT", 9090)

log = logging.getLogger("grpc-server")

logging.basicConfig(
    format='%(asctime)s %(message)s',
    level=logging.DEBUG, 
    stream=sys.stdout,
    datefmt='%Y-%m-%d %H:%M:%S',
)

conn = psycopg2.connect(
    dbname=os.getenv("DB_NAME", "gpx"),
    user=os.getenv("DB_USER", "root"),
    password=os.getenv("DB_PASSWORD", "root"),
    host=os.getenv("DB_HOST", "localhost"),
    port=os.getenv("DB_PORT", "5432")
)

def get_location_info(lat, lng):
    cur = conn.cursor()
    cur.execute(f"""
        SELECT 
            street, 
            ROUND(distance), 
            cutoff_time,
            ROUND(planned_hours),
            planned_time
        FROM gpx_route
        ORDER BY location <-> ST_SetSRID(ST_MakePoint({lng}, {lat}), 4326)
        LIMIT 1;
    """)
    row = cur.fetchone()
    cur.close()
    return row

def get_placemarks(lat, lng, distance):
    cur = conn.cursor()
    cur.execute(f"""
        SELECT
            ST_Y(location) AS latitude,
            ST_X(location) AS longitude,
            name,
            ROUND(distance)
        FROM
            placemarks
        WHERE
            distance >= {distance}
        ORDER BY
            location <-> ST_SetSRID(ST_MakePoint({lng}, {lat}), 4326)
        LIMIT 20;
    """)

    placemarks = []
    for row in cur.fetchall():
        placemarks.append({
            "lat": str(row[0]),
            "lng": str(row[1]),
            "name": str(row[2]),
            "distance": str(row[3]),
        })

    cur.close()

    return json.dumps(placemarks)

def get_gpx_route(lat, lng):
    cur = conn.cursor()
    cur.execute(f"""
        WITH closest_location AS (
            SELECT
                id,
                location
            FROM gpx_route
            ORDER BY location <-> ST_SetSRID(ST_MakePoint({lng}, {lat}), 4326)
            LIMIT 1
        )
        SELECT
            ST_Y(g.location) AS lat,
            ST_X(g.location) AS lng
        FROM gpx_route g, closest_location c
        WHERE g.id >= c.id
        ORDER BY g.id
        LIMIT 500;
    """)

    gpx = Element("GPX")
    trk = SubElement(gpx, "trk")
    trkseg = SubElement(trk, "trkseg")

    for row in cur.fetchall():
        SubElement(trkseg, "trkpt", attrib={"lat": str(row[0]), "lon": str(row[1])})

    cur.close()

    return xml.dom.minidom.parseString(
        tostring(gpx, encoding="unicode")
    ).toprettyxml()

class GPXTracker(gpxtracker_pb2_grpc.GPXTrackerServicer):
    def GetLocationInfo(self, request, context):
        log.info(f"GetLocationInfo: {request.lat} {request.lng}")

        info = get_location_info(
            request.lat,
            request.lng,
        )

        address, distance, cutoff_time, planned_hours, planned_time = info

        placemarks = get_placemarks(
            request.lat,
            request.lng,
            distance,          
        )

        return gpxtracker_pb2.LocationResponse(
            address=address,
            distance=distance,
            planned_time=planned_time,
            planned_hours=planned_hours,
            cutoff_time=cutoff_time,
            placemarks=placemarks,
        )
    
    def GetGPXFile(self, request, context):
        log.info(f"GetGPXFile for {request.userid}: {request.lat} {request.lng}")

        gpx_route = get_gpx_route(request.lat, request.lng)

        return gpxtracker_pb2.GPXFileResponse(
            xml=gpx_route,
        )   

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    
    gpxtracker_pb2_grpc.add_GPXTrackerServicer_to_server(GPXTracker(), server)
    server.add_insecure_port("[::]:" + str(PORT))
    server.start()

    log.info("Listening on " + str(PORT))
    server.wait_for_termination()

if __name__ == "__main__":
    serve()