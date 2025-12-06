print("Half pyramid pattern of stars (*): ")
n = int(input("Enter the number of rows you want in the triangle: "))
for i in range(n):
    for j in range(i+1):
        print("* ", end=" ")
    print()