#!/usr/bin/env python3
"""make_multiplier function
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """make_multiplier
    Args:
        multiplier (float): number
    Returns:
        Callable[[float], float]: float
    """
    return lambda x: x * multiplier
