# Poker Hand Analyzer (Texas Hold’em)

A Texas Hold’em poker hand analyzer written in Python, focused on evaluating hand strength and calculating win probabilities using Monte Carlo simulation.

This project **does not implement betting or full game flow**. Its purpose is to correctly and efficiently evaluate poker hands in a clean, extensible way.

---

## Project Goal

Given:
- player hole cards
- community cards (partial or complete)
- number of opponents

The system should compute:
- win probability
- tie probability
- loss probability

---

## Current Scope

### Implemented
- Consistent internal card representation `(value, suit)`
- Full deck creation (52 cards)
- Removal of known cards from the deck
- Hand evaluation:
  - High Card
  - One Pair

### Not Implemented Yet
- Two Pair
- Three of a Kind
- Straight
- Flush
- Full House
- Four of a Kind
- Straight Flush
- Monte Carlo simulation
- CLI interface

## Project Structure
```
poker/
├── cards.py # Card representation and deck utilities
├── hand_eval.py # Hand evaluation logic
├── simulator.py # (future) Monte Carlo simulation
├── main.py # (future) CLI interface
├── test_cards.py
└── test_hand_eval.py
```



