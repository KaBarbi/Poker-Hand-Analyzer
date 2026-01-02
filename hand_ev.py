from collections import Counter

# Hand ranks
HIGH_CARD = 0
ONE_PAIR = 1
TWO_PAIR = 2
THREE_KIND = 3
STRAIGHT = 4
FLUSH = 5
FULL_HOUSE = 6
FOUR_KIND = 7
STRAIGHT_FLUSH = 8


def evaluate_hand(cards):
    """
    cards: list of 7 cards in (value, suit)
    returns: (rank, tiebreakers)

    Examples:
    (8, [14])       -> Straight Flush A-high
    (6, [13, 10])   -> Full House K over 10
    """
    values = [v for v, _ in cards]
    suits = [s for _, s in cards]

    counts = Counter(values)

    # FOR NOW: only High Card and One Paair
    pair_value = get_pair_value(counts)
    if pair_value:
        kickers = sorted(
            [v for v in values if v != pair_value],
            reverse=True
        )[:3]
        return (ONE_PAIR, [pair_value] + kickers)

    high_cards = sorted(values, reverse=True)[:5]
    return (HIGH_CARD, high_cards)


def get_pair_value(counts):
    for value, count in counts.items():
        if count == 2:
            return value
    return None
