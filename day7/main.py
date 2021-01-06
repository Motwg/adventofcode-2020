from strings import replace_in_string


def count(bag, d):
    contains = 1
    for quantity, bag in d[bag]:
        contains += quantity * count(bag, d)
    return contains


if __name__ == '__main__':
    with open('input.txt', 'r') as reader:
        d = {}
        for line in reader:
            k, v = replace_in_string(line, ('.\n', 'no', ' bags', ' bag'), ('', '0', '', '')).split(' contain ')
            v = [(int(entry.split(' ', 1)[0]), entry.split(' ', 1)[1])for entry in v.split(', ')]
            v = list(filter(lambda x: x[0] != 0, v))
            d.setdefault(k, v)

    can_contain_shiny_gold = {'shiny gold'}
    for i in range(20):
        for k, v in d.items():
            for entry in v:
                if entry[1] in can_contain_shiny_gold:
                    can_contain_shiny_gold.add(k)
    print('Part One: ', len(can_contain_shiny_gold) - 1)

    contains = 0
    for quantity, bag in d['shiny gold']:
        contains += quantity * count(bag, d)
    print('Part Two: ', contains)
