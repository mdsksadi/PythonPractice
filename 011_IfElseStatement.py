'''
Control Statement:
1. Conditional Statement:   if, elif, else
2. Loop Control Statement:  for, while
'''
#if,elif,else statement:

mark1 = 70

if mark1>=33:
    print("Pass")

else:
    print("Fail")   #It is not working because here if works. Else is not working.

mark2 = 20

if mark2>=33:
    print("Pass")   #It is not working because here if works. Else is not working.

else:
    print("Fail")   

#Een Odd finding program:

number = int(input("Enter your number: "))

if number%2==0:
    print("It is an even number.")
else:
    print("It is an odd number.")

#More complex if,elif,else

marks = float(input("Enter your mark: "))

if marks>=80:
    print("A+")
elif marks>=70:     #if the first statement (if), bolow statements will not work.
    print("A")
elif marks>=60:
    print("A-")
elif marks>=50:
    print("B")
elif marks>=40:
    print("C")
elif marks>=30:
    print("D")
else:
    print("F")

'''
We can also write this. But top one is better.
if marks>=80:
    print("A+")
elif marks>=70 and marks<80:    #Here and means and 
    print("A")
elif marks>=60 and marks<70:
    print("A-")
elif marks>=50 and marks<60:
    print("B")
elif marks>=40 and marks<50:
    print("C")
elif marks>=30 and marks<40:
    print("D")
else:
    print("F")
'''