amount = int(input("Enter amount of withdrawal:"))
note1 = amount//100
note2 = (amount%100)//50
note3 = ((amount%100)%50)//10
print("number of 100 rupee notes is", note1)
print("number of 50 rupee notes is", note2)
print("number of 10 rupee notes is", note3)