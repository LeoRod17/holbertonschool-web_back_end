#!/usr/bin/env python3
"""Annotate the below function parameters and return values with
    the appropriate types"""
from typing import List, Iterable, Tuple, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Making a weird function"""
    return [(i, len(i)) for i in lst]
