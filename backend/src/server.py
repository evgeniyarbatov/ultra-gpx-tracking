import grpc
import logging
import gpxtracker_pb2
import gpxtracker_pb2_grpc

from concurrent import futures

PORT = 9090

class GPXTracker(gpxtracker_pb2_grpc.GPXTrackerServicer):
    def GetAddress(self, request, context):
        return gpxtracker_pb2.Response(address=f"Current address")

    def GetRemainginDistance(self, request, context):
        return gpxtracker_pb2.Response(distance=322.0)

    def GetCoveredDistance(self, request, context):
        return gpxtracker_pb2.Response(distance=0.0)

    def GetTimeEstimate(self, request, context):
        return gpxtracker_pb2.Response(timestamp="2022-05-21 23:00:00")

    def GetGPXFile(self, request, context):
        return gpxtracker_pb2.Response(xml="XML file contents")

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    gpxtracker_pb2_grpc.add_GPXTrackerServicer_to_server(GPXTracker(), server)
    server.add_insecure_port("[::]:" + str(PORT))
    server.start()
    print("Server started, listening on " + str(PORT))
    server.wait_for_termination()

if __name__ == "__main__":
    logging.basicConfig()
    serve()