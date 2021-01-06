from collections import deque


class Player:

    def __init__(self, lines):
        self.cards = deque(map(int, lines))
        self.no_sub_game = 0
        self.decks = []

    def __str__(self):
        return str(self.cards)

    def fight(self, other):
        assert isinstance(other, Player)
        print('DECK ONE: {}'.format(self.cards))
        print('DECK TWO: {}'.format(other.cards))
        my = self.cards.popleft()
        his = other.cards.popleft()
        print('PLAY ONE: {}'.format(my))
        print('PLAY TWO: {}'.format(his))
        if my > his:
            self.cards.append(my)
            self.cards.append(his)
        elif his > my:
            other.cards.append(his)
            other.cards.append(my)

    def fight2(self, other):
        assert isinstance(other, Player)
        print('DECK ONE: {}'.format(self.cards))
        print('DECK TWO: {}'.format(other.cards))
        my = self.cards.popleft()
        his = other.cards.popleft()
        print('PLAY ONE: {}'.format(my))
        print('PLAY TWO: {}'.format(his))
        for my_deck, his_deck in zip(self.decks, other.decks):
            if self.cards == my_deck and other.cards == his_deck:
                print('REPEATED! PLAYER ONE WON')
                self.cards.append(my)
                self.cards.append(his)
                return
        self.decks.append(self.cards.copy())
        other.decks.append(other.cards.copy())
        if my <= len(self.cards) and his <= len(other.cards):
            print('STARTING SUB GAME')
            new_my_deck = self.cards.copy()
            new_his_deck = other.cards.copy()
            self.sub_game(
                other,
                [new_my_deck.popleft() for _ in range(my)],
                [new_his_deck.popleft() for _ in range(his)]
            )
        else:
            if my > his:
                self.cards.append(my)
                self.cards.append(his)
            elif his > my:
                other.cards.append(his)
                other.cards.append(my)

    def sub_game(self, other, my_deck, his_deck):
        self.no_sub_game += 1
        my = len(my_deck)
        his = len(his_deck)
        player_one = Player(my_deck)
        player_two = Player(his_deck)
        iteration = 1
        while player_one.get_no_cards() > 0 and player_two.get_no_cards() > 0:
            print('\nSUB GAME {}'.format(self.no_sub_game))
            print('ROUND {}'.format(iteration))
            player_one.fight2(player_two)
            iteration += 1

            my_decks, his_decks = [], []
            for my_deck, his_deck in zip(my_decks, his_decks):
                if player_one.cards == my_deck and player_two.cards == his_deck:
                    print('REPEATED! PLAYER ONE WON')
                    self.cards.append(my)
                    self.cards.append(his)
                    return
            my_decks.append(player_one.cards.copy())
            his_decks.append(player_two.cards.copy())
        else:
            if player_two.get_no_cards() == 0:
                print('WINNER ONE')
                self.cards.append(my)
                self.cards.append(his)
            else:
                print('WINNER TWO')
                other.cards.append(his)
                other.cards.append(my)

    def get_no_cards(self):
        return len(self.cards)

    def get_deck_value(self):
        card = 1
        value = 0
        while len(self.cards) > 0:
            value += self.cards.pop() * card
            card += 1
        return value
