import pygame, sys

pygame.init()
pygame.mixer.init()

red = (255, 0, 0)
white = (255,255,255)
lol = (155,155,65)

pygame.display.set_caption('Hello Nitin')
window = pygame.display.set_mode((500, 400))

paintName=pygame.image.load("plane.png")

objectSize = paintName.get_size()
frameSpeed = pygame.time.Clock()
x = 0
y = 100

while True:
    frameSpeed.tick(50)
    window.fill((0,0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x -= 25
            if event.key == pygame.K_RIGHT:
                x += 25

            if event.key == pygame.K_UP:
                y -= 25
            if event.key == pygame.K_DOWN:
                y += 25

    window.blit(paintName,(x,y))

    if x+objectSize[0] >= 500:
        x = 500 - objectSize[0]

    if y+objectSize[1] >= 400:
        y = 400 - objectSize[1]

    if x<=0:
        x = 0
    if y<=0:
        y = 0

    pygame.draw.rect(window, red, [400,300,15,200])
    pygame.draw.rect(window, lol, [350,200,15,-200])
    pygame.draw.rect(window, white, [180,200,15,200])


    pygame.display.update()
