########################################
#             MD Shekh Sadi            #
#        sadiewu12345@gmail.com        #
########################################

#Take list input from user:

import math

numbers = input("Enter your numbers with spaces: ")

fNumbers1 = numbers.split()

print("Input from user as char: ",fNumbers1)

print("Input from user: ")
for x in range(len(fNumbers1)):
    
    fNumbers1[x]=int(fNumbers1[x])
    
    print(fNumbers1[x],"\n")

fNumbers2 = numbers.split()
sum = 0
for y in fNumbers2:
    sum = sum+int(y)
print("The sum is: ",sum)

digit = 0
letter = 0
word = 0

inp= input("Enter your text: ")

#Number of letter:

for p1 in inp:
    if p1==" ":
        continue
    letter=letter+1
print("Total letter: ",letter)

#Number of word:

for p2 in inp:
    if p2==" ":
        word=word+1
print("Total word: ",word+1)

#Number of digit:

for p3 in inp:
    if p3>='0' and p3<='9':
        digit=digit+1
    else:
        continue
print("Total digit: ",digit)