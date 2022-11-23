#Program for: 1x2x3x........xn
#Program for: 2x4x6x........xn
#Program for: 1x3x5x........xn
#Program for: 4x8x12x.......xn

i1=int(input("Enter the first value of the series: "))
j1=int(input("Enter the last value of the series: "))
k1=int(input("Enter the interval: "))

series1=list(range(i1,j1+1,k1))

mult1=1
for x1 in series1:
    mult1=mult1*x1
    print(x1)
print("Multiply",mult1)

#Program for: 1²x2²x3²x......xn²
#Program for: 2²x4²x6²x......xn²
#Program for: 1²x3²x5²+......xn²

i2=int(input("Enter the first value of the series: "))
j2=int(input("Enter the last value of the series: "))
k2=int(input("Enter the interval: "))

series2=list(range(i2,j2+1,k2))

mult2=1
for x2 in series2:
    mult2=mult2*x2*x2
    print(x2**2)
print("Multiply",mult2)

#Program for: 1³x2³x3³x......xn³
#Program for: 2³x4³x6³x......xn³
#Program for: 1³x3³x5³x......xn³

i3=int(input("Enter the first value of the series: "))
j3=int(input("Enter the last value of the series: "))
k3=int(input("Enter the interval: "))

series3=list(range(i3,j3+1,k3))

mult3=1
for x3 in series3:
    mult3=mult3*x3*x3*x3
    print(x3**3)
print("Multiply",mult3)

#Program for: 1 x 1/2 x 1/3 x......x1/n

i4=int(input("Enter the first value of the series: "))
j4=int(input("Enter the last value of the series: "))
k4=int(input("Enter the interval: "))

series4=list(range(i4,j4+1,k4))

mult4=1
for x4 in series4:
    mult4=mult4*(1/x4)
    print(1/x4)
print("Multiply",mult4)