n = int(input("Enter a number of rows: "))
for i in range(1, n + 1):
    for j in range(n - 1):
        print(" ", end="")
    for k in range(i):
        print("* ", end="")
    print()