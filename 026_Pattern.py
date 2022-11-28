########################################
#             MD Shekh Sadi            #
#        sadiewu12345@gmail.com        #
########################################

star = int(input("Enter the number of star: "))
gap = int(input("Enter the gap between each number: "))

a1 = '*'

for x1 in range(1,star+1,gap):
    print(a1*x1)
    x1=x1+1


for x2 in range(1,star+1,gap):
    for x3 in range(1, star+1,gap):
        if (x3 <= star-x2):
            print(" ",end=" ")
        else:
            print("*", end=" ")
    print()
