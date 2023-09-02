# import the json module from python3
import json
import random 

# function to open and read given file path
def getcards(filepath):
    with open(filepath, 'r') as f:
        data = json.load(f)
    return data

# setting variables
total = 0
score = 0
multiplechoice = False

# making userscore function to keep code dry, using f string
def userscore():
     print(f"Your score is {score}/{total}.")

# making quiz function to ask user flashcard question and check answer
def quiz(q,a):
    guess = input(q + " > ")
    if guess.lower() == a.lower(): 
        print("Correct!")
        return True
    else:
        print(f"Incorrect. The correct answer is {a}")

def mquiz(q,a,one,two,three):
    options = [one,two,three]
    random.shuffle(options)
    print(q)
    for opts in options:
        print(opts)
    guess = input("Enter the symbol in front of the answer you wish to select > ")
    if guess == a: 
        print("Correct!")
        return True
    else:
        print(f"Incorrect. The correct answer is {a}")

# making an endscore function to display different messgages based on score
def endscore(finscore,fintotal):
    if finscore == fintotal:
        print("A perfect score!")
    elif finscore >= fintotal/2:
        print("Very good!")
    elif finscore == 0:
        print("Oof.")
    else:
        print("Try again! Practice makes perfect.")

# function for endgame message
def endgame():
    print("Thanks for playing!")
    userscore()
    endscore(score,total)
    print(f"Your high score is {highscore}")
    while True:
        print("Would you like to:")
        print("1. Review these again")
        print("2. Try another flash card deck?")
        print("3. Exit.")
        endchoice = input("> ")
        if endchoice == "1":
            return 1
        elif endchoice == "2":
            return 2
        elif endchoice == "3":
            return 3
        else:
            print("Invalid selection. Please try again. Choose 1, 2, or 3.")

def build_a_deck():
    while True:
        print("Please note this cannot be used to make multiple choice decks. Yet.")
        topic = input("What is your quiz about? >")
        topic = topic.replace(" ","-")
        if topic == 'about-riley' or topic == 'dnd-trivia' or topic == 'me-capitals':
            print("That name is already taken")
        else:
            customcards = []
            qcont = ""
            while True:
                customq = input("Please enter a question > ")
                customa = input("Please enter the answer > ")
                customcards.append({"q":customq, "a":customa})
                print("Would you like to add another question?")
                print("Y/N")
                qcont = input("> ")
                if qcont == "n" or qcont == "N":
                    deckdict = {"cards":customcards}
                    with open(f"{topic}.json",'w') as outfile:
                        json.dump(deckdict,outfile)
                    return f"{topic}.json"




# deck choice while loop
def startup():
    print("Hi there! Here's our list of Flash Card decks:")
    while True:
        print("1. Middle Eastern Capitals \n 2. Dungeons & Dragons Trivia \n 3. About Riley \n 4. Make your own!")
        choice = input("Which number would you like to access? > ")
        if choice == "1": 
            return "me-capitals.json"
        elif choice == "2":
            return "dnd-trivia.json"
        elif choice == "3":
            return "about-riley.json"
        elif choice =="4":
            return build_a_deck()
        else:
            print("Invalid selection. Please try again. Choose 1, 2, 3, or 4.")

# Where the actual magic happens ---- 
# calling startup to get the file name for getcards function
deckchoice = startup()
deck = getcards(deckchoice)
random.shuffle(deck)

if deckchoice == "about-riley.json" or deckchoice == "dnd-trivia.json":
    multiplechoice = True

# deck = getcards(startup())

# setting up total
total = len(deck["cards"])

# for loop to run all the questions, +1 to score if correct, and post score
next = 0 
highscore = 0
while next!=3:
    score = 0
    print("Let's test your knowledge!")
    for i in deck["cards"]:
        if multiplechoice == False:
            if quiz(i["q"],i["a"]) == True:
                score += 1 
        else:
            if mquiz(i["q"],i["a"],i["opt1"],i["opt2"],i["opt3"]) == True:
                score += 1
        userscore()
    highscore = max(highscore,score)
    next = endgame() 
    if next == 2:
        highscore = 0
        deckchoice = startup()
        deck = getcards(deckchoice)
        total = len(deck["cards"])
        random.shuffle(deck)
        if deckchoice == "about-riley.json" or deckchoice == "dnd-trivia.json":
            multiplechoice = True
        else:
            multiplechoice = False
    
print("Thanks for playing! Goodbye.")