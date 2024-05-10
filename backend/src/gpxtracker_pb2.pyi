from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class LocationRequest(_message.Message):
    __slots__ = ("userid", "lat", "lng")
    USERID_FIELD_NUMBER: _ClassVar[int]
    LAT_FIELD_NUMBER: _ClassVar[int]
    LNG_FIELD_NUMBER: _ClassVar[int]
    userid: str
    lat: float
    lng: float
    def __init__(self, userid: _Optional[str] = ..., lat: _Optional[float] = ..., lng: _Optional[float] = ...) -> None: ...

class LocationResponse(_message.Message):
    __slots__ = ("address", "distance", "cutoff_time", "placemarks")
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    DISTANCE_FIELD_NUMBER: _ClassVar[int]
    CUTOFF_TIME_FIELD_NUMBER: _ClassVar[int]
    PLACEMARKS_FIELD_NUMBER: _ClassVar[int]
    address: str
    distance: float
    cutoff_time: str
    placemarks: str
    def __init__(self, address: _Optional[str] = ..., distance: _Optional[float] = ..., cutoff_time: _Optional[str] = ..., placemarks: _Optional[str] = ...) -> None: ...

class GPXFileResponse(_message.Message):
    __slots__ = ("xml",)
    XML_FIELD_NUMBER: _ClassVar[int]
    xml: str
    def __init__(self, xml: _Optional[str] = ...) -> None: ...
