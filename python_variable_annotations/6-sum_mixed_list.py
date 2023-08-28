#!/usr/bin/env python3
"""Making an add function for lists"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """a function that adds all the floats of a list"""
    sums: float = 0
    for x in mxd_lst:
        sums += x
    return sums
