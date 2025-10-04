production_money = float(input("Enter the amount of money you used to produce the product:"))
sales_money = float(input("Enter the amount of money you earned after selling the produce:"))
if (production_money < sales_money):
    amount = sales_money - production_money
    print("Total profit = {0}".format(amount))
else:
    loss = production_money - sales_money
    print("Total loss = {0}".format(loss))