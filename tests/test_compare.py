import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from compare import compare_hands
from hand_ev import (
    HIGH_CARD, ONE_PAIR, TWO_PAIR, STRAIGHT
)


def test_rank_wins():
    a = (STRAIGHT, [10])
    b = (ONE_PAIR, [14, 13, 12, 11])
    assert compare_hands(a, b) == 1


def test_kicker_wins():
    a = (ONE_PAIR, [14, 13, 10, 8])
    b = (ONE_PAIR, [14, 13, 9, 8])
    assert compare_hands(a, b) == 1


def test_tie():
    a = (TWO_PAIR, [14, 10, 7])
    b = (TWO_PAIR, [14, 10, 7])
    assert compare_hands(a, b) == 0


if __name__ == "__main__":
    test_rank_wins()
    test_kicker_wins()
    test_tie()
    print("Compare hands tests OK")
