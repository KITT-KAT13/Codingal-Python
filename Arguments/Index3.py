def factorial(x):
    '''This is a recursive function to find the fuctorial of an integer'''
    if x==0 or x==1:
        return 1
    else:
        return x*factorial(x-1)
    
print(factorial.__doc__)
print("The factorial of 0: ", factorial(0)) 
print("The factorial of 0: ", factorial(1))    
print("The factorial of 0: ", factorial(2))    
print("The factorial of 0: ", factorial(3))    
print("The factorial of 0: ", factorial(4))    
print("The factorial of 0: ", factorial(5))    
print("The factorial of 0: ", factorial(6))    
print("The factorial of 0: ", factorial(7))    
print("The factorial of 0: ", factorial(8))    
print("The factorial of 0: ", factorial(9))    
print("The factorial of 0: ", factorial(10))       