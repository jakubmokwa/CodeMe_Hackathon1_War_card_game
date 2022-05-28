import random


def deck_init(deck):
    for i in range(11 + 1):
        deck[i] = 4
    return deck


def print_menu():
    print("Menu: ")
    print("P - play")
    print("M - mode")
    print("Q - quit")


def mode_choice(mode):
    while True:
        print("Choose mode:")
        print("S - short (default)")
        print("L - long ")
        action = input()
        action = action.upper()
        match action:
            case 'S':
                mode = 0
                break
            case 'L':
                mode = 1
                break
            case _:
                print("No action selected")
    return mode


def setup_hands(deck, hand):
    while len(hand) < 10:
        deck_list = list(deck)
        tmp_card = random.choice(deck_list)
        if deck[tmp_card] > 0:
            hand.append(tmp_card)
            deck[tmp_card] -= 1
    return deck, hand


def victory_check(pl_wins, pc_wins):
    if pl_wins > pc_wins:
        print(f"You won the game")
        print("Your score: ", pl_wins)
        print("Pc score: ", pc_wins)
    elif pc_wins > pl_wins:
        print("You lost the game")
        print("Your score: ", pl_wins)
        print("Pc score: ", pc_wins)
    else:
        print("Game ended in a draw")
        print("Both you and pc have, ", pl_wins)


def round_check(pl_action, pc_action, pl_wins, pc_wins):
    if pl_action > pc_action:
        print("Your card is bigger, you won this round")
        pl_wins += 1
    elif pc_action > pl_action:
        print("Pc card is bigger, pc won this round")
        pc_wins += 1
    else:
        print("Both cards are the same value, it's a draw")
    return pl_wins, pc_wins


def choice_check(player_hand):
    while True:
        print(player_hand)
        pl_action = int(input("Choose card from your hand ->"))
        if pl_action not in player_hand:
            print("You don't have that card in your hand")
        else:
            break
    return pl_action


def short_game(deck):
    player_hand = list()
    pc_hand = list()
    pl_wins = 0
    pc_wins = 0
    deck, player_hand = setup_hands(deck, player_hand)
    deck, pc_hand = setup_hands(deck, pc_hand)
    for i in range(10):
        pl_action = choice_check(player_hand)
        player_hand.remove(pl_action)
        pc_action = random.choice(pc_hand)
        pc_hand.remove(pc_action)
        print(f"Your choice: {pl_action}")
        print(f"Pc choice: {pc_action}")
        pl_wins, pc_wins = round_check(pl_action, pc_action, pl_wins, pc_wins)
    victory_check(pl_wins, pc_wins)


def long_round_check(pl_action, pc_action, player_hand, pc_hand):
    if pl_action > pc_action:
        player_hand.append(pc_action)
        player_hand.append(pl_action)
        print("Player won this round, both cards added to your hand")
    elif pc_action > pl_action:
        pc_hand.append(pc_action)
        pc_hand.append(pl_action)
        print("Pc won this round, both cards added to its hand")
    else:
        print("It's a draw, both cards are discarded")
    return player_hand, pc_hand


def long_game(deck):
    player_hand = list()
    pc_hand = list()
    pl_wins = 0
    pc_wins = 0
    deck, player_hand = setup_hands(deck, player_hand)
    deck, pc_hand = setup_hands(deck, pc_hand)
    while True:
        if len(pc_hand) == 0:
            print("Player won, pc is out of cards")
            break
        if len(player_hand) == 0:
            print("Pc won, player is our of cards")
            break
        pl_action = choice_check(player_hand)
        player_hand.remove(pl_action)
        pc_action = random.choice(pc_hand)
        pc_hand.remove(pc_action)
        print(f"Your choice: {pl_action}")
        print(f"Pc choice: {pc_action}")
        player_hand, pc_hand = long_round_check(pl_action, pc_action, player_hand, pc_hand)


def menu(deck):
    mode = 0
    while True:
        print_menu()
        action = input()
        action = action.upper()
        match action:
            case 'P':
                if mode:
                    long_game(deck)
                else:
                    short_game(deck)
            case 'M':
                mode = mode_choice(mode)
            case 'Q':
                break
            case _:
                print("No action selected")


def main():
    deck = dict()
    deck = deck_init(deck)
    menu(deck)


main()
