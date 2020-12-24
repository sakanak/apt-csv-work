import pandas
import numpy

def getExcess():
    modpath = input("What was the filename of your intermediate CSV? Include .csv extension: ")

    dfmid = pandas.read_csv(modpath)

    def rounding(x): # significant figure rounding
        if(x == 0):
            return 0
        else:
            return round(x, -int(numpy.floor(numpy.log10(numpy.abs(x)))))

    #########
    # Make colarray
    #########

    colarray = []

    for i in dfmid.columns:
        colarray.append(i)
        
    colarray.remove("Sample Count")
    colarray.remove("Distance (nm)")

    colarray.remove("Unnamed: 0")

    ##############
    print(colarray)
    ##############

    sumarray = []
    proparray = []

    for i in colarray:
        sumarray.append(dfmid[i].sum())

    sum = 0
    for i in sumarray:
        sum = sum + i

    for i in sumarray:
        proparray.append((i/sum))

    data = [colarray, sumarray, proparray]

    print(proparray)

    print("Total Sample Count: " + str(dfmid["Sample Count"].sum()))



    ######################
    # Gibbsian interfacial excess of solute calculation
    ######################


    idx = 0
    head = ""
    head = input("What header would you like a Co for?: ")
    for i in range(0, len(colarray)):
        if head == colarray[i]:
            idx = i

    c0 = proparray[idx] 
    cnarray = []
    gibbsfinal = 0
    cN = 0
    gibbsI = 0
    delL = float('%.3g' % (dfmid["Distance (nm)"][1] - dfmid["Distance (nm)"][0])) 
    area = 0

    a = float(input("What is your lattice parameter?"))

    # molarmass = 58.6934
    lp = 4
    # avo = 6.0221409e+23

    for i in range(0, len(dfmid["Distance (nm)"])):

        n = dfmid["Sample Count"][i]
        # rho = lp*molarmass/((a**3)*avo)
        rho  = lp/(a**3)
        area = n/(rho*delL)

        cN = dfmid[head][i]/n
        gibbsI = (cN-c0)/(1-c0)/area 
        cnarray.append(gibbsI)

        gibbsfinal = gibbsfinal + gibbsI
        
    print(rho)
    print("Gibbsian interfacial excess of " + head + " solute = " + str(gibbsfinal*-1) + " molecules/nm^2") # formula gives negative of excess, because cN - c0


# print(dfmid.columns.get_loc("Distance (nm)")) # ----> col index
# print(dfmid.columns[1]) # index ----> col name