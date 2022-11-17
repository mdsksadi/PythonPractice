'''
Logical Operators:
    1. and
    2. or
    3. not
'''

number1 = float(input("Enter your first number: "))
number2 = float(input("Enter your second number: "))
number3 = float(input("Enter your third number: "))

if number1>number2 and number1>number3:
    print(number1)
elif number3>number1 and number3>number2:
    print(number3)
else:
    print(number2)


#Program for determine vowel and consonent:

letter = input("Enter your letter: ")[0]    #Because of [0] input will consider first letter if I type a string.

if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u' or letter == 'A' or letter == 'E' or letter == 'I' or letter == 'O' or letter == 'U':
    print("Vowel")
else:
    print("Consonent")
    