#!/usr/bin/env python3
"""ftn that returns a tuple."""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ftn that returns a tuple"""
    return (k, v**2)
