from cards import create_deck, card_to_value, remove_known_cards

if __name__ == "__main__":
    deck = create_deck()
    known = [card_to_value('AS'), card_to_value('10H')]

    deck = remove_known_cards(deck, known)

    print(len(deck))
    print(card_to_value('AS') in deck)
    print(card_to_value('10H') in deck)
