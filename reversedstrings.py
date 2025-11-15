string = input("Enter a word or a string: ")
string2 = ( '' )
for i in string:
    string2 = i + string2
print("\nOriginal string is: ", string)
print("\nReversed string is: ", string2)