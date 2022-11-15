#Area of Triangle:

height_triangle = float(input("Enter the vertical height of our triangle: "))
base_triangle = float(input("Enter the base of our triangle: "))

areaTriangle = 0.5*height_triangle*base_triangle

print("The are of our triangle is: ",areaTriangle)
print("\n\n")

#Area of Rectangle:

height_rectangle = float(input("Enter the height of our rectangle: "))
width_rectangle = float(input("Enter the width of our rectangle: "))

areaRectangle = height_rectangle*width_rectangle

print("The are of our rectangle is: ",areaRectangle)
print("\n\n")

#Area of Trapezoid

length_long_side = float(input("Enter the length of the long side: "))
length_opposit_side = float(input("Enter the length of the opposit side: "))
vertical_height = float(input("Vertical height: "))

areTrapezoid = 0.5*(length_long_side+length_opposit_side)*vertical_height

print("The area of our Trapezoid is: ",areTrapezoid)
print("\n\n")

#Area of Ellipse

distance_a = float(input("Enter distance a: "))
distance_b = float(input("Enter distance b: "))
pi=3.14156

areaEllipse = pi*distance_a*distance_b

print("The area of our Ellipse is: ",areaEllipse)
print("\n\n")

#Area of Square

length_of_side = float(input("Enter the length of side of our square: "))

areaSquare = length_of_side**2

print("The area of our square is: ",areaSquare)
print("\n\n")

#Area of Parallelogram

base_Parallelogram = float(input("Enter the base of our Parallelogram: "))
height_Parallelogram = float(input("Enter the height of our Parallelogram: "))

area_Parallelogram = base_Parallelogram*height_Parallelogram

print("The area of our Parallelogram is: ",area_Parallelogram)
print("\n\n")

#Area of Circle

radious_circle = float(input("Enter the radious of our circle: "))

areaCircle = pi*(radious_circle**2)

print("The area of our circle is: ",areaCircle)
print("\n\n")

#Area of Sector

radious_sector = float(input("Enter the radious of our sector: "))
angle_sector = float(input("Enter the angle in radious is: "))

areaSector = 0.5*(radious_sector**2)*angle_sector

print("The area of our Sector is: ",areaSector)
