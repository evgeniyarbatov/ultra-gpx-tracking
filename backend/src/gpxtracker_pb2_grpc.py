# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

import gpxtracker_pb2 as gpxtracker__pb2

GRPC_GENERATED_VERSION = '1.63.0'
GRPC_VERSION = grpc.__version__
EXPECTED_ERROR_RELEASE = '1.65.0'
SCHEDULED_RELEASE_DATE = 'June 25, 2024'
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    warnings.warn(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in gpxtracker_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
        + f' This warning will become an error in {EXPECTED_ERROR_RELEASE},'
        + f' scheduled for release on {SCHEDULED_RELEASE_DATE}.',
        RuntimeWarning
    )


class GPXTrackerStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetLocationInfo = channel.unary_unary(
                '/main.GPXTracker/GetLocationInfo',
                request_serializer=gpxtracker__pb2.LocationRequest.SerializeToString,
                response_deserializer=gpxtracker__pb2.LocationResponse.FromString,
                _registered_method=True)
        self.GetGPXFile = channel.unary_unary(
                '/main.GPXTracker/GetGPXFile',
                request_serializer=gpxtracker__pb2.LocationRequest.SerializeToString,
                response_deserializer=gpxtracker__pb2.GPXFileResponse.FromString,
                _registered_method=True)


class GPXTrackerServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetLocationInfo(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetGPXFile(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_GPXTrackerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetLocationInfo': grpc.unary_unary_rpc_method_handler(
                    servicer.GetLocationInfo,
                    request_deserializer=gpxtracker__pb2.LocationRequest.FromString,
                    response_serializer=gpxtracker__pb2.LocationResponse.SerializeToString,
            ),
            'GetGPXFile': grpc.unary_unary_rpc_method_handler(
                    servicer.GetGPXFile,
                    request_deserializer=gpxtracker__pb2.LocationRequest.FromString,
                    response_serializer=gpxtracker__pb2.GPXFileResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'main.GPXTracker', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class GPXTracker(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetLocationInfo(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/main.GPXTracker/GetLocationInfo',
            gpxtracker__pb2.LocationRequest.SerializeToString,
            gpxtracker__pb2.LocationResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetGPXFile(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/main.GPXTracker/GetGPXFile',
            gpxtracker__pb2.LocationRequest.SerializeToString,
            gpxtracker__pb2.GPXFileResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
