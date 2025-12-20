def squareperi(x):
    perimeter = x
    print("Perimeter of the square is",perimeter)
def rectangleperi(l,b):
    perimeter = 2*(l+b)
    return perimeter
def circumference(r):
    c=2*3.14*r
    print("The circumference of the circle is",circumference)
r=int(input("Enter radius of circle: "))
circumference(r)
x=int(input("Enter the lenght of the side of the square: "))
squareperi(x)
l = int(input("Enter the length of the rectangle: "))
b = int(input("Enter the breadth of the rectangle: "))
rectangleperi(l,b)