import pandas
import matplotlib.pyplot as plt
import numpy

# Use intermediate CSV file generated in ProxigramPeakDecom.py

# On VK's system
#modpath = "steel2mod.csv"
#newpath = "steel2graph.csv"
# isotopes to delete: Cr %,C2 %,C3 %,NiH %,P %,Si %,MoC %,H %
# 1.7, 2.3, -4.9, -2.1

modpath = input("What was the filename of your intermediate CSV? Include .csv extension: ")
newpath = input("What was the filename of your final graphing CSV? Include .csv extension: ")

dfmid = pandas.read_csv(modpath)
dffin = pandas.read_csv(newpath)

# print(dfmid.columns.get_loc("Distance (nm)")) # ----> col index

# print(dfmid.columns[1]) # index ----> col name

def rounding(x): # significant figure rounding
    if(x == 0):
        return 0
    else:
        return round(x, -int(numpy.floor(numpy.log10(numpy.abs(x)))))

# Error bar insertion
idx = 2
while(idx<len(dffin.columns)-1):
    if(dffin.columns[idx+1] != dffin.columns[idx] + "Err"):
        print("u can put error here")
        dffin.insert(idx + 1, dffin.columns[idx] + " Err", numpy.sqrt(dffin[dffin.columns[idx]]*(100-dffin[dffin.columns[idx]])/(dfmid["Sample Count"])))
        print("error placed")
        idx += 2

sum = 0

for i in dffin.columns:
    if(dffin.columns.get_loc(i) % 2 == 0 and dffin.columns.get_loc(i) != 0):
        sum = sum + dffin[i]


dffin.insert (len(dffin.columns), "Error Sum", sum)

del(dffin["Unnamed: 0"])

dffin.to_csv(input("What file would you like your error data to be written to? Include .csv extension: ")) 

# print(dfmid.columns.get_loc("Distance (nm)")) # ----> col index
# print(dfmid.columns[1]) # index ----> col name

############################
# Precipitate Core Composition
idx = 0
idy = 0

x = float(input("From looking at the graph and your intermediate CSV file, at what distance (nm) can the precipitate core be marked off?: "))
y = float(input("Where (nm) does your precipitate core end?: "))

for i in range(0, len(dfmid["Distance (nm)"]-1)):
    if dfmid["Distance (nm)"].loc[i] == x:
        idx = i

    if dfmid["Distance (nm)"].loc[i] == y:
        idy = i


core_df = dfmid[idx:(idy+1)]
del(core_df["Unnamed: 0"])


colarray = []

for i in dfmid.columns:
    colarray.append(i)
    
colarray.remove("Sample Count")
colarray.remove("Distance (nm)")

colarray.remove("Unnamed: 0")

csstring = input("Input a comma separated list of the headers of columns you would like to delete, no spaces (Ex. Ga %,H %): ")
cslist = csstring.split(",")

for i in cslist:
    colarray.remove(i)

sumarray = []
proparray = []
errorarray = []

for i in colarray:
    sumarray.append(core_df[i].sum())

sum = 0
for i in sumarray:
    sum = sum + i

for i in sumarray:
    proparray.append((i*100/sum))

for i in range(0, len(proparray)):
    proparray[i] = float('%.2g' % proparray[i]) 

for i in proparray:
    errorarray.append(rounding(numpy.sqrt(i*(100-i)/sum)))


data = [colarray, sumarray, proparray, errorarray]

isotopeList = ""

newarr = []

for i in errorarray:
    if (str(i)[0] == "0" and i != 0):
        newarr.append(str(i)[2])
    else:
        newarr.append(str(i)[0])
print("Precipitate core composition: ")
for i in range(0, len(colarray)):   
    print("||" + str(proparray[i])+"("+str(newarr[i])+")" + str(colarray[i]) + "||", end = ' ')
print("                                                                            ")

############################
# Matrix Core Composition

x = float(input("From looking at the graph and your intermediate CSV file, at what distance (nm) can the matrix core be marked off?: "))
y = float(input("Where (nm) does your matrix core end?: "))

for i in range(0, len(dfmid["Distance (nm)"]-1)):
    if dfmid["Distance (nm)"].loc[i] == x:
        idx = i

    if dfmid["Distance (nm)"].loc[i] == y:
        idy = i


matrix_df = dfmid[idx:(idy+1)]
del(matrix_df["Unnamed: 0"])

sumarray = []
proparray = []
errorarray = []

for i in colarray:
    sumarray.append(matrix_df[i].sum())

sum = 0
for i in sumarray:
    sum = sum + i

for i in sumarray:
    proparray.append((i*100/sum))

for i in range(0, len(proparray)):
    proparray[i] = float('%.4g' % proparray[i]) 

for i in proparray:
    errorarray.append(rounding(numpy.sqrt(i*(100-i)/sum)))


data = [colarray, sumarray, proparray, errorarray]

isotopeList = ""

newarr = []

for i in errorarray:
    if (str(i)[0] == "0" and i != 0):
        newarr.append(str(i)[2])
    else:
        newarr.append(str(i)[0])
print("Matrix core composition: ")
for i in range(0, len(colarray)):
    print("||" + str(proparray[i])+"("+str(newarr[i])+")" + str(colarray[i]) + "||", end = ' ')
print("                                                                            ")
########################## 
# Entire Sample Statistics

sumarray = []
proparray = []
errorarray = []

for i in colarray:
    sumarray.append(dfmid[i].sum())

sum = 0
for i in sumarray:
    sum = sum + i

for i in sumarray:
    proparray.append((i*100/sum))

for i in range(0, len(proparray)):
    proparray[i] = float('%.5g' % proparray[i]) 

for i in proparray:
    errorarray.append(rounding(numpy.sqrt(i*(100-i)/sum)))


data = [colarray, sumarray, proparray, errorarray]

isotopeList = ""

newarr = []

for i in errorarray:
    if (str(i)[0] == "0" and i != 0):
        newarr.append(str(i)[2])
    else:
        newarr.append(str(i)[0])
print("Entire Analysis: ")
for i in range(0, len(colarray)):
    print("||" + str(proparray[i])+"("+str(newarr[i])+")" + str(colarray[i]) + "||", end = ' ')
print("                                                                            ")

print(data)
print(dfmid["Sample Count"].sum())
