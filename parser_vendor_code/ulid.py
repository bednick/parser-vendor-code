import datetime
import os
import time
import uuid
from typing import Optional, Union

MILLISECONDS_IN_SECS = 1000
TIMESTAMP_LEN = 6
RANDOMNESS_LEN = 10
BYTES_LEN = TIMESTAMP_LEN + RANDOMNESS_LEN


def ulid() -> uuid.UUID:
    return from_bytes()


def from_datetime(value: datetime.datetime) -> uuid.UUID:
    return from_timestamp(value.timestamp())


def from_timestamp(value: Union[int, float]) -> uuid.UUID:
    if isinstance(value, float):
        value = int(value * MILLISECONDS_IN_SECS)
    timestamp = int.to_bytes(value, TIMESTAMP_LEN, "big")
    randomness = os.urandom(RANDOMNESS_LEN)
    return from_bytes(timestamp + randomness)


def from_bytes(value: Optional[bytes] = None) -> uuid.UUID:
    if value is not None and len(value) != BYTES_LEN:
        raise ValueError("ULID has to be exactly 16 bytes long.")
    return uuid.UUID(bytes=value or from_timestamp(time.time()).bytes)
