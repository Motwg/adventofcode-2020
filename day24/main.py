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
    adjacent_tiles = {}
    for pos1 in tiles:
        adjacent_tiles.setdefault(pos1, [])
        for pos2 in get_possible_adjacent(pos1):
            if pos2 in tiles:
                adjacent_tiles[pos1].append(pos2)
    return adjacent_tiles


def get_possible_adjacent(pos):
    return [cord_switcher(code)(*pos) for code in ['7', '4', '1', '9', '6', '3']]


def difference(list1, list2):
    return set(list1).difference(set(list2))


def count_in(list1, list2):
    return sum([1 if element in list2 else 0 for element in list1])


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
    tiles = list(filter(None.__ne__, [k if v == 'b' else None for k, v in tiles.items()]))

    for day in range(100):
        adjacent_tiles = adjacent_dict(tiles)

        to_add, to_remove = set([]), set([])
        for tile in tiles:
            blacks = adjacent_tiles[tile]
            if len(blacks) > 2 or len(blacks) == 0:
                to_remove.add(tile)
            for white in difference(get_possible_adjacent(tile), blacks):
                adjacent = get_possible_adjacent(white)
                if count_in(adjacent, tiles) == 2:
                    to_add.add(white)

        for pos in to_remove:
            tiles.remove(pos)
        for pos in to_add:
            tiles.append(pos)
        print('DAY {:3d}: {}'.format(day + 1, len(tiles)))
