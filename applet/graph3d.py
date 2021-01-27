import matplotlib.pyplot as plt
import numpy as np
import pandas as pd 

def plotpoints(csvfrompospath):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')


    n = 100

    df = pd.read_csv(csvfrompospath)

    # For each set of style and range settings, plot n random points in the box
    # defined by x in [23, 32], y in [0, 100], z in [zlow, zhigh].
    for m, zlow, zhigh in [('o', -50, -25), ('^', -30, -5)]:
        xs = df["0"]
        ys = df["1"]
        zs = df["2"]
        ax.scatter(xs, ys, zs, s=1, marker= 'o')

    ax.set_xlabel('x (nm)')
    ax.set_ylabel('y (nm)')
    ax.set_zlabel('z (nm)')

    plt.show()