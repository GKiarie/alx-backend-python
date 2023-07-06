#!/usr/bin/env python3
"""ftn takes in a list of mixed inst ans floats
and returns sum as float"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """sum elements in a list"""
    return sum(mxd_lst)
