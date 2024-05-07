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

def get_location_info(lat, lng, field):
    cur = conn.cursor()
    cur.execute(f"""
        SELECT {field}
        FROM gpx_route
        ORDER BY location <-> ST_SetSRID(ST_MakePoint({lng}, {lat}), 4326)
        LIMIT 1;
    """)
    row = cur.fetchone()
    cur.close()
    return row[0]

class GPXTracker(gpxtracker_pb2_grpc.GPXTrackerServicer):
    def GetAddress(self, request, context):
        log.info(f"GetAddress")
        return gpxtracker_pb2.AddressResponse(address=f"Current address")

    def GetDistance(self, request, context):
        log.info(f"GetCoveredDistance")
        distance = get_location_info(
            request.lat,
            request.lng,
            'distance',
        )
        return gpxtracker_pb2.DistanceResponse(distance=distance)

    def GetTimeEstimate(self, request, context):
        log.info(f"GetTimeEstimate")
        time_estimate = get_location_info(
            request.lat,
            request.lng,
            'estimated_time',
        )
        return gpxtracker_pb2.TimeEstimateResponse(time_estimate=time_estimate)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    
    gpxtracker_pb2_grpc.add_GPXTrackerServicer_to_server(GPXTracker(), server)
    server.add_insecure_port("[::]:" + str(PORT))
    server.start()

    log.info("Listening on " + str(PORT))
    server.wait_for_termination()

if __name__ == "__main__":
    serve()