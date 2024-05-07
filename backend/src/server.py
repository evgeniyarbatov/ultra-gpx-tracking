import grpc
import gpxtracker_pb2
import gpxtracker_pb2_grpc
import logging
import sys

from concurrent import futures

PORT = 9090

log = logging.getLogger("grpc-server")
logging.basicConfig(
    format='%(asctime)s %(message)s',
    level=logging.DEBUG, 
    stream=sys.stdout,
    datefmt='%Y-%m-%d %H:%M:%S',
)

class GPXTracker(gpxtracker_pb2_grpc.GPXTrackerServicer):
    def GetAddress(self, request, context):
        log.info(f"GetAddress")
        return gpxtracker_pb2.AddressResponse(address=f"Current address")

    def GetRemainginDistance(self, request, context):
        log.info(f"GetRemainginDistance")
        return gpxtracker_pb2.DistanceResponse(distance=322.0)

    def GetCoveredDistance(self, request, context):
        log.info(f"GetCoveredDistance")
        return gpxtracker_pb2.DistanceResponse(distance=0.0)

    def GetTimeEstimate(self, request, context):
        log.info(f"GetTimeEstimate")
        return gpxtracker_pb2.TimeResponse(timestamp="2022-05-21 23:00:00")

    def GetGPXFile(self, request, context):
        log.info(f"GetGPXFile")
        return gpxtracker_pb2.GPXFile(xml="XML file contents")

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    
    gpxtracker_pb2_grpc.add_GPXTrackerServicer_to_server(GPXTracker(), server)
    server.add_insecure_port("[::]:" + str(PORT))
    server.start()

    log.info("Listening on " + str(PORT))
    server.wait_for_termination()

if __name__ == "__main__":
    serve()