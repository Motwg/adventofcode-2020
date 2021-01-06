def rotate_clockwise(strings):
    return [''.join(line) for line in zip(*strings[::-1])]


def rotate_counter_clockwise(strings):
    x = strings
    return [x := rotate_clockwise(x) for _ in range(3)][-1]


def flip_upside_down(strings):
    return strings[::-1]


def flip_left_right(strings):
    return [line[::-1] for line in strings]


def replace_in_string(string, replace_from, replace_to):
    return [string := string.replace(x, y) for x, y in zip(replace_from, replace_to)][-1]


def get_bin(x, n):
    return format(x, 'b').zfill(n)


if __name__ == '__main__':
    pattern = ['1234',
               '5678',
               '9012']
    print(rotate_clockwise(pattern))
    print(rotate_counter_clockwise(pattern))
    print(flip_upside_down(pattern))
    print(flip_left_right(pattern))
