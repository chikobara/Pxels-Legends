import pygame as pg

fps = 60
WIDTH, HEIGHT = 800, 600
win = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Brick Breaker")
PADDLE_WIDTH = 40
PADDLE_HEIGHT = 10


class Paddle:
    VEL = 5

    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

    def draw(self, win):
        pg.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))


def draw(win):
    win.fill("WHITE")
    pg.display.update()


def main():
    clock = pg.time.Clock()
    run = 1
    paddle = Paddle(WIDTH / 2, HEIGHT / 2)

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
