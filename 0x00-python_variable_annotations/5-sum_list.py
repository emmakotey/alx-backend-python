#!/usr/bin/env python3
"""This function sums a list of floats"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """list of floats
    Args:
        input_list (list): list of floats goes here
    Returns:
        float: sum of floats
    """
    if input_list is None:
        return 0
    else:
        return sum(input_list)
