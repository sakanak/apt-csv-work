import tkinter as tk 
import pandas
import matplotlib.pyplot as plt
import numpy as np
import GibbsInterfacialExcess, PosToCSV, ProxigramError, ProxigramPeakDecomp, ProxigramProfilePlot, ColumnModCheck, graph3d

window = tk.Tk()
window.title("GUI")


label = tk.Label(window, text = "Hello World!").pack()
window.geometry('400x200')



def gibbsclicked():
    print("clicked")
    GibbsInterfacialExcess.getExcess()

def colmodcheckclicked():
    print("clicked")
    ColumnModCheck.colcheck()
    
def postocsvclicked():
    print("clicked")
    PosToCSV.csvbuild()
    
def graphclicked(): 
    print("clicked")
    graph3d.plotpoints()
    
def proxplotclicked():
    print("clicked")
    ProxigramProfilePlot.proxplot()
    
def proxerrorclicked():
    print("clicked")
    ProxigramError.proxerror()


def proxpeakdecompclicked():
    print("clicked")
    ProxigramPeakDecomp.entiredecomp()

btcolmod = tk.Button(window, text = "Column Mod Check", command = colmodcheckclicked).pack()
btgibbs = tk.Button(window, text = "Gibbsian Interfacial Excess", command = gibbsclicked).pack()
btgraph = tk.Button(window, text = "Graph POS CSV", command = graphclicked).pack()
btposcsv = tk.Button(window, text = "Create CSV from POS", command = postocsvclicked).pack()
btproxerror = tk.Button(window, text = "Generate Proxigram Error CSV", command = proxerrorclicked).pack()
btproxpeakdecomp = tk.Button(window, text = "Manual Proxigram Peak Decomposition", command = proxpeakdecompclicked).pack()
btproxprofplot = tk.Button(window, text = "Generate Proxigram Profile Plot", command = proxplotclicked).pack()

window.mainloop()