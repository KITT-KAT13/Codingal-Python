print("Enter marks obtained in 3 subjects")
math = int(input("math :"))
english = int(input("english :"))
science = int(input("science :"))

sum = math+english+science

print("total sum :", sum)

perc = (sum/300)*100

print(end="percentage Marks =")
print(perc)