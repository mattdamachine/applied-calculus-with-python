from sympy import *
from sympy.plotting import *


def deriv_calculator(f):
    x = Symbol("x")
    d = Derivative(f, x).doit()
    return d


def find_tangent_line(x, x_val):
    y_val = f.subs(x, x_val)
    m = df.subs(x, x_val)

    tan_eq = m * (x - x_val) + y_val

    return tan_eq, y_val


if __name__ == "__main__":
    f = sympify(input("Enter a function: "))
    x_val = input(
        "Enter an x value to evaluate the derivative at or press enter to return as a function: "
    )

    df = deriv_calculator(f)

    if len(x_val) == 0:
        print("The Derivative is: ", df)
    else:
        print("The derivative is: ", df)
        x, y = symbols("x y")

        x_val = int(x_val)
        tan_eq, y_val = find_tangent_line(x, x_val)

        p = plot(f, tan_eq, (x, -10, 10), show=False)
        p.markers = [
            {
                "args": [[x_val], [y_val]],
                "color": "r",
                "marker": "s",
                "linestyle": "None",
            },
        ]
        p.legend = True
        p.axis_center = (0, 0)
        p.show()
