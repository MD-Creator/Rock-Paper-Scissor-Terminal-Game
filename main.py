import random
import sys
global player_choice

def convert_to_name(letter):
    if letter == "s":
        return "scissor"
    elif letter == "r":
        return "rock"
    elif letter == "p":
        return "paper"
    else:
        return None

def getName(message):
    name = input(message)
    return name

def welcome(name):
    print("Hey ", name, " Welcome to rock paper scissor")

def GameWin(comp_choice, player_choice):
    if comp_choice == player_choice:
        return None
    elif comp_choice == "r":
        if player_choice == "s":
            return False
        elif player_choice == "p":
            return True
    elif comp_choice == "p":
        if player_choice == "r":
            return False
        elif player_choice == "s":
            return True
    elif comp_choice == "s":
        if player_choice == "p":
            return False
        elif player_choice == "r":
            return True

def check_player_choice(name):
    player_choice = input(f"{name}'s turn: Rock(r), Paper(p) and scissor(s) -> ",)
    if player_choice == "r":
        return player_choice
    elif player_choice == "p":
        return player_choice
    elif player_choice == "s":
        return player_choice
    else:
        output = check_player_choice(name)
        return output

def r_p_s_game(name):
    print("Computer's turn:")
    random_num = random.randint(1,3)
    if random_num == 1:
        comp_choice = "r"
    elif random_num == 2:
        comp_choice = "p"
    else:
        comp_choice = "s"
    player_choice = check_player_choice(name)
    status = GameWin(comp_choice,player_choice)
    comp_choice = convert_to_name(comp_choice)
    player_choice = convert_to_name(player_choice)
    print(f"Computer's choice is {comp_choice} and your choice is {player_choice}")
    if status == None:
        print("This Game Is Tie! :|")
    elif status:
        print("You Won the Game! :)")
    else:
        print("You Lose :(")

def check_to_start():


    input_of_user = int(input("Type '1' to start and '0' to exit the game: "))
    if input_of_user == 1:
        return 1
    elif input_of_user == 0:
        return 0
    else:
        output = check_to_start()
        return output

def startGame():
    r_p_s_game(name)
    check_results = check_to_retry()
    do_after_retry_check(check_results)

def check_to_retry():
    global retry_input
    retry_input = input("Type '1' if you want to play again or '0' to exit: ")
    if retry_input == "1":
        retry_input = int(retry_input)
        return retry_input
    elif retry_input == "0":
        retry_input = int(retry_input)
        return retry_input
    else:
        output = check_to_retry()
        return output

def do_after_retry_check(check_results):
    if check_results == 1:
        startGame()
    else:
        sys.exit()
    

name = getName("Enter Your name: ")
welcome(name)
to_start_or_not  = check_to_start()
if to_start_or_not == 1:
    startGame()
else:
    sys.exit()
