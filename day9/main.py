def is_sum(number, numbers):
    for x in numbers:
        for y in numbers:
            if x != y and x + y == number:
                return True
    return False


def is_contiguous_sum(number, numbers):
    for idx, x in enumerate(numbers[:-1]):
        cont_set = {x}
        for y in numbers[idx + 1:]:
            cont_set.add(y)
            if sum(cont_set) == number:
                return cont_set
    return


if __name__ == '__main__':
    with open('input.txt', 'r') as reader:
        numbers = [int(x) for x in reader]
        for idx, number in enumerate(numbers):
            if idx >= 25:
                if not is_sum(number, numbers[idx - 25:idx]):
                    invalid = number
                    print('Part One: ', invalid)

        for idx, number in enumerate(numbers):
            if idx >= 25:
                if cont_set := is_contiguous_sum(invalid, numbers[idx - 25:idx]):
                    print('Part Two: ', max(cont_set) + min(cont_set))
                    break
