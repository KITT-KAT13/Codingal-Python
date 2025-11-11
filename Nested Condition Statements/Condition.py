#Taking inout from students
medical_cause = input("Did you have a medical causes Y OR N:")
attend = int(input("Enter the attendance of the student in percentage: "))

if medical_cause == 'y':
    print("you are allowed.")
else:
    if attend >=75:
        print("Allowed") 
    else:
        print("Not allowed")