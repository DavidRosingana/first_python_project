class Card:
    def __init__(self):
        self.number = number
        self.suit = suit


class Deck:
    suit = ["hearts", "diamonds", "spades", "clubs"]
    max_mumber = 13

    def __init__(self):
        self.cards = []

        for suit in self.suit:
            for number in range(1, self.max_mumber + 1):
                self.cards.append(Card(number, suit))

    def random_card(self):
        pos = 0
        return self.cards.pop(pos)