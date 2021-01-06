from random import choice

from plain import Plain
from tile import Tile
import strings as s

entries = []
no_elements = 12

with open('test20.txt', 'r') as reader:
    for i, line in enumerate(reader):
        if line != '\n':
            entries.append(line.replace('\n', ''))
size = 10
tiles = [Tile(entries[i * 11], entries[i * 11 + 1: (i + 1) * 11]) for i in range(len(entries) // 11)]

commons = 0
for t1 in tiles:
    for t2 in tiles:
        t1.delete_common(t2)

for t1 in tiles:
    t1.update()

mult = 1
for t in tiles:
    print(t.nr, t.border)
    if len(t.border) == 2:
        mult *= t.nr

print(mult)

print('part two')
plain = Plain(no_elements, tiles)
# test20.txt
plain.tiles[0][0].rotate_counter_clockwise()
print(plain)

# input.txt
# plain.tiles[0][0].rotate_clockwise()
# plain.tiles[0][0].flip_upside_down()
for y in range(no_elements):
    for x in range(no_elements):
        i = 1
        while not plain.check_wisely((x, y)):
            plain.change_wisely((x, y))
            i += 1
print('got it')
print(plain.get_centers_string())


def find_pattern(strings, pattern):
    def split(word):
        return [char for char in word]

    pattern_pos = []
    for y, line in enumerate(pattern):
        for x, char in enumerate(line):
            if char == '#':
                pattern_pos.append((x, y))

    chars = []
    for string in strings:
        chars += string
    chars = list(map(split, chars))
    max_px = max(x for x, y in pattern_pos)
    max_py = max(y for x, y in pattern_pos)
    ctn = 0
    idx = []
    new_chars = chars.copy()
    for y, line in enumerate(chars):
        for x, char in enumerate(line):
            if y + max_py < len(chars) and x + max_px < len(line):
                if all(chars[y + p_y][x + p_x] == '#' for p_x, p_y in pattern_pos):
                    ctn += 1
                    idx.append((x, y))
                    for p_x, p_y in pattern_pos:
                        new_chars[y + p_y][x + p_x] = '.'
    return ctn, idx, new_chars


pattern = ['                  # ',
           '#    ##    ##    ###',
           ' #  #  #  #  #  #   ']

# functions = [s.rotate_clockwise, s.flip_upside_down, s.rotate_counter_clockwise, s.rotate_counter_clockwise]
# for f in functions:
#     pattern = f(pattern)

dragons = 0
while dragons == 0:
    dragons, idx, ocean = find_pattern(plain.get_centers_list(), pattern)
    func = choice([s.rotate_clockwise, s.rotate_counter_clockwise,
                   s.flip_left_right, s.rotate_clockwise])
    pattern = func(pattern)
print(dragons)
ctn = 0
for line in ocean:
    for char in line:
        if char == '#':
            ctn += 1
print(ctn)
