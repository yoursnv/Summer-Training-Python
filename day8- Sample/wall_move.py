import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (50, 50, 255)

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 250


class Player(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()

        # Set height, width
        self.image = pygame.Surface([15, 15])
        self.image.fill(WHITE)

        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x

        # Set speed vector
        self.change_x = 0
        self.change_y = 0
        self.walls = None

    def changespeed(self, x, y):
        """ Change the speed of the player. """
        self.change_x += x
        self.change_y += y

    def update(self):
        """ Update the player position. """
        # Move left/right
        self.rect.x += self.change_x

        # Did this update cause us to hit a wall?
        block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
        for block in block_hit_list:
            # If we are moving right, set our right side to the left side of
            # the item we hit
            if self.change_x > 0:
                self.rect.right = block.rect.left
            else:
                # Otherwise if we are moving left, do the opposite.
                self.rect.left = block.rect.right

        # Move up/down
        self.rect.y += self.change_y

        # Check and see if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
        for block in block_hit_list:

            # Reset our position based on the top/bottom of the object.
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            else:
                self.rect.top = block.rect.bottom


class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(BLUE)

        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x

pygame.init()

screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

pygame.display.set_caption('Pac man')

# List to hold all the sprites
all_sprite_list = pygame.sprite.Group()

wall_list = pygame.sprite.Group()

wall = Wall(0, 0, 10, 600)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(10, 0, 790, 10)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(490, 0, 10, 600)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(0, 240, 790, 10)
wall_list.add(wall)
all_sprite_list.add(wall)





# bricks..!!!

wall = Wall(100, 10, 10, 20)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(400, 28, 100, 10)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(10, 50, 90, 10)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(10, 80, 140, 10)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(10, 180, 300, 10)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(180, 10, 10, 100)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(10, 150, 400, 10)
wall_list.add(wall)
all_sprite_list.add(wall)




# Create the player paddle object
player = Player(50, 50)
player.walls = wall_list

all_sprite_list.add(player)

clock = pygame.time.Clock()

done = False

while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.changespeed(-3, 0)
            elif event.key == pygame.K_RIGHT:
                player.changespeed(3, 0)
            elif event.key == pygame.K_UP:
                player.changespeed(0, -3)
            elif event.key == pygame.K_DOWN:
                player.changespeed(0, 3)

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.changespeed(3, 0)
            elif event.key == pygame.K_RIGHT:
                player.changespeed(-3, 0)
            elif event.key == pygame.K_UP:
                player.changespeed(0, 3)
            elif event.key == pygame.K_DOWN:
                player.changespeed(0, -3)

    all_sprite_list.update()

    screen.fill(BLACK)

    all_sprite_list.draw(screen)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()