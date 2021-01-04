import pandas as pd
import numpy
import struct


def csvbuild(pospath):       
    arr = []

    with open(pospath, 'rb') as f:
        for line in f:
            #line = f.readline()
            if(len(line)>=16):
                #d = struct.unpack('>'+'fffffffffII', line[:44]) #4*n
                d = struct.unpack('>'+'ffff', line[:16]) #4*n
            barr = list(d)
            arr.append(barr)


    pd.DataFrame(arr).to_csv(input("What file would you like to generate for your CSV? Include .csv extension: "))