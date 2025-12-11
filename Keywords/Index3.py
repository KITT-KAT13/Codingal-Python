numbers = [1,2,3,4,5,6,7,8,9,0]
for number in reversed(numbers ):
    if number == 5:
        continue   # skip 5
    print(number)