def get_encryption_key(public_key, loop_size):
    value = 1
    for _ in range(loop_size):
        value *= public_key
        value %= 20201227
    return value


if __name__ == '__main__':
    value = 1
    subject_number = 7
    # test
    # door_public_key = 5764801
    # card_public_key = 17807724
    door_public_key = 11349501
    card_public_key = 5107328
    loop_size = 1
    door_loop_size = None
    card_loop_size = None
    while door_loop_size is None or card_loop_size is None:
        value *= subject_number
        value %= 20201227
        if loop_size % 100000 == 0:
            print('{} {}'.format(loop_size, value))
        if value == door_public_key:
            door_loop_size = loop_size
            print('Got door loop size')
        if value == card_public_key:
            card_loop_size = loop_size
            print('Got card loop size')
        loop_size += 1
    print('Loop sizes: ', door_loop_size, card_loop_size)
    print(get_encryption_key(door_public_key, card_loop_size))
