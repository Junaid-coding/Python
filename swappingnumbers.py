a = int(input("Enter your first number (a) :"))
b = int(input("Enter your second number (b) :"))
c = int(input("Enter your third number (c) :"))
print("\nBefore swapping:")
print("a =", a, "b =", b, "c =", c)
a, b, c = b, c, a
print("\nAfter swapping:")
print("a =", a, "b =", b, "c =", c)