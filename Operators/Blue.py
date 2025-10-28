#Taking total amount as input fron user
Amount =int(input("Please enter amount to withdraw : "))

#Calculating the amount they need

note_1 = Amount//100
note_2= (Amount%100)//50
note_3 = ((Amount%100)%50)//10

print("Notes of 100: ", note_1)
print("Notes of 50: ", note_2)
print("Notes of 10: ", note_3)