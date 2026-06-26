import random   # it is a library that generates a random value between a range

number=random.randint(1,100)  #randint gives random integer value from 1 to 100 here 
count=0
attempts=5

while count<attempts:  #this code runs until user does not won  (while true means runs until condition becomes true) 
 count+=1

 user=int(input("enter your number:"))  # user is written inside the while loop so that the loop does not run upto infinite times here the user can give value again and again by running it only one time
 
 if user==number:
  print("You won MAN!!")
  print(f"You took {count} to win")
  break

 elif user<number:  #giving hint tot the user that his value is low than the number 
  print(f"Too Low, Guess high")

 elif user>number:
  print("Too high value guess lower value")
else:
    print("Game Over! You used all 5 chances.")



#______________________________________________________________________________________________



import random

number = random.randint(1,100) #45

count = 0
while count>0: #Infinite Loop
    count += 1
    user   = int(input('Enter your number: ')) #45
    
    if user == number: #user == number, 45 == 45
        print('You won Man..')
        print(f"You took {count} to win!")
        break

    elif user < number: #21<45
        print("Too low , Guess high")

    elif user > number:
        print('Too high value guess lower value')



