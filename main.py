from cards import card_to_value
from hand_ev import evaluate_hand
from compare import compare_hands

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
    player_a = ["AS", "KS", "QS", "JS", "10S", "2D", "3C"]
    player_b = ["9H", "9D", "9S", "9C", "2H", "3D", "4C"]

    hand_a = evaluate_hand([card_to_value(c) for c in player_a])
    hand_b = evaluate_hand([card_to_value(c) for c in player_b])

    result = compare_hands(hand_a, hand_b)

    print("Player A:", HAND_NAMES[hand_a[0]], hand_a[1])
    print("Player B:", HAND_NAMES[hand_b[0]], hand_b[1])

    if result == 1:
        print("Player A wins")
    elif result == -1:
        print("Player B wins")
    else:
        print("Tie")


if __name__ == "__main__":
    main()
