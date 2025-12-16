try:
    num1, num2 = eval(input("Enter a number seperated by a comma:"))
    result = num1 / num2
    print("Result is: ", result)

except ZeroDivisionError:
  print("Division by zero is undefined. ")

except SyntaxError:
   print("Coma is missing, enter the numbers separated by coma like this: 1.2")

except:
   print("Wrong input")
else:
    print("No exceptions")

finally:
      print("This will execute no matter what.")