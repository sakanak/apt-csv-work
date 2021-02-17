import pandas
import numpy

def getExcess(modpath):
    #modpath = input("What was the filename of your intermediate CSV? Include .csv extension: ")

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

    print("This is an array of the proportion of each element in the sample: ")
    print(proparray)

    print("Total Sample Count: " + str(dfmid["Sample Count"].sum()))



    ######################
    # Gibbsian interfacial excess of solute calculation
    ######################


    idx = 0
    head = ""
    head = input("What element (entire header) would you like to calculate Gibbs interfacial excess of solute for?: ")
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

    a = float(input("What is the lattice parameter of the sample matrix (nm)?: "))

    # molarmass = 58.6934

    checkCC = input("If matrix is FCC, type 'FCC'; if matrix is BCC, type 'BCC': ")
    if(checkCC == 'FCC'):
        lp = 4 # 4 for FCC, 2 for BCC
    if(checkCC == 'BCC'):
        lp = 2
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
    print("Gibbsian interfacial excess of " + head + " solute = " + str(gibbsfinal) + " molecules/nm^2") # formula gives negative of excess, because cN - c0


# print(dfmid.columns.get_loc("Distance (nm)")) # ----> col index
# print(dfmid.columns[1]) # index ----> col name