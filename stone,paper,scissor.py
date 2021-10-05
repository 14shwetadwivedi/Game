
#
# Stone, Paper, Scissor Game in Python
# The stone breaks the scissor, the scissor cuts the paper, and paper covers the stone.
#

import random

lst = ['st', 'pr', 'sc']

chance = 10
no_of_chance = 0
computer_point = 0
human_point = 0

print("*********Stone,Paper,Scissor Game*********\n")
print("st for stone \npr for paper \nsc for scissor \n")

# making the game in while
while no_of_chance < chance:
    _input = input('Stone,Paper,Scissor:')
    _random = random.choice(lst)

    if _input == _random:
        print("Tie Both 0 point to each \n ")

    # if user enter sc
    elif _input == "sc" and _random == "st":
        computer_point = computer_point + 1
        print(f"your guess {_input} and computer guess is {_random} \n")
        print("computer wins 1 point \n")
        print(f"computer_point is {computer_point} and your point is {human_point} \n ")

    elif _input == "sc" and _random == "pr":
        human_point = human_point + 1
        print(f"your guess {_input} and computer guess is {_random} \n")
        print("Human wins 1 point \n")
        print(f"computer_point is {computer_point} and your point is {human_point} \n")

    # if user enter pr
    elif _input == "pr" and _random == "sc":
        computer_point = computer_point + 1
        print(f"your guess {_input} and computer guess is {_random} \n")
        print("computer wins 1 point \n")
        print(f"computer_point is {computer_point} and your point is {human_point} \n ")

    elif _input == "pr" and _random == "st":
        human_point = human_point + 1
        print(f"your guess {_input} and computer guess is {_random} \n")
        print("Human wins 1 point \n")
        print(f"computer_point is {computer_point} and your point is {human_point} \n")

    # if user enter st

    elif _input == "st" and _random == "sc":
        human_point = human_point + 1
        print(f"your guess {_input} and computer guess is {_random} \n")
        print("Human wins 1 point \n")
        print(f"computer_point is {computer_point} and your point is {human_point} \n")


    elif _input == "st" and _random == "pr":
        computer_point = computer_point + 1
        print(f"your guess {_input} and computer guess is {_random} \n")
        print("computer wins 1 point \n")
        print(f"computer_point is {computer_point} and your point is {human_point} \n ")

    else:
        print("you have input wrong \n")

    no_of_chance = no_of_chance + 1
    print(f"{chance - no_of_chance} is left out of {chance} \n")

print("Game over")

if computer_point == human_point:
    print("Tie")

elif computer_point > human_point:
    print("Computer wins and you loose")

else:
    print("you win and computer loose")

print(f"your point is {human_point} and computer point is {computer_point}")




