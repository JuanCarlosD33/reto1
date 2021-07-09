import random as rd

suits = ["Hearts", "Spades", "Clubs", "Diamonds"]
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
deck = []
hand = []

for  suit in suits:
  for rank in ranks:
    deck.append(f'{rank} of {suit}')

cant = len(deck)

print(f"\nThere are {cant} cards in the deck.")

hand = rd.choices(deck, k = 5)

for card in hand:

    deck.remove(card)
    print("Dealing ...")

cant = len(deck)

print(f"There are {cant} cards in the deck.\n")

print("Player has the following cards in their hand: \n")

print(f"{hand[0]}, {hand[1]}, {hand[2]}, {hand[3]}, {hand[4]}.\n\n")