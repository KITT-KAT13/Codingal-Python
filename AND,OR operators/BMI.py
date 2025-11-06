height = float(input("Enter your height in cm: "))
weight = float(input("Enter your weight in kgs: "))

BMI = weight / (height/100)**2

print("your BMI is: ",BMI)

if BMI <= 18.4:
    print("You are underweight. ")
elif BMI <= 24.4:
     print("You are health") 
elif BMI <= 29.9:
     print("You are overweight")      
else:
     print("you are serverely overweight"
           
           )

