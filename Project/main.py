'''
1 for snake
-1 for water 
0 for gun
'''

import random

random_number=random.choice([-1,0,1])
computer = random_number
youstr = input("Enter your choice : ")
youDict = {"s":1 , "w" : -1 , "g" : 0}
reversedict = {1 :"Snake", -1:"Water" , 0 :"Gun"}
you = youDict[youstr]

print(f"Computer choice {reversedict[computer]}")
print(f"Your choice {reversedict[you]}")

if(computer == you):
    print("It's Draw!")
else:
    if(computer == -1 and you==1):
        print("You Win!") 
    elif(computer == -1 and you==0):
        print("You Lose!")

    elif(computer == 1 and you==-1):
        print("You Lose!")
    elif(computer == 1 and you==0):
        print("You Win!")

    elif(computer == 0 and you==-1):
        print("You Win!")
    elif(computer == 0 and you==1):
        print("You Lose!")

    else:
        print("Something went wrong!")







