#!/usr/bin/env python3
"""List of Floats"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """add a list of floats"""
    """total_sum = sum(x for x in input_list)
    #return total_sum"""

    i = 0
    tots = 0
    while i < len(input_list):
        tots += input_list[i]
        i += 1
    return tots
