# cli-games/bnc.py

# import the random method from the randint module
from random import randint

# define roles
roles = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]

# Generate a random role using an array
computer = roles[randint(0,2)]

# Rules
pasc = "Scissors cuts Paper"
ropa = "Paper covers Rock"
roli = "Rock crushes Lizard"
lisp = "Lizard poisons Spock"
scsp = "Spock smashes Scissors"
scli = "Scissors decapitates Lizard"
pali = "Lizard eats Paper"
pasp = "Paper disproves Spock"
rosp = "Spock vaporizes Rock"
rosc = "Rock crushes Scissors"


# other
win = "You win!"
lose = "You lose!"
draw = "You tie!"

score = 0

# tie checker
def tie(cpu,user):
    if cpu == user:
        return True
    return False

# outcome function
def outcome(cpu,user):
    answers = cpu + user
    if "Rock" in answers:
        if "Paper" in answers:
            print(ropa)
        elif "Scissors" in answers:
            print(rosc)
        elif "Lizard" in answers:
            print(roli)
        else:
            print(rosp)
    elif "Paper" in answers:
        if "Scissors" in answers:
            print(pasc)
        elif "Lizard" in answers:
            print(pali)
        else:
            print(pasp)
    elif "Scissors" in answers:
        if "Lizard" in answers:
            print(scli)
        else:
            print(scsp)
    else:
        print(lisp)


# win/lose function
def result(cpu,user):
    if cpu == "Rock":
        if user == "Paper" or user == "Spock":
            return True
    elif cpu == "Paper":
        if user == "Scissors" or user == "Lizard":
            return True
    elif cpu == "Scissors":
        if user == "Spock" or user == "Rock":
            return True
    elif cpu == "Lizard":
        if user == "Scissors" or user == "Rock":
            return True
    else: #spock
        if user == "Paper" or user == "Lizard":
            return True
    return False
            
...

player = False

while player == False:
    # Start message
    print("Get ready to play Rock, Paper, Scissors, Lizard, Spock!")
    print("Would you like any instructions? (Yes/No)")
    instructions = input(" > ")
    if instructions == "yes" or instructions == "Yes":
        print("Rock, Paper, Scissors, Lizard, Spock is a variant on Rock, Paper, Scissors")
        print(pasc,ropa,roli,lisp,scsp,scli,pali,pasp,rosp,rosc, sep="\n")
        print("Let's play!")
    else:
        print("Let's play!")
    # Get player input
    player = input("Rock, Paper, Scissors, Lizard, Spock? > ")

    # test
    print(f"Player = {player}, Computer = {computer}")
    # Compare computer and player role
    if tie(computer,player) == True:
        print(draw)
    elif result(computer,player) == True:
        print(win)
        score += 1
        outcome(computer,player)
    else:
        print(lose)
        score -= 1
        outcome(computer,player)
   
    print(f"Your current score is {score}")
    play_again = input("Would you like to play again? (yes/no) > ")
    if play_again == 'yes' or play_again == "Yes":
        player = False
        computer = roles[randint(0,2)]
    else:
        break

"""     if computer == player:
      print("DRAW!")
    elif computer == "Rock": # comp = rock
        if player == "Paper":
            print("You win!", player, "covers", computer)
        elif player == "Spock":
            print("You win!", player, "vaporizes", computer)
        elif player == "Scissors":
           print("You lose!", computer, "crushes", player)
        else: #lizard
           print("You lose!", computer, "crushes", player)
    elif computer == "Paper": # comp = paper
        if player == "Rock":
            print("You lose!", computer, "covers", player)
        elif player == "Spock":
            print("You lose!", player, "is disproved by", computer)
        elif player == "Scissors":
           print("You win!", player, "cuts", computer)
        else: #lizard
           print("You win!", player, "eats", computer)
    elif computer == "Scissors": # comp = scissors
        if player == "Rock":
            print("You win!", player, "crushes", computer)
        elif player == "Spock":
            print("You win!", player, "smashes", computer)
        elif player == "Paper":
           print("You lose!", computer, "cuts", player)
        else: #lizard
           print("You lose!", player, "is decapitated by", computer)
    elif computer == "Lizard": # comp = lizard
        if player == "Rock":
            print("You win!", player, "crushes", computer)
        elif player == "Spock":
            print("You lose!", computer, "poisons", player)
        elif player == "Paper":
           print("You lose!", computer, "eats", player)
        else: # scissors
           print("You win!", computer, "is decapitated by", player)
    elif computer == "Spock": # comp = spock
        if player == "Rock":
            print("You lose!", computer, "vaporizes", player)
        elif player == "Lizard":
            print("You win!", player, "poisons", computer)
        elif player == "Paper":
           print("You win!", player, "disproves", computer)
        else: # scissors
           print("You lose!", computer, "crushes", player) """

