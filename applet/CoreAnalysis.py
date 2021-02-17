import pandas

def coreAnalyze(filepath, modpath, newpath):
        # for VK's data, core # = 85

        df = pandas.read_csv(modpath)
        df["Distance (nm)"] = df["Distance (nm)"].round(decimals=2)
        del(df["Unnamed: 0"])
        df.to_csv(modpath)

        x = float(input("From looking at the graph and your intermediate CSV file, at what distance (nm) can the core be marked off?: "))
        y = float(input("Where (nm) does your core end?: "))

        for i in range(0, len(df["Distance (nm)"]-1)):
            if df["Distance (nm)"].loc[i] == x:
                idx = i

            if df["Distance (nm)"].loc[i] == y:
                idy = i


        core_df = df[idx:(idy+1)]


        meanarray = []
        stdevarray = []
        sumarray = []

        for i in colarray:
            sumarray.append(core_df[i].sum())
        
        df = pandas.read_csv(newpath)

        percentcore_df = df[idx:]
        for i in colarray:
            meanarray.append(percentcore_df[i].mean())
            stdevarray.append(percentcore_df[i].std())
        
        print("Compounds:")
        print(colarray)
        print("Sum:")
        print(sumarray)
        print("Average %:")
        print(meanarray)
        print("Standard Deviation:")
        print(stdevarray)

        statdf = pandas.DataFrame({"Elements": colarray, "Sum": sumarray, "Avg at%": meanarray, "St Dev": stdevarray})
        #statname = input("What do you want to name your core statistics file? Include .csv: ")
        statname = filepath.replace(".csv", "-finalpercent.csv")
        statdf.to_csv(statname)
        #Transpose Core Stats: pandas.read_csv(statname, header = None).T.to_csv(statname, header = False, index = True)