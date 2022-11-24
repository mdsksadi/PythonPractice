number=int(input("Enter your number: "))

a=2

while a<number:

    if number%a==0:
        primeFlag=False
        break
    else:
        primeFlag=True
    a=a+1


if primeFlag==True:
    print(number,"is a prime number")
else:
    print(number,"is not prime number")