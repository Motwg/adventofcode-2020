import itertools


def count_adjacent_neighbours(grid, pos, char='#'):
    assert isinstance(pos, tuple)
    ctn = 0
    for neighbour in itertools.product((-1, 0, 1), (-1, 0, 1)):
        if neighbour != (0, 0) and pos[1] + neighbour[1] > -1 and pos[0] + neighbour[0] > -1:
            try:
                if grid[pos[1] + neighbour[1]][pos[0] + neighbour[0]] == char:
                    ctn += 1
            except IndexError:
                pass
    return ctn


def count_neighbours(grid, pos):
    assert isinstance(pos, tuple)
    ctn = 0
    for neighbour in itertools.product((-1, 0, 1), (-1, 0, 1)):
        if neighbour != (0, 0):
            offset = neighbour
            while len(grid) > pos[1] + offset[1] > -1 \
                    and len(grid[0]) > pos[0] + offset[0] > -1:
                char = grid[pos[1] + offset[1]][pos[0] + offset[0]]
                if char == '.':
                    offset = tuple(map(int.__add__, offset, neighbour))
                    continue
                if char == '#':
                    ctn += 1
                break
    return ctn


def change(char):
    return '#' if char == 'L' else 'L'


def get_to_change_seats_p1(lines):
    to_change = set([])
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char == 'L' and count_adjacent_neighbours(lines, (x, y)) == 0:
                to_change.add((x, y))
            elif char == '#' and count_adjacent_neighbours(lines, (x, y)) > 3:
                to_change.add((x, y))
    return to_change


def get_to_change_seats_p2(lines):
    to_change = set([])
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char == 'L' and count_neighbours(lines, (x, y)) == 0:
                to_change.add((x, y))
            elif char == '#' and count_neighbours(lines, (x, y)) > 4:
                to_change.add((x, y))
    return to_change


def sit_people(lines, changing_function):
    seats = lines.copy()
    while True:
        to_change = changing_function(seats)
        if len(to_change) == 0:
            return seats
        for seat in to_change:
            seats[seat[1]] = seats[seat[1]][:seat[0]] \
                                + change(seats[seat[1]][seat[0]]) \
                                + seats[seat[1]][seat[0] + 1:]


if __name__ == '__main__':
    with open('input.txt', 'r') as reader:
        lines = [line.replace('\n', '') for line in reader]
    print('Part One: ', sum([line.count('#') for line in sit_people(lines, get_to_change_seats_p1)]))
    print('Part Two: ', sum([line.count('#') for line in sit_people(lines, get_to_change_seats_p2)]))
