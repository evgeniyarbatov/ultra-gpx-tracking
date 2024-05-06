// GENERATED CODE -- DO NOT EDIT!

'use strict';
var grpc = require('grpc');
var gpxtracker_pb = require('./gpxtracker_pb.js');

function serialize_AddressResponse(arg) {
  if (!(arg instanceof gpxtracker_pb.AddressResponse)) {
    throw new Error('Expected argument of type AddressResponse');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_AddressResponse(buffer_arg) {
  return gpxtracker_pb.AddressResponse.deserializeBinary(new Uint8Array(buffer_arg));
}

function serialize_DistanceResponse(arg) {
  if (!(arg instanceof gpxtracker_pb.DistanceResponse)) {
    throw new Error('Expected argument of type DistanceResponse');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_DistanceResponse(buffer_arg) {
  return gpxtracker_pb.DistanceResponse.deserializeBinary(new Uint8Array(buffer_arg));
}

function serialize_GPXFile(arg) {
  if (!(arg instanceof gpxtracker_pb.GPXFile)) {
    throw new Error('Expected argument of type GPXFile');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_GPXFile(buffer_arg) {
  return gpxtracker_pb.GPXFile.deserializeBinary(new Uint8Array(buffer_arg));
}

function serialize_LocationRequest(arg) {
  if (!(arg instanceof gpxtracker_pb.LocationRequest)) {
    throw new Error('Expected argument of type LocationRequest');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_LocationRequest(buffer_arg) {
  return gpxtracker_pb.LocationRequest.deserializeBinary(new Uint8Array(buffer_arg));
}

function serialize_TimeResponse(arg) {
  if (!(arg instanceof gpxtracker_pb.TimeResponse)) {
    throw new Error('Expected argument of type TimeResponse');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_TimeResponse(buffer_arg) {
  return gpxtracker_pb.TimeResponse.deserializeBinary(new Uint8Array(buffer_arg));
}


var GPXTrackerService = exports.GPXTrackerService = {
  getAddress: {
    path: '/GPXTracker/GetAddress',
    requestStream: false,
    responseStream: false,
    requestType: gpxtracker_pb.LocationRequest,
    responseType: gpxtracker_pb.AddressResponse,
    requestSerialize: serialize_LocationRequest,
    requestDeserialize: deserialize_LocationRequest,
    responseSerialize: serialize_AddressResponse,
    responseDeserialize: deserialize_AddressResponse,
  },
  getRemainginDistance: {
    path: '/GPXTracker/GetRemainginDistance',
    requestStream: false,
    responseStream: false,
    requestType: gpxtracker_pb.LocationRequest,
    responseType: gpxtracker_pb.DistanceResponse,
    requestSerialize: serialize_LocationRequest,
    requestDeserialize: deserialize_LocationRequest,
    responseSerialize: serialize_DistanceResponse,
    responseDeserialize: deserialize_DistanceResponse,
  },
  getCoveredDistance: {
    path: '/GPXTracker/GetCoveredDistance',
    requestStream: false,
    responseStream: false,
    requestType: gpxtracker_pb.LocationRequest,
    responseType: gpxtracker_pb.DistanceResponse,
    requestSerialize: serialize_LocationRequest,
    requestDeserialize: deserialize_LocationRequest,
    responseSerialize: serialize_DistanceResponse,
    responseDeserialize: deserialize_DistanceResponse,
  },
  getTimeEstimate: {
    path: '/GPXTracker/GetTimeEstimate',
    requestStream: false,
    responseStream: false,
    requestType: gpxtracker_pb.LocationRequest,
    responseType: gpxtracker_pb.TimeResponse,
    requestSerialize: serialize_LocationRequest,
    requestDeserialize: deserialize_LocationRequest,
    responseSerialize: serialize_TimeResponse,
    responseDeserialize: deserialize_TimeResponse,
  },
  getGPXFile: {
    path: '/GPXTracker/GetGPXFile',
    requestStream: false,
    responseStream: false,
    requestType: gpxtracker_pb.LocationRequest,
    responseType: gpxtracker_pb.GPXFile,
    requestSerialize: serialize_LocationRequest,
    requestDeserialize: deserialize_LocationRequest,
    responseSerialize: serialize_GPXFile,
    responseDeserialize: deserialize_GPXFile,
  },
};

exports.GPXTrackerClient = grpc.makeGenericClientConstructor(GPXTrackerService);
