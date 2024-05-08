import grpc
import psycopg2
import logging
import sys
import os

from concurrent import futures

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
            cutoff_time
        FROM gpx_route
        ORDER BY location <-> ST_SetSRID(ST_MakePoint({lng}, {lat}), 4326)
        LIMIT 1;
    """)
    row = cur.fetchone()
    cur.close()
    return row

def store_distance(userid, distance):
    cur = conn.cursor()
    cur.execute(f"""
        INSERT INTO distances (userid, distance) 
        VALUES ('{userid}', {distance})
    """)
    conn.commit()
    cur.close()

class GPXTracker(gpxtracker_pb2_grpc.GPXTrackerServicer):
    def GetLocationInfo(self, request, context):
        log.info(f"GetLocationInfo for {request.userid}: {request.lat} {request.lng}")
        
        info = get_location_info(
            request.lat,
            request.lng,
        )

        address, distance, cutoff_time = info

        store_distance(
            request.userid,
            distance
        )

        return gpxtracker_pb2.LocationResponse(
            address=address,
            distance=distance,
            cutoff_time=cutoff_time,
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