from collections import deque


class Player:

    def __init__(self, lines):
        self.cards = deque(map(int, lines))
        self.prev_cards = []

    def __str__(self):
        return str(self.cards)

    def next_card(self):
        self.prev_cards.append(list(self.cards.copy()))
        card = self.cards.popleft()
        return card

    def get_deck_value(self):
        card = 1
        value = 0
        while len(self.cards) > 0:
            value += self.cards.pop() * card
            card += 1
        return value

    def get_no_cards(self):
        return len(self.cards)

    def won(self, first, second):
        self.cards.append(first)
        self.cards.append(second)
