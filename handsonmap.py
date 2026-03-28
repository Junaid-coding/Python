numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]
result = map(lambda x,y: x+y, numbers1, numbers2)
print("Addition of two lists:")
print(list(result))
nus = [1, 2, 3, 4, 5]
def sq(n):
    return n*n
square = list(map(sq, nus))
print("Squares of numbers in the list:")
print(square)