import pygame

pygame.init()


fps = 60
pygame.display.set_caption("Pixels-Legends")

# window :
WW, WH = 800, 400
win = pygame.display.set_mode((WW, WH))


def draw():
    win.fill("WHITE")
    pygame.display.update()


def main():
    clock = pygame.time.Clock()
    run = 1
    while run:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = 0
                pygame.quit()

            draw()


if __name__ == "__main__":
    main()
