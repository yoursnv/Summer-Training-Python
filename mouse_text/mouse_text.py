import pygame, sys

pygame.init()
pygame.mixer.init()
window = pygame.display.set_mode((500, 400))


paintName=pygame.image.load("hi.png")
myMusic = pygame.mixer.Sound("music.ogg")
# name = pygame.font.SysFont("Courier", 40)
# paintName = name.render("DB Mall", 1, (255, 0, 0), (255, 255, 255))

objectSize = paintName.get_size()
frameSpeed = pygame.time.Clock()

while True:
    frameSpeed.tick(50)
    window.fill((0,0,0))

    mouseCoordinates  = pygame.mouse.get_pos()

    x = mouseCoordinates[0]
    y = mouseCoordinates[1]

    if x + objectSize[0]> 500:
       x =  500 - objectSize[0]
       myMusic.stop()
       myMusic.play()
    if y + objectSize[1]> 400:
       y =  400 - objectSize[1]
       myMusic.stop()
       myMusic.play()



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    window.blit(paintName,(x,y))



    pygame.display.update()
