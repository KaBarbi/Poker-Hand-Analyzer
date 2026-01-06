import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from cards import create_deck, card_to_value, remove_known_cards


def test_remove_known_cards():
    deck = create_deck()
    known = [card_to_value('AS'), card_to_value('10H')]

    new_deck = remove_known_cards(deck, known)

    assert len(new_deck) == 50
    assert card_to_value('AS') not in new_deck
    assert card_to_value('10H') not in new_deck


if __name__ == "__main__":
    test_remove_known_cards()
    print("Cards tests OK")
