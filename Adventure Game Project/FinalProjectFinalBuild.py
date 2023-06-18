import random

# Function to select a character
def character_select():
    print("Character Select:")
    print("1. Ryu")
    print("2. Ken")
    print("3. Guile")
    print("4. Chun-Li")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "5":
        print("Exiting program...")
        exit()

    # Dictionary containing character information
    characters = {
        "1": {"name": "Ryu", "move_command": "Hadouken"},
        "2": {"name": "Ken", "move_command": "Shoryuken"},
        "3": {"name": "Guile", "move_command": "Sonic Boom"},
        "4": {"name": "Chun-Li", "move_command": "Kikouken"}
    }

    if choice in characters:
        character = characters[choice]
        print(f"Selected character: {character['name']}")
        return character
    else:
        print("Invalid choice")
        return None

# Function to execute a command based on the given dialog
def execute_command(dialog, character, move_command, incorrect_choices):
    print(dialog)
    print("Choose one of the following commands:")
    print("1. Scan item")
    print("2. Bag item")
    print("3.", character['name'] + "'s special move:", move_command)

    while True:
        command = input("Enter your command: ")

        if command == "1":
            print("Scanning item...")
            if dialog == "Hey, could you scan this item for me?":
                print("Thanks!")
            else:
                print("That's not what I asked!")
                incorrect_choices.append(command)
        elif command == "2":
            print("Bagging item...")
            if dialog == "Could you bag these items for me?":
                print("Thanks!")
            else:
                print("That's not what I asked!")
                incorrect_choices.append(command)
        elif command == "3":
            print(move_command)
            if dialog == "Open the cash register now!!!":
                print("Forget that, I'm out of here")
            else:
                print("That's cool but what does that have to do with what I asked?")
                incorrect_choices.append(command)
        else:
            print("Invalid command. Try again.")
            incorrect_choices.append(command)

        if len(incorrect_choices) >= 2:
            return False

        if command in ["1", "2", "3"]:
            break

    return True

#Above is the logic for the first section of the game
# Function to start the game with initial customer dialogs
def start_game(character, fail_state):
    customer_dialogs = [
        "Hey, could you scan this item for me?",
        "Could you bag these items for me?",
        "Open the cash register now!!!"
    ]
    random.shuffle(customer_dialogs)

    incorrect_choices = []

    for dialog in customer_dialogs:
        if not execute_command(dialog, character, character["move_command"], incorrect_choices):
            fail_state[0] = True
            return False

    return True

# Function to start section 2
def start_section2(character, fail_state):
    customer_dialogs = [
        "Hey could you answer a quick question for me?",
        "Could you address a concern I have?",
        "Hand over the money if you know what's good for you!!!"
    ]
    random.shuffle(customer_dialogs)

    incorrect_choices = []

    for dialog2 in customer_dialogs:
        if not section_2(dialog2, character, character["move_command"], incorrect_choices):
            fail_state[0] = True
            return False

    return True

# Function to start section 3
def start_section3(character, fail_state):
    customer_dialogs = [
        "The floor is dusty",
        "There's a spill in aisle 5",
        "Hand over the money if you know what's good for you!!!"
    ]
    random.shuffle(customer_dialogs)

    incorrect_choices = []

    for dialog3 in customer_dialogs:
        if not section_3(dialog3, character, character["move_command"], incorrect_choices):
            fail_state[0] = True
            return False

    return True

# Function for section 2
def section_2(dialog2, character, move_command, incorrect_choices):
    print(dialog2)
    print("Choose one of the following commands:")
    print("1. Answer customer's question.")
    print("2. Address customer's concern.")
    print("3.", character['name'] + "'s special move:", move_command)

    while True:
        command = input("Enter your command: ")

        if command == "1":
            print("Yea the answer is...")
            if dialog2 == "Hey could you answer a quick question for me?":
                print("Thanks!")
            else:
                print("That's not what I asked!")
                incorrect_choices.append(command)
        elif command == "2":
            print("Ok, we can rectify this by...")
            if dialog2 == "Could you address a concern I have?":
                print("Thanks!")
            else:
                print("That's not what I asked!")
                incorrect_choices.append(command)
        elif command == "3":
            print(move_command)
            if dialog2 == "Hand over the money if you know what's good for you!!!":
                print("Forget that, I'm out of here")
            else:
                print("That's cool but what does that have to do with what I asked?")
                incorrect_choices.append(command)
        else:
            print("Invalid command. Try again.")
            incorrect_choices.append(command)

        if len(incorrect_choices) >= 2:
            return False

        if command in ["1", "2", "3"]:
            break

    return True

# Function for section 3 of the game
def section_3(dialog3, character, move_command, incorrect_choices):
    print(dialog3)
    print("Choose one of the following commands:")
    print("1. Sweep the floor")
    print("2. Mop the floor")
    print("3.", character['name'] + "'s special move:", move_command)

    while True:
        command = input("Enter your command: ")

        if command == "1":
            print("Sweeping floor...")
            if dialog3 == "The floor is dusty":
                print("Done, now the floor is clean")
            else:
                print("I don't think that's what I should be doing right now.")
                incorrect_choices.append(command)
        elif command == "2":
            print("Time to get the mop...")
            if dialog3 == "There's a spill in aisle 5":
                print("Done, now the floor is clean")
            else:
                print("That's not what I asked!")
                incorrect_choices.append(command)
        elif command == "3":
            print(move_command)
            if dialog3 == "Hand over the money if you know what's good for you!!!":
                print("Forget that, I'm out of here")
            else:
                print("I don't think that's what I should be doing right now.")
                incorrect_choices.append(command)
        else:
            print("Invalid command. Try again.")
            incorrect_choices.append(command)

        if len(incorrect_choices) >= 2:
            return False

        if command in ["1", "2", "3"]:
            break

    return True

# Function to play the rock, paper, scissors game
def play_game(character):
    player_score = 0
    thief_score = 0

    while player_score < 3 and thief_score < 3:
        print("Choose one of the following commands:")
        print("1. Punch")
        print("2. Block")
        print("3. Grab")
        if player_score >= 2:
            print("4.", character['name'] + "'s special move:", character['move_command'])

        player_command = input("Enter your command: ")

        thief_command = random.choice(["1", "2", "3"])

        if player_command == thief_command:
            print("It's a draw!")
        elif (
                (player_command == "1" and thief_command == "3")
                or (player_command == "2" and thief_command == "1")
                or (player_command == "3" and thief_command == "2")
        ):
            print("You win this round!")
            player_score += 1
        elif player_command == "4":
            if player_score >= 2:
                print("Performing", character['name'] + "'s special move:", character['move_command'] + "...")
            else:
                print("Cannot be performed at this moment.")

            player_score += 1
        else:
            print("You lose this round!")
            thief_score += 1

    if player_score == 3:
        print("Thief was defeated. You Win!")
    else:
        print("The thief escaped. Game Over")

# Main game loop
while True:
    character = character_select()
    if character:
        fail_state = [False]
        while True:
            if start_game(character, fail_state):
                start_section2(character, fail_state)
                if fail_state[0]:
                    print("Game Over")
                    break
                start_section3(character, fail_state)
                if fail_state[0]:
                    print("Game Over")
                    break
                play_game(character)
                break
            else:
                print("Game Over")
                break
    else:
        break
