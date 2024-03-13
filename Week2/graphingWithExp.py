import numpy as np
import matplotlib.pyplot as plt
import math


def create_graph():
    x = np.linspace(0.001, 4, 2000)

    y_e = np.exp(x)
    y_2 = np.exp2(x)

    plt.plot(x, y_e)
    plt.plot(x, y_2)

    plt.legend(["e^x", "2^x", "y_3"], loc="lower right")
    plt.xticks(range(math.floor(min(x)), math.ceil(max(x)) + 1))
    plt.axhline(0, color="black", linewidth="0.5")
    plt.axvline(0, color="black", linewidth="0.5")

    plt.show()


if __name__ == "__main__":
    create_graph()
