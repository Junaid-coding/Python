try:
    age = int(input("Enter your age: "))
    print("Your age is correct!")
    if age % 2 == 0:
        print("Your age is an even number")
    else:
        print("Your age is a odd number")
except ValueError:
    print("Type the correct value!")