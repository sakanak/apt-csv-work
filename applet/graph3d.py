import matplotlib.pyplot as plt
import numpy as np
import pandas as pd 

def plotpoints():
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')


    n = 100

    df = pd.read_csv("data\steelnew\steelnewpos.csv")

    # For each set of style and range settings, plot n random points in the box
    # defined by x in [23, 32], y in [0, 100], z in [zlow, zhigh].
    for m, zlow, zhigh in [('o', -50, -25), ('^', -30, -5)]:
        xs = df["1"]
        ys = df["2"]
        zs = df["3"]
        ax.scatter(xs, ys, zs, marker=m)

    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')

    plt.show()