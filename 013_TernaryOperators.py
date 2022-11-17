'''
Find out the leargest number in between tow numbers.
'''

number1 = float(input("Enter your first number: "))
number2 = float(input("Enter your second number: "))

'''
if number1>number2:
    print(number1)
else:
    print(number2)
'''


#Using ternary operator: 

print(number1 if number1>number2 else number2)  #It is super simple to do.
print("Maximum= ",number1 if number1>number2 else number2)  #We can also do like this

maximum = number1 if number1>number2 else number2   #we can also use variable.
print("Maximum= ",maximum)
