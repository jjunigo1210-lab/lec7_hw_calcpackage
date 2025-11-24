"""
scientific 모듈

과학 계산(거듭제곱, 제곱근, 팩토리얼, 조합, 순열)을 제공합니다.
"""

import math

from .utils import ensure_number, ensure_int, Number


def power(base: Number, exp: Number) -> Number:
    """
    거듭제곱: base ** exp
    """
    base = ensure_number(base, "base")
    exp = ensure_number(exp, "exp")
    return base ** exp


def sqrt(x: Number) -> float:
    """
    제곱근: sqrt(x)

    x가 음수면 ValueError를 발생시킵니다.
    """
    x = ensure_number(x, "x")
    if x < 0:
        raise ValueError("x must be non-negative in sqrt()")
    return math.sqrt(x)


def factorial(n: Number) -> int:
    """
    팩토리얼: n! (n은 0 이상의 정수)

    n < 0 이면 ValueError, 정수가 아니면 TypeError를 발생시킵니다.
    """
    n_int = ensure_int(n, "n")
    if n_int < 0:
        raise ValueError("n must be >= 0 in factorial()")
    return math.factorial(n_int)


def nCr(n: Number, r: Number) -> int:
    """
    조합: nCr = n! / (r! * (n - r)!)
    n, r은 0 이상의 정수이며, n >= r 이어야 합니다.
    """
    n_int = ensure_int(n, "n")
    r_int = ensure_int(r, "r")

    if n_int < 0 or r_int < 0:
        raise ValueError("n and r must be >= 0 in nCr()")
    if r_int > n_int:
        raise ValueError("r must be <= n in nCr()")

    return math.comb(n_int, r_int)


def nPr(n: Number, r: Number) -> int:
    """
    순열: nPr = n! / (n - r)!
    n, r은 0 이상의 정수이며, n >= r 이어야 합니다.
    """
    n_int = ensure_int(n, "n")
    r_int = ensure_int(r, "r")

    if n_int < 0 or r_int < 0:
        raise ValueError("n and r must be >= 0 in nPr()")
    if r_int > n_int:
        raise ValueError("r must be <= n in nPr()")

    return math.perm(n_int, r_int)
