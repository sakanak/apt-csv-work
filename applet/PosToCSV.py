import pandas as pd
import numpy
import struct

#Need to update

# character by character file parse, not line by line, until 16
# have char count

def csvbuildcount(pospath):
    chararr = []
    bigarr = []
    charcount = 0
    linecount = 0

    case = 1


    with open(pospath, 'rb') as f:
        marker = 0

        line = f.readline()
        print(len(line))
        for i in range(1000): #(int(len(line)/16)):
            if(marker+16  <= len(line)):
                e = struct.unpack('>'+'ffff', line[marker:marker+16]) #4*n
                #print(e)
                marker = marker+ 16
                #print(marker)
                chararr = list(e)
                bigarr.append(chararr)

            else:
                newline = f.readline()
                
                bytestring = line[marker:len(line)]+newline[0:16-(len(line)-marker)]
                print(len(bytestring))
                
                #if(len(bytestring<16)):
                 #   nextline = f.readline()
                  #  marker = 16 - len(bytestring)
                   # bytestring = bytestring + nextline[0:marker] 
                    #case = 2

                e = struct.unpack('>'+'ffff', bytestring)
                #print(e)
                marker = 16-(len(line)-marker)
                #print(marker)
                if (case == 1):
                    line = newline
                #if (case == 2):
                 #   line = nextline
                  #  case = 1
                chararr = list(e)
                bigarr.append(chararr)

                
                
        
    pd.DataFrame(bigarr).to_csv(input("What file would you like to generate for your CSV? Include .csv extension: "))

                




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

csvbuildcount("data\R41_03111-v01\R41_03111-v01.pos")
exit(0)