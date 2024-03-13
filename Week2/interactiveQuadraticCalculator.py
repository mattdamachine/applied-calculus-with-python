# ax^2 + bx + c

from numpy import sqrt
from sympy.plotting import *
from sympy import Symbol


def zeros(a: float, b: float, c: float):
    # Discriminate
    D = sqrt(b * b - 4 * a * c)

    # Roots
    x1 = (-b + D) / (2 * a)
    x2 = (-b - D) / (2 * a)

    print("The first root is: ", x1)
    print("The second root is: ", x2)


def print_graph(a: float, b: float, c: float):
    x = Symbol("x")
    title = "Quadratic Graph"
    plot(a * x**2 + b * x + c, title=title)


def validate_user_input(prompt: str):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Please enter a valid number")


if __name__ == "__main__":
    print("Welcome to our quadratic calculator!")

    a = validate_user_input("Enter a: ")
    b = validate_user_input("Enter b: ")
    c = validate_user_input("Enter c: ")

    zeros(a, b, c)

    print_graph(a, b, c)
