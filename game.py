from grid import Grid, next_piece_grid, holded_piece_grid
from blocks import *
import random

class Game:
    def __init__(self):
        self.grid = Grid()
        self.holded_grid = holded_piece_grid()
        self.blocks = [LBlock(), JBlock(), ZBlock(), TBlock(), SBlock(), IBlock(), OBlock()]
        self.current_block = self.get_random_block()
        self.next_block = self.get_random_block()
        self.block_is_holded = False
        self.holded_block = None
        self.game_over = False
        self.score = 0
        self.game_speed = 250

    def get_random_block(self):
        if len(self.blocks) == 0:
            self.blocks = [LBlock(), TBlock(), JBlock(), ZBlock(), SBlock(), IBlock(), OBlock()]
        block = random.choice(self.blocks)
        self.blocks.remove(block)
        return block
    
    def block_pos_spawn(self):
        self.current_block.move(0, 4)

    def hold_block(self):
        temp_block = self.current_block
        if self.block_is_holded == False:
            self.block_is_holded = True
            self.holded_block = temp_block
            self.current_block = self.next_block
            self.current_block.back_at_top_middle()
            self.next_block = self.get_random_block()
        elif self.block_is_holded == True:       
            self.current_block = self.holded_block
            self.holded_block = temp_block
            self.current_block.back_at_top_middle()

    def move_left(self):
        self.current_block.move(0, -1)
        if not self.block_inside() or not self.block_fits():
            self.current_block.move(0, 1)

    def move_right(self):
        self.current_block.move(0, 1)
        if not self.block_inside() or not self.block_fits():
            self.current_block.move(0, -1)

    def move_down(self):
        self.current_block.move(1, 0)
        if not self.block_inside() or not self.block_fits():
            self.current_block.move(-1, 0)
            self.lock_block()

    def rotation(self):
        self.current_block.rotate()
        if not self.block_inside() or not self.block_fits():
            self.current_block.undo_rotation()

    def block_fits(self):
        if self.block_inside():
            tiles = self.current_block.get_cell_positions()
            for tile in tiles:
                if not self.grid.is_empty(tile.row, tile.column):
                    return False
            return True
    
    def block_inside(self):
        tiles = self.current_block.get_cell_positions()
        for tile in tiles:
            if not self.grid.is_inside(tile.row, tile.column):
                return False
        return True 
    
    def block_touch_roof(self):
        tiles = self.current_block.get_cell_positions()
        for tile in tiles:
            if tile.row == 0:
                return True
        return False

    def lock_block(self):
        if not self.block_touch_roof():
            tiles = self.current_block.get_cell_positions()
            for position in tiles:
                self.grid.grid[position.row][position.column] = self.current_block.id
            self.current_block = self.next_block
            self.block_pos_spawn()
            self.next_block = self.get_random_block()
            completed = self.grid.check_each_row()
            if completed > 0:
                self.count_points(completed)
        else:
            self.game_over = True

    
    def count_points(self, completed):
        self.score += 100 * completed


    def restart(self):
        self.grid.reset_grid()
        self.blocks = [LBlock(), JBlock(), ZBlock(), TBlock(), SBlock(), IBlock(), OBlock()]
        self.current_block = self.get_random_block()
        self.block_pos_spawn()
        self.next_block = self.get_random_block()
        self.block_is_holded = False
        self.score = 0


    def draw(self, screen, stage_pos_x, stage_pos_y, next_piece_stage_pos_x, next_piece_stage_pos_y, holded_stage_x, holded_stage_y):
        self.grid.draw_grid(screen, stage_pos_x, stage_pos_y)
        self.current_block.draw(screen, stage_pos_x, stage_pos_y)
        self.next_block.draw_next_piece(screen, next_piece_stage_pos_x, next_piece_stage_pos_y)
        if self.block_is_holded == True:
            self.holded_block.draw_holded_piece(screen, holded_stage_x, holded_stage_y)
