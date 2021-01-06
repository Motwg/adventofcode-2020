import re


class Tile:

    def __init__(self, nr, lines):
        self.nr = int(nr.split()[1].replace(':', ''))
        self.commons = []
        self.lines = lines
        self.border = []
        self._update_border()
        self._update_center()

    def __str__(self):
        return '\n'.join(self.lines)

    def _update_center(self):
        string = ''.join(self.lines[1:-1])
        compressed = ''.join('' if i % 10 in [0, 9] else char for i, char in enumerate(string))
        self.center = re.findall('........', compressed)

    def _update_border(self):
        compressed = ''.join(self.lines)
        self.border = [self.lines[0], compressed[9::10], self.lines[9], compressed[::10]]

    def update(self):
        self._update_center()
        self._update_border()

    def get_common(self, other):
        assert isinstance(other, Tile)
        common = []
        if self != other:
            for border in self.border:
                if border in other.border:
                    common.append(border)
                if border[::-1] in other.border:
                    common.append(border)
        return common

    def delete_common(self, other):
        assert isinstance(other, Tile)
        if self != other:
            for border in self.border:
                if border in other.border:
                    other.border.remove(border)
                    self.border.remove(border)
                    self.commons.append(other)
                    other.commons.append(self)
                if border[::-1] in other.border:
                    other.border.remove(border[::-1])
                    self.border.remove(border)
                    self.commons.append(other)
                    other.commons.append(self)

    def rotate_clockwise(self):
        self.lines = [''.join(line) for line in zip(*self.lines[::-1])]
        self.update()

    def rotate_counter_clockwise(self):
        for i in range(3):
            self.rotate_clockwise()

    def flip_upside_down(self):
        self.lines = self.lines[::-1]
        self.update()

    def flip_left_right(self):
        self.lines = [line[::-1] for line in self.lines]
        self.update()
