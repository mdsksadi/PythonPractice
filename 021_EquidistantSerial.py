#Program for: 1+2+3+........+n
#Program for: 2+4+6+........+n
#Program for: 1+3+5+........+n
#Program for: 4+8+12+.......+n

i=int(input("Enter the first value of the series: "))
j=int(input("Enter the last value of the series: "))
k=int(input("Enter the interval: "))

series1=list(range(i,j+1,k))

sum1=0
for x in series1:
    sum1=sum1+x
    print(x)
print("Sum",sum1)

#Program for: 1²+2²+3²+......+n²
#Program for: 2²+4²+6²+......+n²
#Program for: 1²+3²+5²+......+n²

p=int(input("Enter the first value of the series: "))
q=int(input("Enter the last value of the series: "))
r=int(input("Enter the interval: "))

sum2=0
series2=list(range(p,(q+1),r))

for y in series2:
    sum2=sum2+(y*y)
    print(y**2)
print("Sum",sum2)

#Program for: 1³+2³+3³+......+n³
#Program for: 2³+4³+6³+......+n³
#Program for: 1³+3³+5³+......+n³

p2=int(input("Enter the first value of the series: "))
q2=int(input("Enter the last value of the series: "))
r2=int(input("Enter the interval: "))

sum3=0
series3=list(range(p2,(q2+1),r2))

for y2 in series3:
    sum3=sum3+(y2*y2*y2)
    print(y2**3)
print("Sum",sum3)

#Program for: 1+ 1/2 + 1/3 +......+1/n

p3=int(input("Enter the first value of the series: "))
q3=int(input("Enter the last value of the series: "))
r3=int(input("Enter the interval: "))

sum4=0
series4=list(range(p3,(q3+1),r3))

for y3 in series4:
    sum4=sum4+(1/y3)
    print(1/y3)
print("Sum",sum4)