class Waypoint:
    def __init__(self):
        self.pos = 10 + 1j

    def move(self, action, value, ship_pos):
        assert isinstance(action, str)
        assert isinstance(ship_pos, complex)
        self.pos = {
            'L': self.pos * 1j ** (value//90),
            'R': self.pos * (-1j) ** (value//90)
        }.get(action.upper(), self.pos)
        self.pos += {
            'N': value * 1j,
            'E': value,
            'S': -value * 1j,
            'W': -value
        }.get(action.upper(), 0)
        self.pos = round(self.pos.real, 1) + round(self.pos.imag, 1) * 1j

    def __str__(self):
        return '({} {})'.format(self.pos.real, self.pos.imag)
