import pygame

from algoritms import movement
from objects import Create_Star


# Initialize Pygame
pygame.init()

# Window size
WIDTH, HEIGHT = 400, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("White playerangle Example")

# Colors
WHITE = (255, 255, 255)
GREY = (124, 124, 124)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
YELLOW = (255,255,0)

clock = pygame.time.Clock()
FPS = 60

maze = [[1,1,1,1,1,1,1,1,1,1],
        [1,0,0,1,0,0,1,0,0,1],
        [1,0,0,0,0,0,1,0,0,1],
        [1,1,1,0,1,1,1,1,0,1],
        [1,0,0,0,0,0,0,1,0,1],
        [1,1,1,1,1,0,0,1,0,1],
        [0,0,0,1,0,0,0,0,0,1],
        [0,0,0,1,0,0,1,1,0,1],
        [1,0,0,0,0,0,1,0,0,1],
        [1,1,1,1,1,1,1,1,1,1]]
# player properties
player_x = 0
player_y = 300
player_width = 20
player_height = 20
player_speed = 5

#star coordinates
star_x = 60
star_y = 60

walls = []
screen.fill(BLACK)
#Maze builing
for i, row in enumerate(maze):
        for j, collumn in enumerate(row):
            if collumn:
                wall = pygame.Rect(j*(WIDTH/10), i*(HEIGHT/10), (WIDTH/10)-1 , (HEIGHT/10)-1)
                walls.append(wall)

Create_Star(screen, YELLOW, star_x, star_y)

maze_surface = screen.copy() #copies the screen for later use

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player = pygame.Rect(player_x, player_y, player_width, player_height)

    player = movement(player,player_speed,screen, walls)

    player_x, player_y = player.x, player.y
    
    screen.blit(maze_surface, (0,0))

    for i in range(len(walls)):
        pygame.draw.rect(screen, GREY, walls[i])    
    
    pygame.draw.rect(screen, BLUE, player)

 # Update the display
    pygame.display.flip()

    clock.tick(FPS)

# Quit Pygame
pygame.quit()
