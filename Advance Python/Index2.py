s1 = {2,4,7}
s2 = {'a','b','c'}
s3 = list(zip(s1,s2))

print(s3, "\n")

list = [12, 45, 67, 54, 34, 56]
list2 = [25, 65, 45, 23, 87, 97]

for x, y in zip(list, list2[::-1]):
    print(x,y)

students = ["Abenazer", "Collins", "Jenele"]
results = [87, 89, 64] 

new_dict = {students:results for students, results in zip(students, results)}

print("\n{}".format(new_dict))
