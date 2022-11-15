'''
num1 = input("Enter first number: ")
num2 = input("Enter second number: ")

sum = num1+num2

print(sum)  #It will show wrong answer. Becasue input in python is always string.
'''

num1 = input("Enter first number: ")
num2 = input("Enter second number: ")

sum = int(num1)+int(num2)   #Making integer and then addition.

print("The sum is: ",sum)

num3 = int(input("Enter your first number: "))  #Taking input and at the same time make it integer.
num4 = int(input("Enter your second number: ")) #Taking input and at the same time make it integer.

result = num3-num4

print("The result is: ",result) #It is working perfectly

num5 = float(input("Enter your number: "))  #Taking a float input

print("Your float number is: ",num5)