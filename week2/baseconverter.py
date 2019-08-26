# This program converts a given decimal number (Base-10) into any base that you want
# Done in Python 3
# This program was created by Alexander Mitchell

import sys

# Input a number (argv[1]) and the base that I want to convert it to (argv[2])
btennum = int(sys.argv[1])
resultbase = int(sys.argv[2])

if resultbase > 10:
    print("This is only to convert to base 10 and below :)")
    exit()

# This tells the user what Base 10 number and reuslt base they entered. This is also the test for the sys args.
print("Base 10: "+str(btennum)+" and Desired Base:  "+str(resultbase))

# List for the result 
resultarr = []

# How does the program work
# 1. Take the B-10 number and modulo it with the result base
# 2. Take that remainder and append it to the list
# 3. The new B-10 number will be the the current B-10 number divided by the result base
# 4. Once the B-10 number reaches zero it will exit the program because 0 == false and 1 == true
# 5. The list is converted to a string so that we get a clean representation of the result base number
# 6. If the number is result base is 10 then the original number be the output

while btennum:
    rem = btennum%resultbase
    resultarr.append(rem)
    btennum = btennum/resultbase

# This converts the result array to a string.
stringconv = ''.join(map(str,resultarr))

# I had to reverse the string for result B-10 operations, but the other bases were fine
if resultbase == 10:
    print(stringconv[::-1])
else:
    print(stringconv)
    
