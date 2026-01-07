from collections import Counter, defaultdict

import cards

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

    # Four of a Kind
    quads = [v for v, c in counts.items() if c == 4]
    if quads:
        quad_value = max(quads)
        kicker = max(v for v in values if v != quad_value)
        return (FOUR_KIND, [quad_value, kicker])

    # Full House
    trips = sorted([v for v, c in counts.items() if c == 3], reverse=True)
    pairs = sorted([v for v, c in counts.items() if c == 2], reverse=True)

    if trips and (pairs or len(trips) >= 2):
        trip_value = trips[0]
        if pairs:
            pair_value = pairs[0]
        else:
            pair_value = trips[1]
        return (FULL_HOUSE, [trip_value, pair_value])

    # Flush
    flush_values = get_flush_values(cards)
    if flush_values:
        return (FLUSH, flush_values)

    # Straight
    straight_high = get_straight_high(values)
    if straight_high:
        return (STRAIGHT, [straight_high])

    # Three of a Kind
    trips = sorted(
        [v for v, c in counts.items() if c == 3],
        reverse=True
    )
    if trips:
        trip_value = trips[0]
        kickers = sorted(
            [v for v in values if v != trip_value],
            reverse=True
        )[:2]
        return (THREE_KIND, [trip_value] + kickers)

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


def get_straight_high(values):
    unique = set(values)

    if 14 in unique:
        unique.add(1)

    sorted_vals = sorted(unique)

    longest = []
    current = []

    for v in sorted_vals:
        if not current or v == current[-1] + 1:
            current.append(v)
        else:
            current = [v]

        if len(current) >= 5:
            longest = current[:]

    if longest:
        return max(longest)

    return None


def get_flush_values(cards):
    suits = defaultdict(list)

    for value, suit in cards:
        suits[suit].append(value)

    for values in suits.values():
        if len(values) >= 5:
            return sorted(values, reverse=True)[:5]

    return None
