import random

def draw_card() -> int:
    """draw card from deck"""
    cards: list = [
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10
    ]
    return random.choice(cards)


def deck_sum(input_deck: list) -> int:
    """calculates total the deck"""
    total = 0  # var to store sum total of deck.
    for i in input_deck:
        total += i  # adding ith item.
    return total


def display_of_deck(the_deck: list) -> None:
    display_str: str = ""
    display_str += "-- ["
    for i in range(len(the_deck)):
        display_str += str(the_deck[i])
        # adding comma
        if i != len(the_deck) - 1:
            display_str += ", "
    display_str += f"] with {deck_sum(the_deck)} Points"
    print(display_str)


# these are all the cards in the game.
PARENT_CARDS_DECK = [
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10
]

# var to run game.
game_onn: bool = True

# loop to run the game.
while game_onn:
    print("==================================================================")
    print("------------------- WELCOME TO BLACKJACK GAME --------------------")
    print("==================================================================\n")

    #  taking player name.
    print("=======================================================")
    print("-- YOUR NAME MUST HAVE MORE THAN 2 ALPHABETICAL CHAR --")
    player_name: str = ""  # stores name of player.
    while len(player_name) < 2 or not player_name.isalpha():
        player_name = input("-- Please Enter name :>> ")
    print("=======================================================\n")

    # taking amount from player.
    print("=======================================================")
    print("-- MINIMUM DEPOSIT MUST BE $1000 ----------------------")
    player_deposit: int = 0  # store total deposit from player.
    while player_deposit < 1000 or player_deposit > 10000:
        player_deposit = int(input(f"-- {player_name.upper()}, deposit your amount :>> $"))
    print("======================================================\n")

    # player command to bid.
    continue_bidding: bool = True
    while continue_bidding or player_deposit > 19:
        print("=======================================================")
        print(f"-- place your bet ------------------------------------")
        print(f"-- {player_name.upper()} you have ${player_deposit}")
        player_bid: int = 0  # to hold the bid of the player.
        while player_bid < 20 or player_bid > player_deposit:
            player_bid = int(input(f"-- Min bid amount $20 :>> $"))
        player_deposit -= player_bid
        print("=======================================================\n\n")

        # system and player deck
        PLAYER_DECK: list = []
        SYSTEM_DECK: list = []

        # system and player points var
        player_points: int = deck_sum(PLAYER_DECK)
        system_points: int = deck_sum(SYSTEM_DECK)

        # loop to create initial deck
        for _ in range(2):
            # player initialization
            player_draw: int = draw_card()
            PLAYER_DECK.append(11 if player_draw == 1 and player_points < 10 else player_draw)
            player_points = deck_sum(PLAYER_DECK)
            # system initialization
            system_draw: int = draw_card()
            SYSTEM_DECK.append(11 if system_draw == 1 and system_points < 10 else system_draw)
            system_points = deck_sum(SYSTEM_DECK)

        # showing cards for player.
        print("=======================================================")
        print(f"-- {player_name} has [{PLAYER_DECK[0]}, {PLAYER_DECK[1]}] dealer has [{SYSTEM_DECK[0]}, #]")

        # asking player to draw again.
        while input(f"-- {player_name.upper()} press 'd' to draw :>> ") == 'd':
            player_draw: int = draw_card()
            PLAYER_DECK.append(11 if player_draw == 1 and player_points < 10 else player_draw)
            player_points = deck_sum(PLAYER_DECK)
            print("-- you have -------------------------------------")
            display_of_deck(PLAYER_DECK)
            # break if points are higher than 21
            if player_points >= 21:
                break

        # making system draw cards
        if player_points > system_points and  system_points <= 17:
            for _ in range(13):
                print("system draw is running")
                system_draw: int = draw_card()
                SYSTEM_DECK.append(11 if system_draw == 1 and system_points < 10 else system_draw)
                system_points = deck_sum(SYSTEM_DECK)
                # break if loop is success
                if system_points > player_points or system_points >= 21:
                    break

        # final display
        print("\n\n\n")
        print(f"-- player '{player_name.upper()}' has ------------------------------------")
        display_of_deck(PLAYER_DECK)
        print("\n")
        print("-- DEALER has ----------------------------------------------------------")
        display_of_deck(SYSTEM_DECK)
        # checking for winner
        if player_points > 21:
            pass
        ### MAKE SURE IF YOU WANT TO BID AGAIN.
    # delete this break after the program is done.
    break
