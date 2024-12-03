#!/usr/bin/env python3
"""
Creates a type-annotated function floor which takes
a float n as argument and returns the floor of the float.
"""
import math


def floor(n: float) -> int:
    """Returns int floor of n"""
    return math.floor(n)
