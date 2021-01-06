

entries = []

with open('input.txt', 'r') as reader:
    for line in reader:
        entries.append(int(line.replace('\n', '')))


print(entries)
i = 1
for x in entries:
    for y in entries:
        if x + y == 2020:
            print(x, ' ', y, ' ', x * y)
print('part two')
for x in entries:
    for y in entries:
        for z in entries:
            if x + y + z == 2020:
                print(x, ' ', y, ' ', z, '   ', x * y * z)
