# For VK's device
# filepath = 'steelrntest.csv'
# newpath = 'steelmod.csv'
import pandas
import matplotlib.pyplot as plt

def colcheck():
    colname = input('Which column would you like to compare between old and new CSV files? Type column header: ')
    filepath = input("What is the old CSV filepath? Include file name (.../name.csv): ")
    newpath = input("What is the modified CSV's filepath? Include file name (.../name.csv): ")


    df = pandas.read_csv(filepath)
    print(df[colname])
    df = pandas.read_csv(newpath)
    print(df[colname]) 
