if __name__ == '__main__':
    with open('input.txt', 'r') as reader:
        timestamp, busses = [line.replace('\n', '') for line in reader]
    timestamp = int(timestamp)
    (busses := {(int(bus) if bus != 'x' else bus): ((int(bus) - idx) % int(bus) if bus != 'x' else None)
                for idx, bus in enumerate(busses.split(','))}).pop('x')
    now = timestamp
    first = None
    while first is None:
        now += 1
        for bus in busses:
            if now % bus == 0:
                first = bus
    print('Part One: ', (now - timestamp) * first)
    accelerator = 1
    for k, v in busses.items():
        while timestamp % k != v:
            timestamp += accelerator
        accelerator *= k
    print('Part Two: ', timestamp)
