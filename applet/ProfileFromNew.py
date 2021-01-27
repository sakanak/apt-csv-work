import pandas
import matplotlib.pyplot as plt
import numpy

# c:\Git\apt-csv-work\data\10Nisteelgraph.csv
# c:\Git\apt-csv-work\data\10Ni_steel.csv
# On VK's machine
# modpath = "steel2mod.csv"
# newpath = "steel2graph.csv"
# errorpath = "steel2error.csv"
# isotopes to delete: Cr %,C2 %,C3 %,NiH %,P %,Si %,MoC %,H %
def proxplot():
    newpath = input("What was the filename of your final graphing CSV? Include .csv extension: ")
    
    
    dffin = pandas.read_csv(newpath)

    # colarray creation 
    colarray = []

    for i in dffin.columns:
        colarray.append(i)
        
    colarray.remove("Distance (nm)")

    colarray.remove("Unnamed: 0")


    ##########################

    labels = []
    for i in colarray:
        labels.append(i)



    print(colarray)
    for i in colarray:
        plt.scatter(x = dffin["Distance (nm)"], y = dffin[i])


    plt.ylabel("Concentration at%")
    plt.xlabel("Distance (nm)")
    plt.legend(labels)
    ttl = input("What would you like your plot title to be?: ")
    plt.title(ttl)
    plt.show()


proxplot()