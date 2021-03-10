import pandas as pd
import numpy
import struct


def csvlinecount(pospath):
    charcount = 0
    linecount = 0
    
    arr = []

    with open(pospath, 'rb') as f:
        for line in f:
            charcount = charcount + len(line)
            linecount = linecount + 1
    
        print(str(charcount/16) + " atoms to transfer to CSV")
        return(charcount/16)





def csvbuildcount(pospath):
    chararr = []
    bigarr = []
    charcount = 0
    linecount = 0

    case = 1

    with open(pospath, 'rb') as f:
        marker = 0

        line = f.readline()
        for i in range(int(csvlinecount(pospath))): #(int(len(line)/16)):
            if(marker+16  <= len(line)):
                e = struct.unpack('>'+'ffff', line[marker:marker+16]) #4*n
                marker = marker + 16
                chararr = list(e)
                bigarr.append(chararr)

            else:
                byteLong = True
                newline = f.readline()
                if(len(line[marker:len(line)])+len(newline)<16):
                    byteLong = False
                if(byteLong == True):
                    bytestring = line[marker:len(line)]+newline[0:16-(len(line)-marker)]
                    marker = 16-(len(line)-marker)
                    line = newline

                if(byteLong == False):
                    bytestring = line[marker:len(line)]+newline
    

                    while(len(bytestring) < 16):
                        nextline = f.readline()

                        if(len(nextline) > 16 - len(bytestring)):
                            marker = 16-len(bytestring)
                            bytestring = bytestring + nextline[0:16-len(bytestring)]
                            line = nextline

                        if(len(nextline) <= 16 - len(bytestring)):
                            bytestring = nextline + bytestring            
                    
                #print(len(bytestring))
               
                e = struct.unpack('>'+'ffff', bytestring)
                
                #line = newline
                chararr = list(e)
                bigarr.append(chararr)

    csvfrompospath = pospath.replace(".pos", "-posconverted.csv")
    pd.DataFrame(bigarr).to_csv(csvfrompospath)

#def csvbuild(pospath):       
   #arr = []

   #with open(pospath, 'rb') as f:
   #    for line in f:
   #        #line = f.readline()
   #        if(len(line)>=16):
   #            #d = struct.unpack('>'+'fffffffffII', line[:44]) #4*n
   #            d = struct.unpack('>'+'ffff', line[:16]) #4*n
   #        barr = list(d)
   #        arr.append(barr)


   #pd.DataFrame(arr).to_csv(input("What file would you like to generate for your CSV? Include .csv extension: "))

#csvbuildcount("data\R41_03111-v01\R41_03111-v01.pos")
#exit(0)