import pygame

def movement(player,player_speed,screen_obj, walls):
    screen = screen_obj.get_rect()
    player_last = pygame.Rect.copy(player)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        player.x -= player_speed
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        player.x += player_speed
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        player.y -= player_speed
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        player.y += player_speed
    
    if player.x < 0 or player.x + player.width > screen.width or player.y < 0 or player.y + player.height > screen.height:
        return player_last
    
    for wall in walls:
        if player.colliderect(wall):
            return player_last
    
    return player

    

    

