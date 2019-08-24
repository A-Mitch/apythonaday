# This program converts a given decimal number into base 10
# I also updated to Python 3 Haha
import sys


# Input a number and the base thar I want to convert it to
btennum = int(sys.argv[1])
resultbase = int(sys.argv[2])

if resultbase > 10:
    print("This is only for things below base 10 :)")
    exit()

# This tells the user what Base 10 number and reuslt base they entered. This is also the test for the sys args.
print("Base 10: "+str(btennum)+" and Desired Base:  "+str(resultbase))

# Divide the base 10 number by the desired base
# The remainder is the rightmost number

resultarr = []

while btennum:
    rem = btennum%resultbase
    resultarr.append(rem)
    btennum = btennum/resultbase

if resultbase == 10:
    print(resultarr[::-1])
else:
    print(resultarr)
    
