import pygame
import math

pi = math.pi

def Create_Star(screen, color, star_x, star_y):

    radius_outer = 7
    radius_inner = 14

    angles_outer = [pi/2, (9/10)*pi, (13/10)*pi, (17/10)*pi, (21/10)*pi]
    angles_inner = [(7/10)*pi, (11/10)*pi, (3/2)*pi, (19/10)*pi, (23/10)*pi]

    points = []

    for i in range(5):
        y = star_y + radius_outer * math.sin(angles_outer[i])
        x = star_x + radius_outer * math.cos(angles_outer[i])
        points.append((x,y))
        y = star_y + radius_inner * math.sin(angles_inner[i])
        x = star_x + radius_inner * math.cos(angles_inner[i])
        points.append((x,y))
    
    pygame.draw.polygon(screen, color, points)

