#!/usr/bin/env python3
"""module to write helper functions"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """function to calculate start and end indexes"""
    start = (page - 1) * page_size
    return start, start + page_size
