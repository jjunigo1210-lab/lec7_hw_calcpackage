"""
main.py

mycalc 패키지가 제대로 동작하는지 테스트하는 예시 스크립트.
과제 캡처용으로도 사용 가능합니다.
"""

from mycalc import (
    add,
    subtract,
    multiply,
    divide,
    int_divide,
    mod,
    power,
    sqrt,
    factorial,
    nCr,
    nPr,
)


def main():
    print("=== 기본 연산 ===")
    print("add(10, 5)        =", add(10, 5))
    print("subtract(10, 5)   =", subtract(10, 5))
    print("multiply(10, 5)   =", multiply(10, 5))
    print("divide(10, 5)     =", divide(10, 5))
    print("int_divide(10, 3) =", int_divide(10, 3))
    print("mod(10, 3)        =", mod(10, 3))

    print("\n=== 과학 계산 ===")
    print("power(2, 10)      =", power(2, 10))
    print("sqrt(16)          =", sqrt(16))
    print("factorial(5)      =", factorial(5))
    print("nCr(5, 2)         =", nCr(5, 2))
    print("nPr(5, 2)         =", nPr(5, 2))


if __name__ == "__main__":
    main()
