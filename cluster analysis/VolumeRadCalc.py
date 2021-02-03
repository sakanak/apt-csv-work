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

molOmega = float(input("In nm^3, what is your Average Atomic Volume for the isotope of interest?: "))
#dMax = float(input("What is your d-max (nm)?: "))
#order = float(input("What is your order (ions)?: "))
#nMin = float(input("What is your N-min (ions)?: "))
#length = float(input("What is your l (nm)?: "))
#dErosion = float(input("What is your d-erosion paramter (nm)?: "))
clusterCount = int(input("How many clusters do you have?: "))
if(bounded == True):
    multiplier = 2
else:
    multiplier = 4


df = pandas.read_csv(input("Input CSV filepath: "))

#print(df)

dfvolume = df["Solute Ions"][1:clusterCount+1]*multiplier*molOmega # Sphere volumes
dfrad = (dfvolume*3/(4*numpy.pi))**(1/3) # Equivalent Radii (nm)

stats = [numpy.std(dfvolume), numpy.std(dfrad)]

volTotal = 0
radTotal = 0

for i in dfvolume[1:clusterCount+1]:
    volTotal = volTotal + i

for i in dfrad[1:clusterCount+1]:
    radTotal = radTotal + i

volAvg = volTotal/clusterCount
radAvg = radTotal/clusterCount

print("Average Volume is: " + str(volAvg) + " nm^3 and Average Radius is " + str(radAvg) + " nm." )
print("Number of Features: " + str(clusterCount))
print("Standard deviation of volume in nm^3: " + str(stats[0]))
print("Standard deviation of radius in nm: " + str(stats[1]))
