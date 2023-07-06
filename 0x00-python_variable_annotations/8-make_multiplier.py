#!/usr/bin/env python3
"""This code includes a function that performs the multiplication of a float by a given multiplier"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    
    def multiplier_func(number: float) -> float:
        """fload is multiplied by a multiplier"""
        return multiplier * number

    return multiplier_func
