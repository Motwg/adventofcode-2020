if __name__ == '__main__':
    with open('input.txt', 'r') as reader:
        groups_one, group_one, groups_all, group_all, inited = [], set([]), [], set([]), False
        for line in reader:
            if line == '\n':
                groups_one.append(group_one)
                group_one = set([])
                groups_all.append(group_all)
                inited = False
            else:
                unique_line = set([char for char in line.replace('\n', '')])
                group_one.update(unique_line)
                if inited:
                    group_all.intersection_update(unique_line)
                else:
                    group_all, inited = unique_line, True
    print('Part One: ', sum([len(group) for group in groups_one]))
    print('Part Two: ', sum([len(group) for group in groups_all]))
