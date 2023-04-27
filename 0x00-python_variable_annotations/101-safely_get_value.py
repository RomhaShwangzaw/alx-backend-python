#!/usr/bin/env python3
"""More involved type annotations module"""
from typing import Mapping, Any, TypeVar, Type, Optional, Union


T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any, default:
                     Optional[T] = None) -> Union[Any, T]:
    """
    Returns the value associated with a key from a dictionary,
    or a default value if the key is not a valid value
    """
    if key in dct:
        return dct[key]
    else:
        return default
