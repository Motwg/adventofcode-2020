from tile import Tile
from random import choice


class Plain:

    def __init__(self, size, tiles):
        self.size = size
        corners = []
        borders = []
        assert isinstance(tiles, list)
        for tile in tiles:
            assert isinstance(tile, Tile)
            if len(tile.commons) == 2:
                corners.append(tile)
            elif len(tile.commons) == 3:
                borders.append(tile)

        def build_first_line():
            line = [corners[0], corners[0].commons[0]]
            for i in range(1, self.size - 1):
                for common in line[i].commons:
                    if (common in borders or common in corners) and common not in line:
                        line.append(common)
            return line

        def next_line(prev_line):
            line = []
            for i in range(self.size):
                for common in prev_line[i].commons:
                    if common not in prev_line:
                        line.append(common)
            return line

        self.tiles = [build_first_line()]
        self.tiles.append(next_line(self.tiles[0]))
        for i in range(1, self.size - 1):
            self.tiles.append(next_line(self.tiles[i] + self.tiles[i - 1]))

    def __str__(self):
        grid = []
        for tile_line in self.tiles:
            grid_line = []
            for i in range(10):
                line = []
                for tile in tile_line:
                    line.append(tile.lines[i])
                grid_line.append('  '.join(line))
            grid.append('\n'.join(grid_line))

        return '\n\n'.join(grid)

    def check_wisely(self, pos):
        print('check ', pos)
        for y in range(pos[1] + 1):
            for x in range(pos[0] + 1):
                if x > 0:
                    if self.tiles[y][x].border[3] != self.tiles[y][x - 1].border[1]:
                        return False
                if y > 0:
                    if self.tiles[y][x].border[0] != self.tiles[y - 1][x].border[2]:
                        return False
        return True

    def change_wisely(self, pos):
        element = self.tiles[pos[1]][pos[0]]
        assert isinstance(element, Tile)
        func = choice([element.rotate_clockwise, element.rotate_counter_clockwise,
                       element.flip_left_right, element.flip_upside_down])
        func()

    def get_centers_string(self):
        grid = []
        for tile_line in self.tiles:
            grid_line = []
            for i in range(8):
                line = []
                for tile in tile_line:
                    line.append(tile.center[i])
                grid_line.append(''.join(line))
            grid.append('\n'.join(grid_line))

        return '\n'.join(grid)

    def get_centers_list(self):
        grid = []
        for tile_line in self.tiles:
            grid_line = []
            for i in range(8):
                line = []
                for tile in tile_line:
                    line.append(tile.center[i])
                grid_line.append(''.join(line))
            grid.append(grid_line)

        return grid
