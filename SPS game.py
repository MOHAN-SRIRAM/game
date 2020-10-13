import random
while True:
    player=input("Select any one STONE,PAPER,SCISSORS :")
    computer=random.choice(["STONE","PAPER","SCISSORS"])

    if player==computer:
        print("Game is TIE!")

    elif player=="STONE":
        if computer=="PAPER":
            print("You LOOSE!\n",computer,'"covers"',player)
        else:
            print("You WIN!\n",player,'"smashes"',computer)
    elif player=="PAPER":
        if computer=="STONE":
            print("You WIN!\n",player,'"covers"',computer)
        else:
            print("You LOOSE!\n",computer,'"cuts"',player)
    elif player=="SCISSORS":
        if computer=="PAPER":
            print("You WIN!\n",player,'"cuts"',computer)
        else:
            print("You LOOSE!\n",computer,'"smashes"',player)
    else:
        print("Check your Spelling!\n\t(OR)\nCheck the case!")
