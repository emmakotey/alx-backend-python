#!/usr/bin/env python3

from typing import Union, Tuple
"""This function converts a Python variable to a KV pair"""


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Converts a Python variable to a KV pair."""
    return k, v ** 2
