actual_cost =  float(input("Enter actual product price: "))
sell_amount =  float(input("Enter the sales amount: "))

if(sell_amount > actual_cost) :
    amount = sell_amount - actual_cost

    print ("Total profit = {0}".format(amount))
else:
     print("No profit")    
 