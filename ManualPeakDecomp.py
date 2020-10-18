# import csv
import pandas
# import tkinter as tk
import matplotlib.pyplot as plt
# import numpy as np

# For VK's device
# filepath is the original CSV file
# modpath, the intermediate, does not need to be created manually, the program will do it
# newpath, the final CSV, also does not need to be created manually, the program will do it
#filepath = "/Users/vishal/Documents/MATLAB/python_scripts/steelrntest.csv"
#modpath = "/Users/vishal/Documents/MATLAB/python_scripts/steelmod.csv"
#newpath = "/Users/vishal/Documents/MATLAB/python_scripts/steelgraph.csv"

# Peak Decomposition %s

# Fe 12.89674948
# Al 86.53753737
# Cr 0.5657131534
# Unknown Peak Column: Rn % (27Da)

#Columns irrelevant to analysis (7): NiH %, C2 %, C3 %, C4 %, Ca %, Ga %, H %

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
namearr = [] # collects element names to search for in CSV
multarr = [] # connects elements to percentage composition
peakName = input("What is the name of the unknown peak column? ")
for i in range(0, int(peakEN)):
    namearr.append(input('What is element number '+str(i+1)+' in the peak? Use element symbol (Ex. Fe): '))
    multarr.append(0.01*float(input(str(namearr[i])+ " makes up what percent of the peak? ")))

print(namearr)
print(multarr)
print(peakName)

headarr = []
for i in namearr:
    headarr.append(i + ' %') # CSV file headers are in the form "Al %", need to add % for parsing

print(headarr)
for i in range(0, len(headarr)-1):
    df[headarr[i]] = (df['Rn % (27Da)']*multarr[i])+df[headarr[i]] # replaces element % column with distribution added

del df['Rn % (27Da)']
df.to_csv(modpath) # writes to intermediate file

################ creation of final "graph" CSV used to generate scatterplot

df = pandas.read_csv(modpath)
colnumdisc = input("How many columns of data would you like to discard for analysis? These include columns with no data, or those such as 'Ga %' which are remnants of processes like FIB milling: ") 
trasharr = []
for i in range (0, int(colnumdisc)):
    trasharr.append(input("What is the header of the column you would like to discard? Include % (Ex. 'Ga %'): "))

print(trasharr)

# next steps include cleaning up CSV for analysis, removing Sample Count and other extraneous columns associated with dataframe and array functions 

for i in trasharr:
    df["Sample Count"] = df["Sample Count"]-df[i]
    del df[i]

newpath = input("Input filepath where you would like the new final cropped proxigram to go. Please make this distinct from the intermediate file: ")
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

# generation of scatterplot

labels = []
for i in colarray:
    labels.append(i)

print(colarray)
for i in colarray:
    plt.scatter(x = df["Distance (nm)"], y = df[i])
plt.ylabel("Concentration %")
plt.xlabel("Distance (nm)")
plt.legend(labels)
ttl = input("What would you like your plot title to be?")
plt.title(ttl)
plt.show()