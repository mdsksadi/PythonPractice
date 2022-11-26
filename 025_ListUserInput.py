'''
GCD is Greatest Common Divisor

Formula: 
'''


#Take list input from user:

import math

numbers = input("Enter your numbers with spaces: ")

fNumbers = numbers.split()

for x in range(len(fNumbers)):
    
    fNumbers[x]=int(fNumbers[x])
    
    print(fNumbers[x])