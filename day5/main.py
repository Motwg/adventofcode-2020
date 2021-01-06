with open('input.txt', 'r') as reader:
    f = lambda s, list_x, list_y: (s := s.replace(x, y) for x, y in zip(list_x, list_y))
    seats = [[x for x in f(line, ['\n', 'F', 'B', 'R', 'L'], ['', '0', '1', '1', '0'])][-1] for line in reader]
print('Part One: ', max(seats := set([int(seat[:7], 2) * 8 + int(seat[7:], 2) for seat in seats])))
[print('Part Two: ', seat) for seat in {x for x in range(min(seats), max(seats))}.difference(seats)]
