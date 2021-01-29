import pandas
import numpy

# Calculates average volume and radius for solute ions, bounded or clipped. 


# File name on VK's system:
# c:\Git\apt-csv-work\data\R41_03111-v01\stock1.xlsx

checkBounded = input("Are these bounded? Type Y for yes and N for clipped: ")

if(checkBounded == 'Y'):
    bounded = True
else:
    bounded = False

print(bounded)

molOmega = float(input("In nm^3, what is your omega parameter for the isotope of interest?: "))
dMax = float(input("What is your d-max (nm)?: "))
order = float(input("What is your order (ions)?: "))
nMin = float(input("What is your N-min (ions)?: "))
length = float(input("What is your l (nm)?: "))
dErosion = float(input("What is your d-erosion paramter (nm)?: "))
clusterCount = int(input("How many clusters do you have?: "))
if(bounded == True):
    multiplier = 2
else:
    multiplier = 4


df = pandas.read_csv(input("What's good?: "))

#print(df)

dfvolume = df["Solute Ions"][1:clusterCount+1]*multiplier*molOmega
dfrad = (dfvolume*3/(4*numpy.pi))**(1/3)


volTotal = 0
radTotal = 0

for i in dfvolume[1:clusterCount+1]:
    volTotal = volTotal + i

for i in dfrad[1:clusterCount+1]:
    radTotal = radTotal + i

volAvg = volTotal/clusterCount
radAvg = radTotal/clusterCount

print("Average Volume is: " + str(volAvg) + " nm^3 and Average Radius is " + str(radAvg) + " nm." )


