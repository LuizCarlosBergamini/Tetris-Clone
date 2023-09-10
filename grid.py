import pygame as pg
from colors import Colors

# handles the grid that shows the game
class Grid:
    def __init__(self):
        self.num_rows = 20
        self.num_columns = 11
        self.cell_size = 30
        self.grid = [[0 for j in range(self.num_columns)] for i in range(self.num_rows)]
        self.color = self.get_cell_colors()

    def print_grid(self):
        for row in range(self.num_rows):
            for column in range(self.num_columns):
                print(self.grid[row][column], end=' ')
            print()

    def is_inside(self, row, column):
        if row >= 0 and row < self.num_rows and column >= 0 and column < self.num_columns:
            return True
        return False
    
    def is_empty(self, row, column):
        if self.grid[row][column] == 0:
            return True
        return False
    
    def is_row_full(self, row):
        for column in range(self.num_columns):
            if self.grid[row][column] == 0:
                return False
        return True
    
    def delete_row(self, row):
        for column in range(self.num_columns):
            self.grid[row][column] = 0 
    
    def check_each_row(self):
        completed = 0
        for row in range(self.num_rows - 1, 0, -1):
            if self.is_row_full(row):
                self.delete_row(row) 
                completed += 1
            elif completed > 0:
                self.lower_blocks(row, completed)  
        return completed 
    

    def lower_blocks(self, row, num_rows):
        for col in range(self.num_columns):
            self.grid[row + num_rows][col] = self.grid[row][col]
            self.grid[row][col] = 0

    def reset_grid(self):
        for row in range(self.num_rows):
            for column in range(self.num_columns):
                self.grid[row][column] = 0


    def get_cell_colors(self):
        # This function returns a list of 7 colors
        black = ('Black')
        green = ('Green')
        blue = ('Blue')
        yellow = ('Yellow')
        cyan = ('Cyan')
        magenta = ('Magenta')
        orange = ('Orange')
        red = ('Red')

        return [black, green, blue, yellow, cyan, magenta, orange, red]
    
    def draw_grid(self, screen, stage_pos_x, stage_pos_y):
        for row in range(self.num_rows):
            for column in range(self.num_columns):
                # cell value
                cell_value = self.grid[row][column]
                # cell rect
                x = column * self.cell_size + stage_pos_x
                y = row * self.cell_size + stage_pos_y
                cell_rect = pg.Rect(x + 1, y + 1, self.cell_size - 1, self.cell_size - 1)
                pg.draw.rect(screen, self.color[cell_value], cell_rect)


# handles the grid thqat shows the next piece
class next_piece_grid(Grid):
    def __init__(self):
        self.num_rows = 5
        self.num_columns = 5
        self.cell_size = 30
        self.grid = [[0 for j in range(self.num_columns)] for i in range(self.num_rows)]
        self.color = self.get_cell_colors()

    def draw_next_grid(self, screen, next_piece_stage_pos_x, next_piece_stage_pos_y):
        for row in range(self.num_rows):
            for column in range(self.num_columns):
                #cell value
                cell_value = self.grid[row][column]
                x = column * self.cell_size + next_piece_stage_pos_x
                y = row * self.cell_size + next_piece_stage_pos_y
                cell_rect = pg.Rect(x + 1, y + 1, self.cell_size - 1, self.cell_size - 1)
                pg.draw.rect(screen, self.color[cell_value], cell_rect)


class holded_piece_grid(Grid):
    def __init__(self):
        self.num_rows = 5
        self.num_columns = 5
        self.cell_size = 20
        self.grid = [[0 for j in range(self.num_columns)] for i in range(self.num_rows)]
        self.color = self.get_cell_colors()

    
    def draw_holded_grid(self, screen, holded_stage_pos_x, holded_stage_pos_y):
        for row in range(self.num_rows):
            for column in range(self.num_columns):
                #cell value
                cell_value = self.grid[row][column]
                x = column * self.cell_size + holded_stage_pos_x
                y = row * self.cell_size + holded_stage_pos_y
                cell_rect = pg.Rect(x + 1, y + 1, self.cell_size - 1, self.cell_size - 1)
                pg.draw.rect(screen, self.color[cell_value], cell_rect)
        
