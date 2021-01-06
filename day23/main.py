from day23.circle import Circle

values = [5, 8, 6, 4, 3, 9, 1, 7, 2]

current = max(values)
while len(values) != 10000:
    current += 1
    values.append(current)

# values = [3, 8,  9,  1,  2,  5,  4,  6,  7]
# vals = [5, 8, 6, 4, 3, 9, 1, 7, 2] + [x for x in range(10, 100000)]
circle = Circle(values)

try:
    for _ in range(100000):
        circle.round()
except Exception as e:
    print(e.args)

print('\n', circle)
# print(circle.got)
# print(circle.r_moves)
