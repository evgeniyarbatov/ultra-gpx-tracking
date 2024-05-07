from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class LocationRequest(_message.Message):
    __slots__ = ("lat", "lng")
    LAT_FIELD_NUMBER: _ClassVar[int]
    LNG_FIELD_NUMBER: _ClassVar[int]
    lat: float
    lng: float
    def __init__(self, lat: _Optional[float] = ..., lng: _Optional[float] = ...) -> None: ...

class AddressResponse(_message.Message):
    __slots__ = ("address",)
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    address: str
    def __init__(self, address: _Optional[str] = ...) -> None: ...

class DistanceResponse(_message.Message):
    __slots__ = ("distance",)
    DISTANCE_FIELD_NUMBER: _ClassVar[int]
    distance: float
    def __init__(self, distance: _Optional[float] = ...) -> None: ...

class TimeEstimateResponse(_message.Message):
    __slots__ = ("time_estimate",)
    TIME_ESTIMATE_FIELD_NUMBER: _ClassVar[int]
    time_estimate: str
    def __init__(self, time_estimate: _Optional[str] = ...) -> None: ...
