#!/usr/bin/env python3
"""This method gets value from a dictionary."""
from typing import Mapping, Any, Union, TypeVar, Optional

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Optional[T] = None) -> Union[Any, T]:
    """safely revtrieve value from dictionary.
    Args:
        dct (dict): The dictionary.
        key (str): The key .
        default (any): Returned value.
    Returns:
        Value from dictionary.
    """
    if key in dct:
        return dct[key]
    else:
        return default
