def cord_switcher(code):
    switcher = {
        '7': lambda x, y: (x - 1, y + 1),
        '4': lambda x, y: (x - 2, y),
        '1': lambda x, y: (x - 1, y - 1),
        '9': lambda x, y: (x + 1, y + 1),
        '6': lambda x, y: (x + 2, y),
        '3': lambda x, y: (x + 1, y - 1)
    }
    return switcher.get(code)


def flip_tile(tile):
    return 'w' if tile == 'b' else 'b'


def init_tiles(lines):
    tiles = {}
    for line in lines:
        pos = (0, 0)
        for char in line:
            pos = cord_switcher(char)(*pos)
        if pos not in tiles.keys():
            tiles[pos] = 'b'
        else:
            tiles[pos] = flip_tile(tiles[pos])
    return tiles


def count_color(tiles, color='b'):
    assert isinstance(tiles, dict)
    return list(tiles.values()).count(color)


def is_adjacent(pos1, pos2):
    return True if abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1]) == 2 and pos1[0] != pos2[0] else False


def adjacent_dict(tiles):
    assert isinstance(tiles, dict)
    adjacent_tiles = {}
    for k1 in tiles.keys():
        adjacent_tiles.setdefault(k1, 0)
        for k2, color in tiles.items():
            if color == 'b' and is_adjacent(k1, k2):
                adjacent_tiles[k1] += 1
    return adjacent_tiles


def get_possible_adjacent(pos):
    return [cord_switcher(code)(*pos) for code in ['7', '4', '1', '9', '6', '3']]


def fill(tiles):
    assert isinstance(tiles, dict)
    new_tiles = {}
    for k in tiles.keys():
        for pos in get_possible_adjacent(k):
            if pos not in tiles.keys():
                new_tiles.setdefault(pos, 'w')
    tiles.update(new_tiles)


if __name__ == '__main__':
    lines = []
    with open('input.txt', 'r') as reader:
        for line in reader:
            lines.append(line.replace('\n', '')
                         .replace('se', '3')
                         .replace('sw', '1')
                         .replace('ne', '9')
                         .replace('nw', '7')
                         .replace('e', '6')
                         .replace('w', '4'))
    tiles = init_tiles(lines)

    print('Part One: ', count_color(tiles))

    for day in range(100):
        fill(tiles)
        adjacent_tiles = adjacent_dict(tiles)

        to_change = []
        for k, v in tiles.items():
            blacks = adjacent_tiles[k]
            if v == 'b':
                if blacks == 0 or blacks > 2:
                    to_change.append(k)
            elif v == 'w':
                if blacks == 2:
                    to_change.append(k)

        for pos in to_change:
            tiles[pos] = flip_tile(tiles[pos])
        print('DAY {:3d}: {}'.format(day + 1, count_color(tiles)))
        print(len(tiles))
