import csv
import pandas
import tkinter as tk
import matplotlib.pyplot as plt
import numpy as np

# For VK's device
#filepath = "/Users/vishal/Documents/MATLAB/python_scripts/steelrntest.csv"
#modpath = "/Users/vishal/Documents/MATLAB/python_scripts/steelmod.csv"
#newpath = "/Users/vishal/Documents/MATLAB/python_scripts/steelgraph.csv"

# Peak Decomposition %s

# Fe 12.89674948
# Al 86.53753737
# Cr 0.5657131534
# Unknown Peak Column: Rn % (27Da)

#Unnecessary columns (7): NiH %, C2 %, C3 %, C4 %, Ca %, Ga %, H %

# Tkinter GUI

# window = tk.Tk()
# label = tk.Label(text = "File Path")
# entry = tk.Entry()
# label.pack()
# entry.pack()
# filename = entry.get()

filepath = input("What is your CSV filepath? Include file name (.../name.csv): ")
modpath = input("What path would you like your modified CSV file to have? Include file name (.../name.csv): ")

df = pandas.read_csv(filepath)

peakEN = input('How many possible elements in your peak? ')
namearr = []
multarr = []
peakName = input("What is the name of the unknown peak column? ")
for i in range(0, int(peakEN)):
    namearr.append(input('What is element number '+str(i+1)+' in the peak? Use element symbol (Ex. Fe): '))
    multarr.append(0.01*float(input(str(namearr[i])+ " makes up what percent of the peak? ")))

print(namearr)
print(multarr)
print(peakName)

headarr = []
for i in namearr:
    headarr.append(i + ' %')

print(headarr)
for i in range(0, len(headarr)-1):
    df[headarr[i]] = (df['Rn % (27Da)']*multarr[i])+df[headarr[i]]

del df['Rn % (27Da)']
df.to_csv(modpath) 

#############################

df = pandas.read_csv(modpath)
colnumdisc = input("How many columns of data would you like to discard? ")
trasharr = []
for i in range (0, int(colnumdisc)):
    trasharr.append(input("What is the header of the column you would like to discard? Include % when applicable "))

print(trasharr)

for i in trasharr:
    df["Sample Count"] = df["Sample Count"]-df[i]
    del df[i]

newpath = input("Input filepath where you would like the new cropped proxigram to go. This can overwrite another CSV file if preferred: ")
df.to_csv(newpath)
print("New Sample Count:")
print(df["Sample Count"])

df = pandas.read_csv(newpath)
colarray = []
for i in df.columns:
    colarray.append(i)
print(colarray)
colarray.remove("Sample Count")
colarray.remove("Distance (nm)")


for i in colarray:
    df[i] = (df[i]/df["Sample Count"])*100

del df["Sample Count"]
del df["Unnamed: 0"]
del df["Unnamed: 0.1"]
print("headers of newpath: " + df.columns)

print(colarray)
df.to_csv(newpath)

colarray.remove("Unnamed: 0")
colarray.remove("Unnamed: 0.1")


labels = []
for i in colarray:
    labels.append(i)

print(colarray)
for i in colarray:
    plt.scatter(x = df["Distance (nm)"], y = df[i])
plt.ylabel("Concentration %")
plt.xlabel("Distance (nm)")
plt.legend(labels)
plt.show()