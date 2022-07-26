#!/venv/bin python3

"""
driver.py: does stuff
"""

__author__ = "Max Hariri-Turner"
__email__ = "maxkht8@gmail.com"

name_to_value = {"ace": 11, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9,
                 "ten": 10, "jack": 10, "queen": 10, "king": 10}
suits = {"hearts": 0, "clubs": 1, "diamonds": 2, "spades": 3}


def main():
    seen_cards = []
    query = input("Card exposed: ")
    while query != "q":
        if query != "my turn":
            card = parse_card(query)
            if card not in seen_cards:
                seen_cards.append(card)
            else:
                print("this is a repeat card poggers")
        else:
            deck = []
            for name in name_to_value.keys():
                for suit in suits:
                    construct = f"{name} of {suit}"
                    deck.append(parse_card(construct))
            for card in seen_cards:
                deck.remove(card)
            stats_counter = [[0 for i in range(4)] for j in range(2)]
            cards_left = 0
            for card in deck:
                stats_counter[0][suits[card[1]]] += name_to_value[card[0]]
                stats_counter[1][suits[card[1]]] += 1
                cards_left += 1
            print(stats_counter)
            for suit in suits:
                print(f"Average {suit[0:-1]} value on draw: {stats_counter[0][suits[suit]] / cards_left}")
                print(f"  average in suit on draw: {stats_counter[0][suits[suit]] / stats_counter[1][suits[suit]]}")
        print(seen_cards)
        query = input("Card exposed/\"my turn\": ")


def parse_card(line):
    # Format must be of the type "count of suit", e.g. "king of hearts"
    parts = line.split(" of ")
    if len(parts) != 2:
        print("ERROR: unexpected card parse input")
    if parts[0] not in name_to_value.keys():
        print("ERROR: card name not recognized")
    if parts[1] not in suits.keys():
        print("ERROR: suit not recognized")
    card = (parts[0], parts[1])
    return card


if __name__ == "__main__":
    main()
