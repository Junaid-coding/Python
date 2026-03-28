test_dict = {'a': 1, 'b': 2, 'c': 1, 'd': 3, 'e': 1}
print("The original dictionary is: " +str(test_dict))
target_value = 1
res = 0
for key in test_dict:
    if test_dict[key] == target_value:
        res += 1
print("Frequncy of target value is: " +str(res))