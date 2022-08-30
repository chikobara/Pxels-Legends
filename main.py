import pygame as pg

pg.init()


fps = 60

# window :
WW, WH = 800, 400
win = pg.display.set_mode((WW, WH))
pg.display.set_caption("Pixels-Legends")


def draw():
    pass


def main():
    run = 1

    while run:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = 0
                break

    pg.quit()


if __name__ == "__main__":
    main()
