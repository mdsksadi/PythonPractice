number = int(input("Enter your number: "))

result = 1

for x in range(1,number+1):
    result=result*x

print("The factorial of",number,"is:",result)