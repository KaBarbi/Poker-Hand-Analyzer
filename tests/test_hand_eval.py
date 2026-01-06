import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from hand_ev import (
    evaluate_hand,
    HIGH_CARD,
    ONE_PAIR,
    TWO_PAIR,
    THREE_KIND
)

def test_high_card():
    cards = [
        (14, 0), (13, 1), (10, 2),
        (9, 3), (5, 0), (3, 1), (2, 2)
    ]

    rank, tb = evaluate_hand(cards)
    assert rank == HIGH_CARD
    assert tb == [14, 13, 10, 9, 5]


def test_one_pair():
    cards = [
        (14, 0), (14, 1),
        (10, 2), (9, 3), (5, 0), (3, 1), (2, 2)
    ]

    rank, tb = evaluate_hand(cards)
    assert rank == ONE_PAIR
    assert tb == [14, 10, 9, 5]


def test_two_pair():
    cards = [
        (14, 0), (14, 1),
        (10, 2), (10, 3),
        (7, 0), (4, 1), (2, 2)
    ]

    rank, tb = evaluate_hand(cards)
    assert rank == TWO_PAIR
    assert tb == [14, 10, 7]


def test_three_of_a_kind():
    cards = [
        (12, 0), (12, 1), (12, 2),
        (14, 0), (10, 1), (5, 2), (2, 3)
    ]

    rank, tb = evaluate_hand(cards)
    assert rank == THREE_KIND
    assert tb == [12, 14, 10]


if __name__ == "__main__":
    test_high_card()
    test_one_pair()
    test_two_pair()
    test_three_of_a_kind()
    print("Hand evaluation tests OK")
