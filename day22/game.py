from day22.player import Player


class Game:

    def __init__(self, no_game, p_one, p_two):
        self.round = 0
        self.no_game = no_game
        assert isinstance(p_one, Player)
        assert isinstance(p_two, Player)
        self.one = p_one
        self.two = p_two

    def start(self):
        while self.one.get_no_cards() > 0 and self.two.get_no_cards() > 0:
            self.next_round()
            # print(list(self.one.cards), self.one.prev_cards)
            for one_deck, two_deck in zip(self.one.prev_cards, self.two.prev_cards):
                if one_deck == list(self.one.cards) and two_deck == list(self.two.cards):
                    print('REPEATED')
                    return 1
        if self.one.get_no_cards() == 0:
            return 2
        elif self.two.get_no_cards() == 0:
            return 1

    def next_round(self):
        self.round += 1
        if self.no_game == 1:
            print('\nGAME {} ROUND {}'.format(self.no_game, self.round))
            print('DECK ONE: {}'.format(self.one.cards))
            print('DECK TWO: {}'.format(self.two.cards))
        first = self.one.next_card()
        second = self.two.next_card()
        if self.no_game == 1:
            print('PLAY ONE: {}'.format(first))
            print('PLAY TWO: {}'.format(second))

        # sub game
        if first <= self.one.get_no_cards() and second <= self.two.get_no_cards():
            print('STARTING SUB GAME')
            new_one_deck = self.one.cards.copy()
            new_two_deck = self.two.cards.copy()
            player_one = Player([new_one_deck.popleft() for _ in range(first)])
            player_two = Player([new_two_deck.popleft() for _ in range(second)])
            sub_game = Game(self.no_game + 1, player_one, player_two)
            winner = sub_game.start()
            if winner == 1:
                self.one.won(first, second)
            elif winner == 2:
                self.two.won(second, first)
        # normal game
        else:
            if first > second:
                self.one.won(first, second)
            else:
                self.two.won(second, first)
