import pygame

pygame.init()
screen = pygame.display.set_mode((1920,1080)) #(width, height)
clock = pygame.time.Clock()
running = True
pygame.display.set_caption("Lemmings") #sets window title
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2) 


background_surf = pygame.image.load('Graphics/brick.jpg').convert()

ground_surf = pygame.image.load('Graphics/green.jpg').convert()

player_surf = pygame.image.load('Graphics/blue.jpg').convert()
player_rect = player_surf.get_rect(midbottom = (80,800))


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill('red')

    screen.blit(background_surf, (0,0))
    screen.blit(ground_surf, (0,800))
    screen.blit(player_surf, player_rect)
    player_rect.left += 20
    if player_rect.left > 1920:
        player_rect.right = -40

    #RENDER THE GAME HERE
    

    #flip() seems like it displays whatever I have rendered above to the screen. Is that not what update() does?
    pygame.display.update()

    clock.tick(60) #Limits to 60 FPS

pygame.quit()


#    pygame.draw.circle(screen, "blue", player_pos, 45)

#   keys = pygame.key.get_pressed()
#     if keys[pygame.K_w]:
#         player_pos.y -= 300 * dt
#     if keys[pygame.K_s]:
#         player_pos.y += 300 * dt
#     if keys[pygame.K_a]:
#         player_pos.x -= 300 * dt
#     if keys[pygame.K_d]:
#         player_pos.x += 300 * dt