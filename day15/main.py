def game(numbers, no_turns):
    assert isinstance(numbers, dict)
    last = tuple(numbers)[-1]
    turn = max(numbers.values())
    while turn < no_turns:
        spoken = turn - numbers.get(last, turn)
        numbers[last] = turn
        last = spoken
        turn += 1
    return spoken


if __name__ == '__main__':
    numbers = {number: idx + 1 for idx, number in enumerate([1, 20, 8, 12, 0, 14])}
    print('Part One:', game(numbers.copy(), 2020))
    print('Part Two:', game(numbers.copy(), 30000000))
