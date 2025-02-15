import pygame as pg
import colors as c
import level1 as l1
import level2 as l2
pg.init()

screen = pg.display.set_mode((800, 600))

clock = pg.time.Clock()

state = 2

def buildCharacter(x, y):
    return pg.Rect(x, y, 15, 15)

def checkQuit():
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()


def start():
    global state

    start_rect = pg.Rect(300, 350, 150, 50)
    while state == 0:
        checkQuit()
        pg.event.pump()
        screen.fill(c.white)

        pg.draw.rect(screen, c.green, start_rect)

        mx, my = pg.mouse.get_pos()
        keys = pg.key.get_pressed()

        if (start_rect.collidepoint(mx, my)) or keys[pg.K_SPACE]:
            state = 1

        pg.display.flip()
        clock.tick(60)
        
def apply_movement(char, shift):
    keys = pg.key.get_pressed()
    if keys[pg.K_LEFT] or keys[pg.K_a]:
        char.x -= shift
    if keys[pg.K_RIGHT] or keys[pg.K_d]:
        char.x += shift
    if keys[pg.K_UP] or keys[pg.K_w]:
        char.y -= shift
    if keys[pg.K_DOWN] or keys[pg.K_s]:
        char.y += shift
    

def level(level, obj):
    global state

    start_rect = obj.start_rect
    end_rect = obj.end_rect

    char = buildCharacter(start_rect.x, start_rect.y)

    while state == level:
        checkQuit()
        pg.event.pump()
        screen.fill(c.white)

        apply_movement(char, 4)

        for wall in obj.walls:
            if char.colliderect(wall):
                state = -1

        pg.draw.rect(screen, c.orange, start_rect)
        pg.draw.rect(screen, c.green, end_rect)

        for wall in obj.walls:
            pg.draw.rect(screen, c.blue, wall)

        pg.draw.rect(screen, c.red, char)

        pg.display.flip()
        clock.tick(60)

def end():
    global state
    while state == -1:
        checkQuit()
        pg.event.pump()
        screen.fill(c.red)

        keys = pg.key.get_pressed()
        if keys[pg.K_SPACE]:
            state = 0
            pg.time.delay(100)
        pg.display.flip()
        clock.tick(60)

while True:
    checkQuit()
    if state == -1:
        end()
    elif state == 0:
        start()
    elif state == 1:
        level(state, l1)
    elif state == 2:
        level(state, l2)