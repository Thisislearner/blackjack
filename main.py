import random


def draw_card() -> int :
    """draw card from deck"""
    cards : list = [
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10
    ]
    return random.choice(cards)


def deck_sum(input_deck : list) -> int:
    """calculates total the deck"""
    total = 0  # var to store sum total of deck.
    for i in input_deck:
        total += i # adding ith item.
    return total


# these are all the cards in the game.
PARENT_CARDS_DECK = [
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10
]

# var to run game.
game_onn : bool = True

# loop to run the game.
while game_onn:
    print("==================================================================")
    print("------------------- WELCOME TO BLACKJACK GAME --------------------")
    print("==================================================================\n")

    #  taking player name.
    print("=======================================================")
    print("-- YOUR NAME MUST HAVE MORE THAN 2 ALPHABETICAL CHAR --")
    player_name : str = "" # stores name of player.
    while len(player_name) < 2 or not player_name.isalpha():
        player_name = input("-- Please Enter name :>> ")
    print("=======================================================\n")

    # taking amount from player.
    print("=======================================================")
    print("-- MINIMUM DEPOSIT MUST BE $1000 ----------------------")
    player_deposit : int = 0  # store total deposit from player.
    while player_deposit < 1000 or player_deposit > 10000:
        player_deposit = int(input(f"{player_name}, Please deposit amount :>> "))
    # delete this break after the program is done.
    break