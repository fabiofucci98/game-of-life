class Game(object):
    def __init__(self):
        self.grid_height = 34
        self.grid_lenght = 34
        self.is_playing = False

    def set_grid(self, grid):
        self.grid = grid

    def play(self):
        while self.get_number_of_live_cells() != 0:
            self.grid = self.update_grid()
            yield self.grid

    def get_number_of_live_cells(self):
        n = 0
        for i in range(self.grid_height):
            for j in range(self.grid_lenght):
                if self.grid[i][j] == 1:
                    n += 1
        return n

    def change_state(self, i, j, grid):
        alive_neighbours = self.alive_neighbours(i, j)
        if self.grid[i][j] == 1:

            if alive_neighbours < 2:
                grid[i][j] = 0
            elif alive_neighbours > 3:
                grid[i][j] = 0
            else:
                grid[i][j] = 1
        else:
            if alive_neighbours == 3:
                grid[i][j] = 1
        return grid

    def alive_neighbours(self, row, column):
        alive_neighbours = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                try:
                    if self.grid[row+i][column+j] == 1:
                        alive_neighbours += 1

                except:
                    pass
        return alive_neighbours - self.grid[row][column]

    def update_grid(self):
        grid = []
        for i in range(self.grid_height):
            grid.append([])
            for j in range(self.grid_lenght):
                grid[i].append(0)

        for i in range(self.grid_height):
            for j in range(self.grid_lenght):
                grid = self.change_state(i, j, grid)
        return grid
