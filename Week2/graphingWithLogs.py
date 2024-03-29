import numpy as np
import matplotlib.pyplot as plt
import math


def create_graph():
    # return 2000 evenly spaced samples in an array from .001 to 16
    x = np.linspace(0.001, 16, 2000)

    print(len(x))

    y_e = np.log(x)  # natural log (y = ln x)
    y_10 = np.log10(x)  # y = log_10(x)
    y_2 = np.log2(x)  # y = log_2(x)

    plt.plot(x, y_e)
    plt.plot(x, y_10)
    plt.plot(x, y_2)

    plt.legend(["ln", "log10", "log2"], loc="lower right")
    plt.xticks(range(math.floor(min(x)), math.ceil(max(x)) + 1))
    plt.axhline(0, color="black", linewidth="0.5")
    plt.axvline(0, color="black", linewidth="0.5")

    plt.show()


if __name__ == "__main__":
    create_graph()
