# A tool to expand out a binomial with Pascal's Triangle into its equivalent expression

from sympy import *


def binomial_expansion(num: int, coefficients: list[int]):
    x, y = symbols('x y')

    expr = 0

    for i in range(num + 1):
        expr += coefficients[i] * x ** i * y ** (num - i)

    return expr


def pascals_triangle(numRows: int):
    pascal = [[1] * (i + 1) for i in range(numRows + 1)]

    for i in range(numRows + 1):
        for j in range(1, i):
            pascal[i][j] = pascal[i - 1][j - 1] + pascal[i - 1][j]

    return pascal[numRows]


if __name__ == "__main__":
    while True:
        try:
            exponent = int(input("What would you like to raise (x + y) to?: "))
            if exponent < 0:
                print("Exponent must be positive!")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")

    pascal_row = pascals_triangle(exponent)

    expr = binomial_expansion(exponent, pascal_row)

    print(expr)

