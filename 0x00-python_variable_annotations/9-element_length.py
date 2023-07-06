#!/usr/bin/env python3
"""return element length"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """returns el length"""
    return [(i, len(i)) for i in lst]
