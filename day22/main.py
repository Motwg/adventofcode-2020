from day22.player import Player
from day22.game import Game


def part_one(player_one, player_two):
    iteration = 0
    while player_one.get_no_cards() > 0 and player_two.get_no_cards() > 0:
        player_one.fight(player_two)
        iteration += 1
    print(iteration)
    print(player_one, player_one.get_deck_value())
    print(player_two, player_two.get_deck_value())


def part_two(player_one, player_two):
    iteration = 1
    while player_one.get_no_cards() > 0 and player_two.get_no_cards() > 0:
        print('\nGAME ROUND {}'.format(iteration))
        player_one.fight2(player_two)
        iteration += 1
    print(iteration)
    print(player_one, player_one.get_deck_value())
    print(player_two, player_two.get_deck_value())


lines = []
with open('input.txt', 'r') as reader:
    for line in reader:
        lines.append(line.replace('\n', ''))
player_one = Player(lines[1:26])
player_two = Player(lines[28:53])

# player_one = Player(lines[0:5])
# player_two = Player(lines[6:11])

# player_one = Player(lines[0:2])
# player_two = Player(lines[3:6])

print(player_one)
print(player_two)
# part_one(player_one, player_two)
# part_two(player_one, player_two)
game = Game(1, player_one, player_two)
winner = game.start()
print('\nPLAYER {} WON'.format(winner))
if winner == 1:
    print(player_one.get_deck_value())
elif winner == 2:
    print(player_two.get_deck_value())
