try:
    number = int(input("Enter a number: "))
    print("The number enetered is", number)
except ValueError as ex:
    print("Exception:", ex)