from colors import Colors
import pygame as pg
from position import Position
from grid import holded_piece_grid

class Block:
    def __init__(self, id):
        self.id = id
        self.holded_grid = holded_piece_grid()
        self.cells = {}
        self.cell_size = 30
        self.rotation_state = 0
        self.row_offset = 0
        self.column_offset = 0
        self.colors = Colors.get_cell_colors()

    def move(self, rows, columns):
        self.row_offset += rows
        self.column_offset += columns

    def back_at_top_middle(self):
        self.row_offset = 0
        self.column_offset = 4

    def get_cell_positions(self):
        tiles = self.cells[self.rotation_state]
        moved_tiles = []
        for position in tiles:
            moved_tiles.append(
                Position(position.row + self.row_offset, position.column + self.column_offset)
            )
        return moved_tiles
    
    def rotate(self):
        self.rotation_state += 1
        if self.rotation_state > 3:
            self.rotation_state = 0

    def undo_rotation(self):
        self.rotation_state -= 1
        if self.rotation_state < 0:
            self.rotation_state = 3


    def draw(self, screen, stage_pos_x, stage_pos_y):
        tiles = self.get_cell_positions()
        for tile in tiles:
            tile_rect = pg.Rect(
                tile.column * self.cell_size + stage_pos_x + 1, 
                tile.row * self.cell_size + stage_pos_y + 1, 
                self.cell_size - 1, self.cell_size - 1
            )
            pg.draw.rect(screen, self.colors[self.id], tile_rect)

    # For the next block
    # --------------------------------------------------------------------------------------------------------------- #

    def block_pos(self):
        tiles = self.cells[self.rotation_state]
        moved_tiles = []
        for position in tiles:
            moved_tiles.append(
                Position(position.row + 1, position.column + 1)
            )
        return moved_tiles

    
    def draw_next_piece(self, screen, next_stage_pos_x, next_stage_pos_y):
        tiles = self.block_pos()
        for tile in tiles:
            tile_rect = pg.Rect(
                tile.column * self.cell_size + next_stage_pos_x + 1, 
                tile.row * self.cell_size + next_stage_pos_y + 1, 
                self.cell_size - 1, self.cell_size - 1
            )
            pg.draw.rect(screen, self.colors[self.id], tile_rect)

    
    # for the holded block
    # --------------------------------------------------------------------------------------------------------------- #
    
    def draw_holded_piece(self, screen, holded_stage_pos_x, holded_stage_pos_y):
        tiles = self.block_pos()
        for tile in tiles:
            tile_rect = pg.Rect(
                tile.column * self.holded_grid.cell_size + holded_stage_pos_x + 1, 
                tile.row * self.holded_grid.cell_size + holded_stage_pos_y + 1, 
                self.holded_grid.cell_size - 1, self.holded_grid.cell_size - 1
            )
            pg.draw.rect(screen, self.colors[self.id], tile_rect)

    

