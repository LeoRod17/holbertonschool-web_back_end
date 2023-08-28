#!/usr/bin/env python3
"""a function that returns a float multiplied by itself"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """a function that returns a float multiplied by itself"""
    def mult(num: float) -> float:
        res = num * multiplier
        return res
    return mult
