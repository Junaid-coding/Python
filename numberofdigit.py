num = int(input("Enter your number: "))
count = 0
temp = num
while temp > 0:
    temp //= 10
    count += 1 
print("Total number of digits", count)