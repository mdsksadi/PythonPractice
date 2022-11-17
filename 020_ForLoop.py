num1=[10,20,30,40,50]
print(num1)

print("Using while loop: ")
i=0
length=len(num1)
while i<length:
    print(num1[i])
    i=i+1

#Using for loop:

print("Using for loop: ")

for x in num1:  #here x is a variable and num1 is our list. num1 theke ekta ekta kore value x variable er moddhe rakhtese.
    print(x)

#Add all our value of list:

s=0
for y in num1:
    s=s+y
print(s)