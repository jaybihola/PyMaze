import pygame as pg

start_rect = pg.Rect(25, 25, 25, 25)
end_rect = pg.Rect(735, 535, 25, 25)

walls = [
    # Outer boundary
    pg.Rect(0, 0, 800, 15),
    pg.Rect(0, 0, 15, 600),
    pg.Rect(785, 0, 15, 600),
    pg.Rect(0, 585, 800, 15),

    # Inner walls for the maze
    pg.Rect(15, 100, 110, 15),
    pg.Rect(200, 15, 15, 100),
    pg.Rect(300, 15, 15, 200),
    pg.Rect(100, 200, 200, 15),
    pg.Rect(100, 200, 15, 150),
    pg.Rect(15, 400, 200, 15),
    pg.Rect(200, 350, 15, 150),
    pg.Rect(300, 300, 15, 200),
    pg.Rect(200, 500, 250, 15),
    pg.Rect(450, 300, 15, 215),
    pg.Rect(350, 300, 100, 15),
    pg.Rect(350, 100, 15, 215),
    pg.Rect(400, 100, 200, 15),
    pg.Rect(400, 200, 15, 115),
    pg.Rect(500, 200, 15, 115),
    pg.Rect(600, 100, 15, 200),
    pg.Rect(500, 400, 200, 15),
    pg.Rect(600, 300, 200, 15),
    pg.Rect(700, 100, 15, 215),
    pg.Rect(650, 400, 15, 175),
    pg.Rect(700, 500, 100, 15),
]
