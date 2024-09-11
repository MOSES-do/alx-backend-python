#!/usr/bin/env python3
"""String, Int, FLoat to Tuple"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """OR | Args"""
    sqr: Union[int, float] = v*v
    return (k, sqr)
