import random

options = ["Rock", "Paper", "Scissors"]

computer = random.choice(options)
player = False

print("Rock, Paper, Scissors, Shoot!")

while player == False:

    player = input("Rock, Paper, or Scissors? ")

    if player == computer:
        print("You Tie!")
    elif player == "Rock":
        if computer == "Paper":
            print("You lose! " + computer + " covers " + player)
        else:
            print("You win! " + player + " smashes " + computer)
    elif player == "Paper":
        if computer == "Rock":
            print("You win! " + player + " covers " + computer)
        else:
            print("You lose! " + computer + " cuts " + player)
    elif player == "Scissors":
        if computer == "Paper":
            print("You win! " + player + " cuts " + computer)
        else:
            print("You lose! " + computer + " smashes " + player)
    elif player == "Quit":
        print('Game Over')
        break
    else:
        print('Not a valid play')

    player = False
    computer = random.choice(options)