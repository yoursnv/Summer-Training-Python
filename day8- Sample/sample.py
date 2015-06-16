import pygame, sys

pygame.init()
pygame.mixer.init()
window = pygame.display.set_mode((500, 400))


paintName=pygame.image.load("plane.png")
myMusic = pygame.mixer.Sound("music.ogg")
# name = pygame.font.SysFont("Verdana", 40)
# paintName = name.render("Nitin", 1, (255, 0, 0), (255, 255, 255))

objectSize = paintName.get_size()
frameSpeed = pygame.time.Clock()
x = 300
y = 200

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
        myMusic.stop()
        myMusic.play()

    if y+objectSize[1] >= 400:
        y = 400 - objectSize[1]
        myMusic.stop()
        myMusic.play()

    if x<=0:
        x = 0
        myMusic.stop()
        myMusic.play()
    if y<=0:
        y = 0
        myMusic.stop()
        myMusic.play()


    pygame.display.update()
