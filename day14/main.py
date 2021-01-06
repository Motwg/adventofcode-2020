from strings import replace_in_string, get_bin


def apply_mask_p1(integer, mask):
    assert isinstance(mask, str)
    mask_and = mask.replace('X', '1')
    mask_or = mask.replace('X', '0')
    return int(integer) & int(mask_and, 2) | int(mask_or, 2)


def apply_mask_p2(integer, mask):
    assert isinstance(mask, str)
    string = ''
    for i, m in zip(get_bin(integer, 36), mask):
        if m == '0':
            string += i
        elif m == '1':
            string += '1'
        elif m == 'X':
            string += 'X'
    return get_all_numbers(string)


def get_all_numbers(string):
    assert isinstance(string, str)
    try:
        return [int(string, 2)]
    except ValueError:
        numbers = []
        numbers.extend(get_all_numbers(string.replace('X', '1', 1)))
        numbers.extend(get_all_numbers(string.replace('X', '0', 1)))
    return numbers


if __name__ == '__main__':
    with open('input.txt', 'r') as reader:
        instructions = [replace_in_string(line, ['\n', 'mem[', ']'], ['']*3).split(' = ') for line in reader]

    memory = {}
    mask = 'X' * 36
    for ins in instructions:
        if ins[0] == 'mask':
            mask = ins[1]
        else:
            memory[int(ins[0])] = apply_mask_p1(int(ins[1]), mask)
    print('Part One: ', sum(memory.values()))

    memory.clear()
    for ins in instructions:
        if ins[0] == 'mask':
            mask = ins[1]
        else:
            for address in apply_mask_p2(int(ins[0]), mask):
                memory[address] = int(ins[1])
    print('Part Two: ', sum(memory.values()))
