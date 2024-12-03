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
    #player name.
    player_name : str = ""
    print("=======================================================")
    while len(player_name) < 2 or not player_name.isalpha():
        player_name = input("-- Enter your name :>> ")
    print("=======================================================")

    # taking total deposit from player.
    print("=======================================================\n")
    print("-- HERE MINIMUM DEPOSIT IS $1000 ----------------------")
    player_total_amount : int = 0 # amount entered by player.
    while player_total_amount < 1000 or player_total_amount > 10000:
        player_total_amount = int(input (f"-- {player_name} please deposit amount :>> "))
    print("=======================================================")

    # player & system details
    player_cards : list = [] # holds all cards of player
    Player_points : int = 0 # score of player.
    system_cards : list = [] # holds all cards of system.
    system_points : int = 0 # score of system.

    # loop to create initial deck
    # delete this break after the program is done.
    break