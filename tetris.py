import pygame as pg
from game import Game

pg.init()
screen = pg.display.set_mode((600, 800))
pg.display.set_caption("Tetris")
clock = pg.time.Clock()

dark_blue = (44, 44, 127)

#create a rectangle that is centralized in the screen
stage = pg.Rect(50, 100, 331, 601)
next_piece_stage = pg.Rect(405, 100, 150, 150)
score = pg.Rect(405, 450, 150, 40)
holded_stage = pg.Rect(405, 270, 100, 100)

# Game instance
game = Game()

# Track player actions
held_keys = []
rotation_state = 0

MOVE_EVENT = pg.USEREVENT
pg.time.set_timer(MOVE_EVENT, game.game_speed)



def main():
    global held_keys, rotation_state
    running = True
    # Spawn block in a random position
    game.block_pos_spawn()
    
    while running:
        clock.tick(60)
        screen.fill(dark_blue)

        # quits the game
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            if event.type == pg.KEYDOWN:
                if game.game_over == True:
                    game.game_over = False
                    game.restart()
                if event.key == pg.K_LEFT:
                    game.move_left()
                if event.key == pg.K_RIGHT:
                    game.move_right()
                if event.key == pg.K_DOWN:
                    held_keys.append('down')
                if event.key == pg.K_SPACE:
                    game.rotation()
                if event.key == pg.K_f:
                    game.hold_block()
                if event.key == pg.K_ESCAPE:
                    game.restart()
            if event.type == MOVE_EVENT:
                # Moves block down
                game.move_down()

            elif event.type == pg.KEYUP:
                if event.key == pg.K_DOWN:
                    held_keys.remove('down')

        # draw the title
        T = title_font(font_size=50).render('T', True, 'Red')
        E = title_font(font_size=50).render('E', True, 'Orange')
        T2 = title_font(font_size=50).render('T', True, 'Yellow')
        R = title_font(font_size=50).render('R', True, 'Green')
        I = title_font(font_size=50).render('I', True, 'Blue')
        S = title_font(font_size=50).render('S', True, 'Purple')
        screen.blit(T, (stage.x + 60, stage.y - 80))
        screen.blit(E, (stage.x + 100, stage.y - 80))
        screen.blit(T2, (stage.x + 140, stage.y - 80))
        screen.blit(R, (stage.x + 180, stage.y - 80))
        screen.blit(I, (stage.x + 220, stage.y - 80))
        screen.blit(S, (stage.x + 238, stage.y - 80))

        # draw the score
        pg.draw.rect(screen, 'Black', score)
        score_title = title_font(font_size=15).render('SCORE:', True, 'White')
        score_text = title_font(font_size=15).render(f'{game.score}', True, 'White')
        screen.blit(score_title, (score.x + 5, score.y - 30))
        screen.blit(score_text, (score.x + 5, score.y + 6))
        
        # draw the stage where game will be played
        pg.draw.rect(screen, 'White', stage)
        # draw the stage where the next piece will be shown
        pg.draw.rect(screen, 'Black', next_piece_stage)
        # draw the stage where the holded piece will be shown
        pg.draw.rect(screen, 'Black', holded_stage)

        # draws the game        
        game.draw(screen, stage.x, stage.y, next_piece_stage.x, next_piece_stage.y, holded_stage.x, holded_stage.y)
        
        # draw the game over
        game_over = title_font(font_size=30).render('GAME OVER', True, 'White')
        restart = title_font(font_size=15).render('Press any key to restart', True, 'White')
        if game.game_over == True:
            screen.blit(game_over, (stage.x + 26, stage.y + 250))
            screen.blit(restart, (stage.x + 20, stage.y + 300))

        # moves the block by inputs of player
        moves_block()
        

        # updates the screen
        pg.display.update()
                    
    pg.quit()

def title_font(font_size):
    title_font = pg.font.Font('modern-tetris.ttf', font_size)
    return title_font


def moves_block():
    global held_keys
    for i in held_keys:
        if i == 'down':
            game.move_down()


    

main()