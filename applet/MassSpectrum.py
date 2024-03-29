import pandas as pd
import matplotlib.pyplot as plt



def makespec(csvfrompospath):
    df = pd.read_csv(csvfrompospath)
    df = df["3"]

    binsize = float(input("What's your binsize?: "))
    length = int(input("What is the max charge to mass ratio you want?: "))
    
    binN = int(length/binsize)
    marker = 0
    count = [0]*binN
    tally = [0]*binN

    for i in range(binN):
        count[i] = marker
        marker+=binsize

    print(count)

    for i in df:
        for j in range(len(count)):
            if(i>(count[j]-binsize/2) and i<(count[j]+binsize/2)):
                tally[j] += 1
            

    print(tally)

    plt.scatter(x = count, y = tally)
    plt.ylabel("Frequency")
    plt.xlabel("Mass to Charge Ratio (m/z)")
    plt.title("Mass Spectrum")

    #for i in range(len(count)):
    #    plt.plot(    [count[i], tally[i]], [count[i], 0]     )    
    
    plt.stem(count, tally)
    
    plt.show()
    #print(tally)
    