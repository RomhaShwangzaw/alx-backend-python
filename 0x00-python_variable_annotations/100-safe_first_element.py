#!/usr/bin/env python3
"""Ducktyping Unknown Input Types Module"""
from typing import Sequence, Any, Optional


# The types of the elements of the input are not known
def safe_first_element(lst: Sequence[Any]) -> Optional[Any]:
    """Returns the first element of lst, or None if lst doesn't exist"""
    if lst:
        return lst[0]
    else:
        return None
