import copy


def perform(instructions, current=0, accumulator=0, visited=None):
    if visited is None:
        visited = []
    if current in visited:
        return accumulator
    if current not in instructions.keys():
        raise Exception(accumulator)
    visited.append(current)
    if instructions[current][0] == 'nop':
        return perform(instructions, current+1, accumulator, visited)
    elif instructions[current][0] == 'acc':
        return perform(instructions, current + 1, accumulator + instructions[current][1], visited)
    elif instructions[current][0] == 'jmp':
        return perform(instructions, current + instructions[current][1], accumulator, visited)
    else:
        raise Exception('Unknown instruction')


def swap_instruction(instructions, idx):
    new_instructions = copy.deepcopy(instructions)
    if new_instructions[idx][0] == 'nop':
        new_instructions[idx][0] = 'jmp'
    elif new_instructions[idx][0] == 'jmp':
        new_instructions[idx][0] = 'nop'
    return new_instructions


if __name__ == '__main__':
    with open('input.txt', 'r') as reader:
        instructions = {idx: [line.split()[0], int(line.split()[1])] for idx, line in enumerate(reader)}
    print('Part One:', perform(instructions))
    for i in range(len(instructions.keys())):
        try:
            perform(swap_instruction(instructions, i))
        except Exception as e:
            print('Part Two:', e.args[0])
