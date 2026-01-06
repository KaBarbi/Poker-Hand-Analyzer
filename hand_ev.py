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
    values = [v for v, _ in cards]
    counts = Counter(values)

    pairs = get_pairs(counts)

    trips = get_trips(counts)
    pairs = get_pairs(counts)

  # Three of a Kind
    if trips:
        kickers = sorted(
            [v for v in values if v != trips],
            reverse=True
        )[:2]
        return (THREE_KIND, [trips] + kickers)

    # Two Pair
    if len(pairs) >= 2:
        high_pair, low_pair = pairs[:2]
        kicker = max(v for v in values if v not in (high_pair, low_pair))
        return (TWO_PAIR, [high_pair, low_pair, kicker])

    # One Pair
    if len(pairs) == 1:
        pair_value = pairs[0]
        kickers = sorted(
            [v for v in values if v != pair_value],
            reverse=True
        )[:3]
        return (ONE_PAIR, [pair_value] + kickers)

    # High Card
    high_cards = sorted(values, reverse=True)[:5]
    return (HIGH_CARD, high_cards)


def get_pairs(counts):
    """
    Returns a list of pair values sorted descending.
    """
    return sorted(
        [value for value, count in counts.items() if count == 2],
        reverse=True
    )


def get_trips(counts):
    """
    Returns the value of the three of a kind or None.
    """
    for value, count in counts.items():
        if count == 3:
            return value
    return None
