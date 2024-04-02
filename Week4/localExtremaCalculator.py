# local min/max calculator
# assume fn is differentiable

from sympy import *
from sympy.parsing.sympy_parser import parse_expr


def local_extrema_calc(f, x):
    x = Symbol("x")
    max_list = []
    min_list = []

    # find f'
    dy = Derivative(f, x).doit()
    print("The derivative is: ", dy)

    # find critical points (set dy = 0)
    critical_points = solve(dy, x)
    print("The critical points are x = ", critical_points)

    # find f''
    d2f = Derivative(f, x, 2).doit()

    # check second derivative test
    for point in critical_points:
        cp = d2f.subs({x: point}).evalf()
        if cp > 0:
            print("x = ", point.evalf(3), " is a local minimum")
            y = parse_expr(f).subs({x: point}).evalf()
            y = round(float(y), 2)
            min_list.append(y)
        elif cp < 0:
            print("x = ", point.evalf(3), " is a local maximum")
            y = parse_expr(f).subs({x: point}).evalf()
            y = round(float(y), 2)
            max_list.append(y)
        else:  # (cp == 0)
            print("Unable to determine if ", cp, "is min or max")

    # find local min/max
    print("Local max(es) of ", f, " is ", max_list)
    print("Local min(s) of ", f, " is ", min_list)


if __name__ == "__main__":
    f = input("Enter a function: ")
    x = input("Enter a variable to differentiate with respect to: ")
    local_extrema_calc(f, x)
