# october 25 2021 snake and ladder
#clyan livingston assignment
#
import random




MAX_VAL = 90

# snake bite move you from high to low
snakes = {
    14: 3,
    20: 15,
    39: 33,
    66: 53,
    69: 58,
    79: 67,
    84: 71,
    88: 36
    
}

# ladder climb move you from low to high
ladders = {
    6: 17,
    24: 26,
    30: 44,
    49: 62,
    82: 86
    
}

player_turn_text = [
    "Please proceed.",
    "",
]

snake_bite = [
    "its sad ",
    "snake bite",
    
]

ladder_jump = [
    "yes go ",
    "massive ",
   
]


def welcome_msg():
    msg = """
    Welcome to Snake and Ladder Game.
    clyan livingston trail run 
    """
    print(msg)


def get_player_names():
    player1_name = None
    while not player1_name:
        player1_name = input("Please enter first player name: ").strip()

    player2_name = None
    while not player2_name:
        player2_name = input("Please enter second player name: ").strip()

    print("\nMatch will be played between '" + player1_name + "' and '" + player2_name + "'\n")
    return player1_name, player2_name


def get_dice_value():
    
    dice_value = random.randint(1, 6)
    print("Its a " + str(dice_value))
    return dice_value


def got_snake_bite(old_value, current_value, player_name):
    print("\n" + random.choice(snake_bite).upper())
    print("\n" + player_name + " got a bite. Down from " + str(old_value) + " to " + str(current_value))


def got_ladder_jump(old_value, current_value, player_name):
    print("\n" + random.choice(ladder_jump).upper())
    print("\n" + player_name + " climbed the ladder from " + str(old_value) + " to " + str(current_value))


def snake_ladder(player_name, current_value, dice_value):
    
    old_value = current_value
    current_value = current_value + dice_value

    if current_value > MAX_VAL:
        print("You need " + str(MAX_VAL - old_value) + " to win continue ")
        return old_value

    print("\n" + player_name + " moved from " + str(old_value) + " to " + str(current_value))
    if current_value in snakes:
        final_value = snakes.get(current_value)
        got_snake_bite(current_value, final_value, player_name)

    elif current_value in ladders:
        final_value = ladders.get(current_value)
        got_ladder_jump(current_value, final_value, player_name)

    else:
        final_value = current_value

    return final_value


def check_win(player_name, position):
    
    if MAX_VAL == position:
        print("\n\n\nThats it.\n\n" + player_name + " won the game.")
        print("Congratulations " + player_name)
        print("\nThank you for playing the game.\n\n")
        


def start():
    welcome_msg()
    
    player1_name, player2_name = get_player_names()
   
    player1_current_position = 0
    player2_current_position = 0

    while True:
        
        input_1 = input("\n" + player1_name + ": " + random.choice(player_turn_text) + " Hit the enter to roll dice: ")
        print("\nMoving dice...")
        dice_value = get_dice_value()
       
        print(player1_name + " moving....")
        player1_current_position = snake_ladder(player1_name, player1_current_position, dice_value)

        check_win(player1_name, player1_current_position)

        input_2 = input("\n" + player2_name + ": " + random.choice(player_turn_text) + " Hit the enter to roll dice: ")
        print("\nMoving dice...")
        dice_value = get_dice_value()
        
        print(player2_name + " moving....")
        player2_current_position = snake_ladder(player2_name, player2_current_position, dice_value)

        check_win(player2_name, player2_current_position)


if __name__ == "__main__":
    start()
