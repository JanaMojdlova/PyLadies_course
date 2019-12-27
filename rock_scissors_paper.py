import random 

def computer_play():
    return random.choice(["rock", "scissors", "paper"])

def is_valid_play(play):
    return play in ["rock", "paper", "scissors"] 

def determine_game_result(player, computer):
    if player == computer:
        return "tie"
    elif (player == "rock" and computer == "paper") or (player == "scissors" and computer == "rock") or (player == "paper" and computer == "scissors") :
        return "computer"
    elif (player == "rock" and computer == "scissors") or (player == "scissors" and computer == "paper") or (player == "paper" and computer == "rock"):
        return "player"


player = None
while not is_valid_play(player):
    player = input('rock, paper or scissors? ')

computer = computer_play()
result = determine_game_result(player, computer)

print("Computer: " + computer)
print("You: " + player)

if result == "tie":
    print("It's a tie!")
elif result == "computer":
    print("Computer won!")
elif result == "player":
    print("You won!")








