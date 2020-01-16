# -*- coding: utf-8 -*-

zCount=0
bits=8
upperLimit=2**bits

for i in range(0,upperLimit):
    myBin=bin(i)[2:].zfill(bits)
    print(i,myBin)
    if (myBin.count('0') > myBin.count('1')):
        zCount=zCount+1

#while (i<upperLimit):
#    myBin=bin(i)[2:].zfill(12)
#    print(i,myBin)
#    if (myBin.count('0') > myBin.count('1')):
#        zCount=zCount+1
#    i=i+1

#print("More zeroes than ones: " , "%.5e" %zCount)
print("\nMore zeroes than ones: " , zCount)