from functools import reduce

entries = []

with open('input.txt', 'r') as reader:
    for line in reader:
        entries.append(line.replace('\n', ''))

ctn = []
rights = [1, 3, 5, 7, 1]
downs = [1, 1, 1, 1, 2]
for right, down in zip(rights, downs):
    trees = 0
    x = 0
    for i, entry in enumerate(entries[:]):
        if i % down == 0:
            if entry[x % len(entry)] == '#':
                trees += 1
            x += right
    ctn.append(trees)

print(reduce((lambda x, y: x * y), ctn))
