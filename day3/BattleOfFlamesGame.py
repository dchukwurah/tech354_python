import random

# options for choosing character
fighter_option = {
    1: "Charizard",
    2: "Typhlosion",
    3: "Arcanine",
    4: "Rapidash",
    5: "Infernape",
    6: "Blaziken",
    7: "Ninetales"
}


# options for choosing an attack
attack_option = {
    1: "Fire Blast",
    2: "Flamethrower",
    3: "Inferno",
    4: "Overheat"
}


# dice roll method
def roll_dice():
    return random.randint(1, 6)


# method to retrieve names
def get_name():
    retrieved_name = True

    while retrieved_name:
        name = input("What is your name? ")
        if name.isalpha():
            return name
        else:
            retrieved_name = True
            print("Please provide your name in alphabetical letters only")


def select_character():
    print("Select a character:")
    print(fighter_option)
    character_choice = int(
        input("Which Character do you choose (1-7): "))  # input on the choice for a particular character

    while character_choice > 7 or character_choice < 0:
        print(
            f"Sorry player, that is an invalid choice. Please choose a number between 1-7: ")
        character_choice = input("Which Character do you choose (1-7): ")
    return fighter_option[character_choice]


def select_move():
    print("Select a move:")
    print(attack_option)
    move_choice = int(
        input("Which move do you choose (1-4): "))  # input on the choice for a particular move

    while move_choice > 4 or move_choice < 1:
        print(
            f"Sorry player, that is an invalid choice. Please choose a number between 1-4: ")
        move_choice = int(input("Which Character do you choose (1-4): "))
    return attack_option[move_choice]


def cpu_select_move():
    print("Cpu is selecting a move....")
    print(attack_option)
    cpu_move_choice = random.randint(1, 4)  # input on the choice for a particular move
    return attack_option[cpu_move_choice]


def play_game():
    print("Welcome to Battle of Flames!")
    print("Player 1:")
    name = get_name()
    player1 = select_character()
    print(f"Player 1, {name}, selected {player1}")

    opponent = str(input("Choose your opponent (player/CPU): ").lower())
    while opponent != "cpu" and opponent != "player":
        print(
            f"Sorry player, that is an invalid choice. Please type player or cpu.")  # only accepting values
        opponent = str(input("Choose your opponent (player/CPU): ").lower())
    if opponent == "player":
        print("Player 2:")
        name2 = get_name()
        player2 = select_character()
        print(f"Player 2, {name2}, selected {player2}")
    elif opponent == "cpu":
        name2 = "cpu"
        player2 = random.choice(fighter_option)
        print(f"CPU selected {player2}")

    player1_health = 100
    player2_health = 100

    while player1_health > 0 and player2_health > 0:
        print(f"Player 1, {name}")
        move = select_move()
        print(f"{player1} selected {move}")

        damage = (roll_dice() * roll_dice()) + 10
        player2_health -= damage
        print(f"{player1} attacked {player2} and used {move}! The damage was {damage}")
        print(f"{player2}'s health is now {player2_health}")

        if player2_health <= 0:
            print(f"Congratulations {name}!")
            print(f"Player 1 {player1} wins")
            return
        if opponent == "cpu":
            move = cpu_select_move()
            print(f"{player2} selected {move}")
            damage = (roll_dice() * roll_dice()) + 10
            player1_health -= damage
            print(f"{player2} attacked {player1} and used {move}! The damage was {damage}")
            print(f"{player1}'s health is now {player1_health}")
        else:
            print(f"Player 2, {name2}")
            move = select_move()
            print(f"{player2} selected {move}")
            damage = (roll_dice() * roll_dice()) + 10
            player1_health -= damage
            print(f"{player2} attacked {player1} and used {move}! The damage was {damage}")
            print(f"{player1}'s health is now {player1_health}")

        if player1_health <= 0:
            print(f"Congratulations {name2}!")
            print(f"Player 2 {player2} wins")
            return
        elif player1_health > player2_health:
            print(f"{player1} is winning")
        else:
            print(f"{player2} is winning")


play_game()
