import random 

def game():
    run=0
    while True :
        score=random.randint(0,6)
        if score==0:
            print(f"You Are Out at {run} Run")
            break
        else:
            run +=score
    return run

print("....... Welcome To The Cricket Game ......")
Player1=input("Enter 1st Player name : ").upper().strip()
Player1_score=game()
print(f"{Player1} Score {Player1_score} Run")
Player2=input("Enter 2nd Player name : ").upper().strip()
Player2_score=game()
print(f"{Player2} Score {Player2_score} Run")

if Player1_score>Player2_score:
    print(f"{Player1} Won the Game")
elif Player2_score>Player1_score:
    print(f"{Player2} Won the Game ")
else:
    print("Match TIE ")