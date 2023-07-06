#!/usr/bin/env python3
"""This is a  function with annotated parameters and
return values with appropriate type"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]
                   ) -> List[Tuple[Sequence, int]]:
    """Returns value"""
    return [(i, len(i)) for i in lst]
