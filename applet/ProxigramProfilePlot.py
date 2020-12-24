import pandas
import matplotlib.pyplot as plt
import numpy


# On VK's machine
# modpath = "steel2mod.csv"
# newpath = "steel2graph.csv"
# errorpath = "steel2error.csv"
# isotopes to delete: Cr %,C2 %,C3 %,NiH %,P %,Si %,MoC %,H %
def proxplot():
    modpath = input("What was the filename of your intermediate CSV? Include .csv extension: ")
    newpath = input("What was the filename of your final graphing CSV? Include .csv extension: ")
    errorpath = input("What was the filename of your error CSV? Include .csv extension: ")

    dfmid = pandas.read_csv(modpath)
    dffin = pandas.read_csv(newpath)
    dferr = pandas.read_csv(errorpath)

    # colarray creation 
    colarray = []

    for i in dfmid.columns:
        colarray.append(i)
        
    colarray.remove("Sample Count")
    colarray.remove("Distance (nm)")

    colarray.remove("Unnamed: 0")

    csstring = "Cr %,C2 %,C3 %,NiH %,P %,Si %,MoC %,H %" # input("Input a comma separated list of the headers of columns you would like to delete, no spaces (Ex. Ga %,H %): ")
    cslist = csstring.split(",")

    for i in cslist:
        colarray.remove(i)

    ##########################

    labels = []
    for i in colarray:
        labels.append(i)

    errarr = []
    for i in colarray:
        errarr.append(i + " Err")


    print(colarray)
    for i in colarray:
        plt.scatter(x = dffin["Distance (nm)"], y = dffin[i])
    for j in errarr:
        for i in colarray:
            plt.errorbar(x = dffin["Distance (nm)"], y = dffin[i], yerr = dferr[j], linestyle = "None", color = "black", capsize = 1, elinewidth = .1)

    #for i in colarray:
    #   for j in errarr:
    #      plt.scatter(x = dffin["Distance (nm)"], y = dffin[i])
            #plt.errorbar(x = dffin["Distance (nm)"], y = dffin[i], yerr = dferr[j], linestyle = "None", capsize = 1)


    plt.ylabel("Concentration at%")
    plt.xlabel("Distance (nm)")
    plt.legend(labels)
    ttl = input("What would you like your plot title to be?: ")
    plt.title(ttl)
    plt.show()


