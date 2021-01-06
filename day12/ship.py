import cmath


class Ship:
    def __init__(self):
        self.angle = 0
        self.pos = 0j

    def sail(self, action, value):
        assert isinstance(action, str)
        self.angle += {
            'L': value,
            'R': -value
        }.get(action.upper(), 0)
        self.pos += {
            'N': value * 1j,
            'E': value,
            'S': -value * 1j,
            'W': -value,
            'F': (cmath.rect(value, self.angle / 180 * cmath.pi))
        }.get(action.upper(), 0)
        self.pos = round(self.pos.real, 1) + round(self.pos.imag, 1) * 1j

    def move(self, action, value, waypoint_pos):
        assert isinstance(action, str)
        assert isinstance(waypoint_pos, complex)
        if action.upper() == 'F':
            self.pos += waypoint_pos * value

    def __str__(self):
        return '({} {}) {}'.format(self.pos.real, self.pos.imag, self.angle)
