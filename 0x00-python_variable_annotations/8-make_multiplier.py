#!/usr/bin/env python3
"""takes in flaot, returns ftn that multiplies
float by multiplier"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """returns a ftn"""
    def multiply(value: float) -> float:
        return value * multiplier
    return multiply
