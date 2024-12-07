#snakeTower

import pygame as pg

pg.init()
screen = pg.display.set_mode((1920, 1080))
pg.display.set_caption("snakeTower")
clock = pg.time.Clock()

running = True
while running:
    # Handle events
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    
    # Game logic here
     
    ""# Draw everything
    screen.fill((0, 0, 0))  # Fill screen with black
    pg.display.flip()    # Update the display
    
    clock.tick(60)  # Limit to 60 FPS""

pg.quit()