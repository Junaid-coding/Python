print("Enter your scores for the following subjects-")
math = int(input("Maths:"))
science = int(input("Science:"))
hindi = int(input("Hindi:"))
history = int(input("History:"))
geo = int(input("Geography:"))
sum = math+science+hindi+history+geo
print("Sum of all your scores in each subjects is", sum)
perc = (sum/500)*100
print(end="Percentage of your marks:")
print(perc)