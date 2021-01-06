def start(cups, iterations):
    def destination_loop(destination):
        max_val = max(cups)
        return destination if destination > 0 else max_val
    d = {
        cup: next_cup for cup, next_cup in zip(cups, cups[1:] + [cups[0]])
    }
    cur = cups[0]
    for i in range(1, iterations + 1):
        if i % (iterations // 10000) == 0:
            print('LOADING: {:5d}%oo'.format(i // 1000))
        temp_cur = cur
        pickup = [cur := d[cur] for _ in range(3)]
        cur = d[cur]
        destination = temp_cur - 1
        destination = destination_loop(destination)
        while destination in pickup:
            destination -= 1
            destination = destination_loop(destination)

        d[temp_cur], d[pickup[-1]], d[destination] = d[pickup[-1]], d[destination], d[temp_cur]

    x = 1
    return [x := d[x] for _ in range(len(cups) - 1)]  # (temp_cur, pickup, destination), cur  #[x := d[x] for _ in cups]


cups = [5, 8, 6, 4, 3, 9, 1, 7, 2]
test_cups = [3, 8,  9,  1,  2,  5,  4,  6,  7]
cups_mln = cups + [x for x in range(10, 1000000)]
# print('Part One: ', ''.join(map(str, start(cups, 100))))
print('Part Two: ', start(cups_mln, 10000000)[:2])
