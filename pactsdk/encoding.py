import base64
from typing import Sequence

import algosdk


# Not used but may be handy for e.g. users of the lib when writing unit tests.
def serialize_uint64(values: Sequence[int]) -> str:
    _bytes = bytes(
        x
        for i in values
        for x in int.to_bytes(i, length=8, byteorder="big", signed=False)
    )
    return base64.b64encode(_bytes).decode("ascii")


def deserialize_uint64(data: str) -> list[int]:
    decoded = base64.b64decode(data)
    return [
        int.from_bytes(decoded[offset : offset + 8], byteorder="big", signed=False)
        for offset in range(0, len(decoded), 8)
    ]


def decode_string_from_global_state(encoded: str) -> str:
    return base64.b64decode(encoded).decode()


def decode_address_from_global_state(encoded: str) -> str:
    return algosdk.encoding.encode_address(base64.b64decode(encoded))
