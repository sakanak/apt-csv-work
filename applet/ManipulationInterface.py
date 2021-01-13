import tkinter as tk 
import pandas
import matplotlib.pyplot as plt
import numpy as np
import GibbsInterfacialExcess, PosToCSV, ProxigramError, ProxigramPeakDecomp, ProxigramProfilePlot, ColumnModCheck, graph3d, MassSpectrum


#Data on VK's system: c:\Git\apt-csv-work\data\steel2\steel2.csv

window = tk.Tk()
window.title("Proxigram Modification")

window.geometry('500x500')



label = tk.Label(window, text = "What is your original proxigram CSV filepath?").pack()
fileentry = tk.Entry(window)
fileentry.pack()

label = tk.Label(window, text = "What is the filepath of your modified proxigram CSV? \n (Generated by Manual Peak Decomposition)").pack()
modentry = tk.Entry(window)
modentry.pack()

label = tk.Label(window, text = "What is the filepath of the at% proxigram CSV \n from which you will plot a profile? (Generated by MPD)").pack()
newentry = tk.Entry(window)
newentry.pack()

label = tk.Label(window, text = "What is the filepath of the POS file").pack()
posentry = tk.Entry(window)
posentry.pack()

label = tk.Label(window, text = "What is the filepath of the CSV you generated from POS file").pack()
csvfromposentry = tk.Entry(window)
csvfromposentry.pack()

label = tk.Label(window, text = "What was the filename of your error CSV? Include .csv extension:").pack()
errorentry = tk.Entry(window)
errorentry.pack()

filepath = "filler"
modpath = "filler"
newpath = "filler"

def entryfilled():
    global filepath
    global modpath
    global newpath
    global pospath
    global csvfrompospath
    global errorpath
    filepath = fileentry.get()
    modpath = modentry.get()
    newpath = newentry.get()
    pospath = posentry.get() 
    errorpath = errorentry.get() 
    csvfrompospath = csvfromposentry.get() 
    print([filepath, modpath, newpath, pospath, csvfrompospath, errorpath])

btentryfill = tk.Button(window, text = "Load entered filepaths", command = entryfilled).pack()


def gibbsclicked():
    print("clicked")
    print("this is ur modpath: " + modpath)
    GibbsInterfacialExcess.getExcess(modpath)

def colmodcheckclicked():
    print("clicked")
    ColumnModCheck.colcheck(filepath, newpath)
    
def postocsvclicked():
    print("clicked")
    PosToCSV.csvbuildcount(pospath)
    
def graphclicked(): 
    print("clicked")
    graph3d.plotpoints(csvfrompospath)
    
def proxplotclicked():
    print("clicked")
    ProxigramProfilePlot.proxplot(modpath, newpath, errorpath)
    
def proxerrorclicked():
    print("clicked")
    ProxigramError.proxerror(modpath, newpath)


def proxpeakdecompclicked():
    print("clicked")
    ProxigramPeakDecomp.entiredecomp()

def massspecclicked():
    print("clicked")
    MassSpectrum.makespec(csvfrompospath)

btcolmod = tk.Button(window, text = "Column Mod Check", command = colmodcheckclicked).pack()
btgibbs = tk.Button(window, text = "Gibbsian Interfacial Excess", command = gibbsclicked).pack()
btgraph = tk.Button(window, text = "Graph POS CSV", command = graphclicked).pack()
btposcsv = tk.Button(window, text = "Create CSV from POS", command = postocsvclicked).pack()
btproxerror = tk.Button(window, text = "Generate Proxigram Error CSV", command = proxerrorclicked).pack()
btproxpeakdecomp = tk.Button(window, text = "Manual Proxigram Peak Decomposition", command = proxpeakdecompclicked).pack()
btproxprofplot = tk.Button(window, text = "Generate Proxigram Profile Plot", command = proxplotclicked).pack()
btmassspec = tk.Button(window, text = "Generate Mass Spectrum", command = massspecclicked).pack()





window.mainloop()