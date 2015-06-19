
import pygame, sys
from Colloision.collision import Collision

pygame.init()
pygame.mixer.init()

windowSize = (800, 600)

screen = pygame.display.set_mode(windowSize)

#Adding Resources to the Game
otherObject = pygame.image.load("hey.png")
sound = pygame.mixer.Sound("music.ogg")

collisionText = pygame.font.SysFont("courier",28)

renderText = collisionText.render("Hey I am Intersected", 1 ,(255,255,0),(0,0,0))

otherObjectSize = otherObject.get_size()
otherObject.fill((255,255,255), None, pygame.BLEND_RGBA_MAX)


x,y = 0,0

clock = pygame.time.Clock()
directionX,directionY = 1,1

def playSound():
    sound.stop()
    sound.play()

rectangle = Collision(100,100,400,400)
mario = Collision(0, 0, otherObjectSize[0], otherObjectSize[1])

while True:
    clock.tick(30)
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    captureMouse = pygame.mouse.get_pos()
    x = captureMouse[0]
    y = captureMouse[1]

    mario.setPosition(x,y)

    if mario.intersect(rectangle):
        screen.blit(renderText,(10,10))
        playSound()

    pygame.draw.rect(screen,(255,255,255),(100,100,400,400),1)
    screen.blit(otherObject,(x,y))

    pygame.display.update()