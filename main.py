import pygame as pg

fps = 60
width, height = 800, 600
win = pg.display.set_mode((width, height))
pg.display.set_caption("Brick Breaker")


def draw(win):
    win.fill("WHITE")
    pg.display.update()


def main():
    clock = pg.time.Clock()
    run = 1

    while run:
        clock.tick(fps)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = 0
                break
        draw(win)

    pg.quit()
    quit()


if __name__ == "__main__":
    main()
