import random

user_prompt = True

while user_prompt:
    name = input("What is your name? ")
    if name.isalpha():
        user_prompt = False
    else:
        print("Please provide your name in alphabetical letters only")


def coin_toss():
    heads_or_tails = random.choice(["heads", "tails"])

    user_guess = input(f"Thanks {name}! Hello and Welcome to the coin toss game. Please guess heads or tails: ").lower()

    if user_guess == heads_or_tails:
        print(f"Congtratulations {name}!. You won it was {heads_or_tails}.")
    else:
        print(f"Sorry {name}, you lost the game :( It was {heads_or_tails}.")


loop_on = True
while loop_on:
    print(coin_toss())
    anotherToss = str(input("Would you like to do another coin toss (y/n)? "))
    if anotherToss.lower() != "y":
        print(f"Thanks for playing {name}, see you next time")
        loop_on = False

