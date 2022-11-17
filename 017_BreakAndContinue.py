#Break:

i=0

while i<=5:
    
    if i==2:
        break
    print(i)
    i=i+1

j=0

while j<=5:
    
    j=j+1       #this command must be before continue. Otherwise it will not work. Maybe IDE issue
    if j==2:
        continue
    print(j)