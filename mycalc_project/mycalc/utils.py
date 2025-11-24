"""
utils 모듈

입력 값 검증 등 공통 유틸 함수 모음.
"""

from typing import Union

Number = Union[int, float]


def ensure_number(x: Number, name: str = "value") -> Number:
    """
    x가 int 또는 float인지 확인하고, 아니면 TypeError를 발생시킵니다.
    """
    if not isinstance(x, (int, float)):
        raise TypeError(f"{name} must be int or float, got {type(x).__name__}")
    return x


def ensure_int(x: Number, name: str = "value") -> int:
    """
    x를 정수형으로 사용할 수 있는지 확인합니다.
    float인데 정수처럼 생긴 경우 (예: 5.0)는 int로 캐스팅합니다.
    """
    if isinstance(x, bool):
        raise TypeError(f"{name} must be an integer, got bool")
    if isinstance(x, float):
        if x.is_integer():
            return int(x)
        else:
            raise TypeError(f"{name} must be an integer-like value, got {x}")
    if not isinstance(x, int):
        raise TypeError(f"{name} must be int, got {type(x).__name__}")
    return x
