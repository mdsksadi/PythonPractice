name = input("Enter your name: ")
age = input("Enter your age: ")
gpa = input("Enter your gpa: ")
empty = input()
empty2 = input()


print("Student Information")
print("-------------------")
print("Name: "+name)
print("Age: ",age)
print("GPA: ",gpa)

print("The test result is: ",empty)
print("The test result is: "+empty2)

#Python input is from user is always string. We need to convert it integer if we want integer value. We can use int() function for that.

print(type(empty))  
print(type(empty2)) 