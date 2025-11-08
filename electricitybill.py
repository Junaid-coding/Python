units = int(input("Enter how many units of electricity you have used: "))
if units <= 50:
    per_unit = units*2.60
    surcharge = 25
elif units <= 100:
    per_unit = units*3.25
    surcharge = 35
elif units <= 200:
    per_unit = units*5.26
    surcharge = 45
else:
    per_unit = units*8.45
    surcharge = 75
total = per_unit + surcharge
print("Your total cost is = %.2f" %total)
