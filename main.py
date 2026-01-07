from cards import card_to_value
from hand_ev import evaluate_hand

HAND_NAMES = {
    0: "High Card",
    1: "One Pair",
    2: "Two Pair",
    3: "Three of a Kind",
    4: "Straight",
    5: "Flush",
    6: "Full House",
    7: "Four of a Kind",
    8: "Straight Flush"
}


def main():
    # Exemplo fixo (pode trocar depois)
    cards_input = ["AS", "KS", "QS", "JS", "10S", "2D", "3C"]

    cards = [card_to_value(c) for c in cards_input]

    rank, tiebreakers = evaluate_hand(cards)

    print("Cards:", cards_input)
    print("Hand:", HAND_NAMES[rank])
    print("Tiebreakers:", tiebreakers)


if __name__ == "__main__":
    main()
