# Taking input of units
Units = int(input("Please enter the number of units you consumed: "))
if(Units < 50):
    amount = Units * 2.60
    surchage = 25
elif(Units <= 100):
    amount = 130 + ((Units - 50) * 3.25)
    surchage = 35
elif(Units <= 200):
    amount = 130 + 162.50 + ((Units - 100)*5.26)  
    surchage = 45
else:
    amount = 130 + 162.50 + 526 +((Units - 200)* 8.45) 
    surchage = 75  

#calculating and display the total Bill

total = amount + surchage           
print("\nElectricy Bill = %.2f" %total)