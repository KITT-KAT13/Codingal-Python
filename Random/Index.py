import random
playing = True
number = str(random.randint(10,20))  

print("I will generate a number from 10,20 and you'll have to guess the number one at a time")
print("The game ends when you get 1")

#iterating loop till the

while playing:
      guess = input("Give me your best guess!: ")
      if number == guess:
            print(" You win")
            print("the number was", number )
            break
      else:
             print("Your guess is out of range, try again")