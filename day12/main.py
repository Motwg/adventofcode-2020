from day12.ship import Ship
from day12.waypoint import Waypoint

if __name__ == '__main__':
    with open('input.txt', 'r') as reader:
        instructions = [(line.replace('\n', '')[0], int(line.replace('\n', '')[1:])) for line in reader]
    ship = Ship()
    [ship.sail(*ins) for ins in instructions]
    print('Part One:', int(abs(ship.pos.real) + abs(ship.pos.imag)))

    ship, wp = Ship(), Waypoint()
    for ins in instructions:
        ship.move(*ins, wp.pos)
        wp.move(*ins, ship.pos)
    print('Part Two:', int(abs(ship.pos.real) + abs(ship.pos.imag)))
