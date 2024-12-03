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

    # delete this break after the program is done.
    break