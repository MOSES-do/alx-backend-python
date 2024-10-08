#!/usr/bin/env python3
"""Complex types - Functions"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """multiplier function"""
    return lambda x: x * multiplier
