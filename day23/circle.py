class Circle:

    def __init__(self, circle):
        self.move = 0
        assert isinstance(circle, list)
        self.circle = circle
        self.min_val = min(circle)
        self.max_val = max(circle)
        self.current = circle[0]
        self.destination = None
        self.pick_ups = []

        self.got = {}
        self.r_moves = []

    def __str__(self):
        return 'cups: {} at {}'.format(self.circle, self.current)

    def register(self):
        got = self.circle.copy()
        got.append(self.current)
        got = tuple(got)
        if got in self.got.keys():
            # print('\n===MOVE {}==='.format(self.move))
            r_move = self.got[got]
            print('LIKE {}'.format(r_move))
            # print('cups: {}  at {}'.format(self.circle, self.current))
            # print('dest: {}'.format(self.destination))
            if r_move in self.r_moves:
                # raise Exception('REPEATED from {} to {}'.format(*self.r_moves))
                raise Exception('REPEATED {}'.format(self.r_moves))
            elif len(self.r_moves) < 2:
                self.r_moves.append(r_move)
            else:
                self.r_moves[1] = r_move
            # else:
            #     self.r_moves.append(r_move)
        else:
            self.got[got] = self.move

    def rotate(self, number=1):
        for _ in range(7):
            self.circle.insert(0, self.circle.pop(-1))
        while self.circle[0] != number:
            self.circle.append(self.circle.pop(0))

    def round(self):
        self.move += 1

        self.rotate()
        if self.move % 1000 == 0:
            print('\n===MOVE {}==='.format(self.move))
            print('cups: {}  at {}'.format((self.circle[-4:-1], self.circle[0], self.circle[1:4]), self.current))
        self.pick_up()
        # print('pick: {}'.format(self.pick_ups))
        self.select_destination()
        # print('dest: {}'.format(self.destination))
        self.next()
        self.drop()
        # self.register()
        # print('drop: {}'.format(self.circle))

    def next(self):
        self.current = self.circle[self.get_next_idx(self.current)]

    def get_next_idx(self, number):
        idx = self.circle.index(number) + 1
        if idx >= len(self.circle):
            idx = 0
        return idx

    def get_prev_idx(self, number):
        idx = self.circle.index(number) - 1
        if idx < 0:
            idx = len(self.circle) - 1
        return idx

    def pick_up(self, cups=3):
        for i in range(cups):
            idx = self.get_next_idx(self.current)
            self.pick_ups.append(self.circle.pop(idx))

    def drop(self):
        for cup in self.pick_ups[::-1]:
            self.circle.insert(self.get_next_idx(self.destination), cup)
        self.pick_ups = []

    def select_destination(self):
        destination = self.current - 1
        if destination < self.min_val:
            destination = self.max_val
        while destination not in self.circle:
            destination -= 1
            if destination < self.min_val:
                destination = self.max_val
        self.destination = destination
