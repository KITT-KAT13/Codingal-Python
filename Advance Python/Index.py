numbers1 = [1, 5, 7, 8, 9, 12, 56, 3]
numbers2 = [3, 45, 23, 4, 56, 2, 45, 3]
result = map(lambda x, y: x + y, numbers1, numbers2)
print("Addition of two lists")
print(list(result))

nums = [8, 3, 6, 9, 2, 4]
def sq(n):
    return n*n
square = list(map(sq,nums))

print("Square of numbers in list")
print(square)