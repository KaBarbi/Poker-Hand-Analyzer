from cards import create_deck, card_to_value, remove_known_cards
from hand_ev import evaluate_hand, ONE_PAIR, HIGH_CARD

if __name__ == "__main__":
    deck = create_deck()
    known = [card_to_value('AS'), card_to_value('10H')]

    deck = remove_known_cards(deck, known)

    print(len(deck))
    print(card_to_value('AS') in deck)
    print(card_to_value('10H') in deck)
    
    
from hand_ev import evaluate_hand, ONE_PAIR, HIGH_CARD

cards = [
    (14, 0), (14, 1),
    (10, 2), (9, 3), (5, 0), (3, 1), (2, 2)
]

rank, tb = evaluate_hand(cards)
assert rank == ONE_PAIR
assert tb[0] == 14

cards = [
    (14, 0), (13, 1), (10, 2),
    (9, 3), (5, 0), (3, 1), (2, 2)
]

rank, tb = evaluate_hand(cards)
assert rank == HIGH_CARD
assert tb[0] == 14

print("OK")

