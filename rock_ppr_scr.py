import random

# comp = ["rock", "paper", "scissor"]

comp = random.randint(1,3)

player = int(input("Choose 1.rock 2.paper 3.scissor\n"))

if(comp==1):
    computer = "Rock"
elif(comp==2):
    computer = "Paper"
elif comp == 3:
    computer = "Scissor"
else:
    pass

if(player==1):
    player_val = "Rock"
elif(player==2):
    player_val = "Paper"
elif player == 3:
    player_val = "Scissor"
else:
    pass

print(f"Computer chooses: {computer} You choose: {player_val}")

if(comp==player):
    print("It's a tie!!!!")
elif(comp==1 and player==2):
    print("Paper covers rock ----->")
    print("You win!!!")
elif(comp==1 and player==3):
    print("Rock beats scissor -------->")
    print("Computer wins!!!")
elif(comp==2 and player == 1):
    print("Paper covers rock ----->")
    print("Computer wins")
elif(comp==2 and player ==3):
    print("Scissor cuts paper -------->")
    print("You win!!!!")
elif(comp==3 and player==1):
    print("Rock beats scissor -------->")
    print("You win!!!")
elif(comp==3 and player==2):
    print("Scissor cuts paper -------->")
    print("Computer wins")
else:
    print("Others")