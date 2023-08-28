#!/usr/bin/env python3
"""Making an add function for lists"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """a function that adds all the floats of a list"""
    sums: float = 0
    for x in input_list:
        sums += x
    return sums
