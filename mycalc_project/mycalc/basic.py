"""
basic 모듈

기본 사칙연산 및 나눗셈 관련 함수들을 제공합니다.
"""

from .utils import ensure_number, Number


def add(a: Number, b: Number) -> Number:
    """
    덧셈: a + b
    """
    a = ensure_number(a, "a")
    b = ensure_number(b, "b")
    return a + b


def subtract(a: Number, b: Number) -> Number:
    """
    뺄셈: a - b
    """
    a = ensure_number(a, "a")
    b = ensure_number(b, "b")
    return a - b


def multiply(a: Number, b: Number) -> Number:
    """
    곱셈: a * b
    """
    a = ensure_number(a, "a")
    b = ensure_number(b, "b")
    return a * b


def divide(a: Number, b: Number) -> float:
    """
    나눗셈: a / b

    b가 0이면 ZeroDivisionError를 발생시킵니다.
    """
    a = ensure_number(a, "a")
    b = ensure_number(b, "b")
    if b == 0:
        raise ZeroDivisionError("b must not be zero in divide()")
    return a / b


def int_divide(a: Number, b: Number) -> int:
    """
    정수 나눗셈: a // b

    b가 0이면 ZeroDivisionError를 발생시킵니다.
    """
    a = ensure_number(a, "a")
    b = ensure_number(b, "b")
    if b == 0:
        raise ZeroDivisionError("b must not be zero in int_divide()")
    return int(a // b)


def mod(a: Number, b: Number) -> Number:
    """
    나머지 연산: a % b

    b가 0이면 ZeroDivisionError를 발생시킵니다.
    """
    a = ensure_number(a, "a")
    b = ensure_number(b, "b")
    if b == 0:
        raise ZeroDivisionError("b must not be zero in mod()")
    return a % b
