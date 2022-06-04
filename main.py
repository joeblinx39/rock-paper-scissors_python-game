import random

while True:
    choices=["R","P","S"]
    
    computer=random.choice(choices)
    player = input("R: rock, P: paper, or S: scissors?:")
    
    while player not in choices:
        print("That is not a valid input!, Please enter correct option")
        player = input("R: rock, P: paper, or S: scissors?:")
         
        
    if player==computer:
        print("computer:",computer)
        print("player: ",player)
        print("Tie")
        
    elif player == "R":
        if computer == "P":
           print("computer:",computer)
           print("player: ",player)
           print("You lose!")
        if computer == "S":
           print("computer:",computer)
           print("player: ",player)
           print("You win!")
           
    elif player == "S":
        if computer == "R":
           print("computer:",computer)
           print("player: ",player)
           print("You lose!")
        if computer == "P":
           print("computer:",computer)
           print("player: ",player)
           print("You win!")
           
    elif player == "P":
        if computer == "S":
           print("computer:",computer)
           print("player: ",player)
           print("You lose!")
        if computer == "R":
           print("computer:",computer)
           print("player: ",player)
           print("You win!")
    play_again =input("Play again? (Y/n):")
    
    if play_again != "Y":
        break
print("Bye")
