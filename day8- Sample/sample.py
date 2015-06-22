import pygame

BLUE = (0, 0, 255)

screen = pygame.display.set_mode((800, 400))

gameExit = False

while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True

    screen.fill(BLUE)
    pygame.display.update()
