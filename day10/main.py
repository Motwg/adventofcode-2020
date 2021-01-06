def ones_to_arranges(ones):
    return {
        2: 2,
        3: 4,
        4: 7
    }.get(ones, 1)


if __name__ == '__main__':
    with open('input.txt', 'r') as reader:
        (numbers := [int(x) for x in reader]).append(0)
        numbers.sort()
    numbers = {x: y for x, y in zip(numbers, numbers[1:] + [max(numbers) + 3])}
    diffs = [v - k for k, v in numbers.items()]
    print('Part One: ', diffs.count(1) * diffs.count(3))
    ctn, arranges = 0, 1
    for x in diffs:
        if x == 1:
            ctn += 1
        else:
            arranges *= ones_to_arranges(ctn)
            ctn = 0
    print('Part Two: ', arranges)
