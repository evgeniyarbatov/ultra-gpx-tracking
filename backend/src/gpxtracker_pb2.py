# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: gpxtracker.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10gpxtracker.proto\x12\x04main\"+\n\x0fLocationRequest\x12\x0b\n\x03lat\x18\x01 \x01(\x02\x12\x0b\n\x03lng\x18\x02 \x01(\x02\"\x8b\x01\n\x10LocationResponse\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\t\x12\x10\n\x08\x64istance\x18\x02 \x01(\x02\x12\x13\n\x0b\x63utoff_time\x18\x03 \x01(\t\x12\x12\n\nplacemarks\x18\x04 \x01(\t\x12\x15\n\rplanned_hours\x18\x05 \x01(\x02\x12\x14\n\x0cplanned_time\x18\x06 \x01(\t\"\x1e\n\x0fGPXFileResponse\x12\x0b\n\x03xml\x18\x01 \x01(\t2\x8e\x01\n\nGPXTracker\x12\x42\n\x0fGetLocationInfo\x12\x15.main.LocationRequest\x1a\x16.main.LocationResponse\"\x00\x12<\n\nGetGPXFile\x12\x15.main.LocationRequest\x1a\x15.main.GPXFileResponse\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'gpxtracker_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_LOCATIONREQUEST']._serialized_start=26
  _globals['_LOCATIONREQUEST']._serialized_end=69
  _globals['_LOCATIONRESPONSE']._serialized_start=72
  _globals['_LOCATIONRESPONSE']._serialized_end=211
  _globals['_GPXFILERESPONSE']._serialized_start=213
  _globals['_GPXFILERESPONSE']._serialized_end=243
  _globals['_GPXTRACKER']._serialized_start=246
  _globals['_GPXTRACKER']._serialized_end=388
# @@protoc_insertion_point(module_scope)
