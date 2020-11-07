import pandas
import matplotlib.pyplot as plt
import numpy

# Use intermediate CSV file generated in ProxigramPeakDecom.py

# On VK's system
# modpath = "steel2mod.csv"
# newpath = "steel2graph.csv"

modpath = input("What was the filename of your intermediate CSV? Include .csv extension: ")
newpath = input("What was the filename of your final graphing CSV? Include .csv extension: ")

dfmid = pandas.read_csv(modpath)
dffin = pandas.read_csv(newpath)

# print(dfmid.columns.get_loc("Distance (nm)")) # ----> col index

# print(dfmid.columns[1]) # index ----> col name

idx = 2
if(idx < len(dffin.columns)):
    if(dffin.columns[idx + 1] != dffin.columns[idx]):
        dffin.insert(idx + 1, dffin.columns[idx] + " Err", numpy.sqrt(dffin[dffin.columns[idx]]*(100-dffin[dffin.columns[idx]])/(dfmid["Sample Count"])))
        idx = idx + 2
    else:
        idx = idx + 2

sum = 0

for i in dffin.columns:
    if(dffin.columns.get_loc(i) % 2 == 0):
        sum = sum + dffin[i]

dffin.insert (len(dffin.columns), "Error Sum", sum)

del(dffin["Unnamed: 0"])

dffin.to_csv(input("What file would you like your error data to be written to? Include .csv extension: "))


