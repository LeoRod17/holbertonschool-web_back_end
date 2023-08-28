#!/usr/bin/env python3
"""Making a function that returns a tuple"""
from typing import Tuple, Union
import math


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """a function that returns a text and a float in a tuple"""
    sq: float = v**2
    return (k, sq)
