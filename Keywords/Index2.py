start = int(input("Enter the start number: "))
end = int(input("Enter the end number: "))

for number in range(start, end +1):
    if number % 20 == 0:
        print("twist")
    elif number % 15 == 0:
        pass    
    elif number % 5 == 0:
        print("fizz")
    elif number % 3 == 0:
        print("buzz")
    else: 
        print(number)        