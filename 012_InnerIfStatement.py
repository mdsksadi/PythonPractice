'''
It is also called nested if satetement
'''
#Rough code:

if 7>3:
    if 7>9:
        print("Hi")
    else:
        print("Hello")

#Finding the largenst value in between 3 numbers.

number1 = float(input("Enter your first number: "))
number2 = float(input("Enter your second number: "))
number3 = float(input("Enter yourt third number: "))

if number1>number2:
    if number1>number3:
        print(number1)
    else:
    	print(number3)
else:
    if number2>number1:
        print(number2)
    else:
        print(number3)