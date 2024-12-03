import random


def draw_card() -> int :
    """draw card from deck"""
    cards : list = [
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10
    ]
    return random.choice(cards)


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