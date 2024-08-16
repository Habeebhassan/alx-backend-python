#!/usr/bin/env python3
"""
first element of a sequence Argument code with correct duck-typed annotations
"""
from typing import Union, Any, Sequence


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Duck-typed function that safe_first_elemient
    """
    if lst:
        return lst[0]
    else:
        return None
