def neighbour(p1, p2):
    assert isinstance(p1, tuple) and isinstance(p2, tuple)
    return True if sum([abs(x1 - x2) for x1, x2 in zip(p1, p2)]) == 1 else False


def get_neighbours(p):
    neighbours = []
    for idx, x in enumerate(p):
        nb1, nb2 = list(p), list(p)
        nb1[idx], nb2[idx] = x + 1, x - 1
        neighbours.extend([tuple(nb1), tuple(nb2)])
    return neighbours


if __name__ == '__main__':
    with open('test.txt', 'r') as reader:
        lines = [line.replace('\n', '') for line in reader]
    actives = set([])
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char == '#':
                actives.add((x, y, 0))

        # set(filter(lambda x: x is not None, [a1 if neighbour(a, a1) else None for a1 in actives]))
    for _ in range(6):
        to_add = set([])
        to_remove = set([])
        for a in actives:
            for nb in get_neighbours(a):
                if nb not in actives:
                    if sum([1 if nb_of_nb in actives else 0 for nb_of_nb in get_neighbours(nb)]) == 3:
                        to_add.add(nb)
            if not 1 < sum([1 if neighbour(a, a1) else 0 for a1 in actives]) < 4:
                to_remove.add(a)
        actives.difference_update(to_remove)
        actives.update(to_add)
        print(len(actives))
        print(to_add)
        print(to_remove)
