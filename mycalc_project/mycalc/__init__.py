"""
mycalc 패키지

기본 연산, 과학 계산, 조합/순열 등을 지원하는 간단한 계산기 패키지입니다.
"""

from .basic import (
    add,
    subtract,
    multiply,
    divide,
    int_divide,
    mod,
)

from .scientific import (
    power,
    sqrt,
    factorial,
    nCr,
    nPr,
)

__all__ = [
    # basic
    "add",
    "subtract",
    "multiply",
    "divide",
    "int_divide",
    "mod",
    # scientific
    "power",
    "sqrt",
    "factorial",
    "nCr",
    "nPr",
]
