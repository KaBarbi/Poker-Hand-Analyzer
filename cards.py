# 52 Cards
# value: 2-14 (where 14 = Ace)
# suit: 0–3
# ('A', 'S') → (14, 'S')

def card_to_value(card):
    """
    Convert card notation to (value, suit).

    card: tuple ('A', 'S') or string 'AS', '10H', 'TD'
    """
    if isinstance(card, str):
        rank, suit = card[:-1], card[-1]
    else:
        rank, suit = card

    rank_map = {
        '2': 2, '3': 3, '4': 4, '5': 5, '6': 6,
        '7': 7, '8': 8, '9': 9,
        '10': 10, 'T': 10,
        'J': 11, 'Q': 12, 'K': 13, 'A': 14
    }

    suit_map = {'H': 0, 'D': 1, 'C': 2, 'S': 3}

    if rank not in rank_map or suit not in suit_map:
        raise ValueError(f"Carta inválida: {card}")

    return rank_map[rank], suit_map[suit]


def create_deck():
    """
    Create a complete deck of 52 cards.
    Returns a list of (value, suit) tuples.
    """
    ranks = ['2', '3', '4', '5', '6', '7',
             '8', '9', '10', 'J', 'Q', 'K', 'A']
    suits = ['H', 'D', 'C', 'S']

    return [card_to_value((rank, suit)) for rank in ranks for suit in suits]


def remove_known_cards(deck, known_cards):
    """
    Remove known cards from the deck.

    deck: list of (value, suit)
    known_cards: list of (value, suit)
    """
    return [card for card in deck if card not in known_cards]
