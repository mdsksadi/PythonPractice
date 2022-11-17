'''
List is an object of python where I can store my data.
Index 0 to n
'''

subjects = ["C","C++","Java","Python","ros2","CMake","Linux"]   #All kind of data can be store here.

print(subjects) #Print all the value of list
#print 1st value of our silt
print(subjects[0])
#print 5th value of list
print(subjects[4])
#print 3rd to last value of list
print(subjects[2:])
#print 1st value from inverse side of list
print(subjects[-1])
#print 1st 3 value of the list
print(subjects[:3])

'''
"in" and "not in" operator
'''

print("Python" in subjects) #It will show True
print("Math" in subjects)   #It will show False
print("Math" not in subjects)   #It will show True

#Adding value with list

subjects=subjects+["HTML"]
print(subjects)     #print(subjects+["HTML"])   It will do samek task

#print multiple time

print(subjects*3)

#Some functions for "list"

#To find out the length
print(len(subjects)) 
#To add any value
subjects.append("CSS")      #no need to use any extra variable
print(subjects)

#To incert any value
subjects.insert(2,"OS")     #Here 2 is the index number. So for insert we need an index number and a value/item.
print(subjects)

#To remove any value
subjects.remove("CSS")      #It removes required value
print(subjects)     

#To sorting any list
number = [12,54,21,31,2,1,5]
number.sort()       #Small to larger value
print(number)

#To revese any list
number.reverse()        #large to smaller value
print(number)

#To pop 1 value
number.pop()    #It will remove the last value of the list
print(number)

#To copy list item
number2=number.copy()   #It copies all the value of number to number2

#To identify the position
pos=number.index(5)     #We need a variable to keep the position of the value
print(pos)

#To count the repeatation
cnt=number.count(5)     #We need a variable to keep the repeatation number of the required value/item.
print(cnt)

#To clear the whole list
number.clear()  #It removes all the value of the list. So, now we have just the list but no item inside the list. 
print(number)
