import random    

def game():
    print("You are playing the game..")
    score = random.randint(1,62)

    #Fetch the high Score 
    with open("hiScore.txt") as f:
        hiscore = f.read()
        if(hiscore!=""):
            hiscore=int(hiscore)
        else:
            hiscore=0

    print(f"Your Score : {score}")
    if(score>hiscore):
        #write this hiscore to the file 
        with open("hiScore.txt","w") as f:
                f.write(str(score))

    return score

game()