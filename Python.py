import pygame

pygame.init()
screen = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()
running = True
pygame.display.set_caption("lemmings") #sets window title

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2) 

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    

    screen.fill("red")

    pygame.draw.circle(screen, "blue", player_pos, 50)

    #RENDER THE GAME HERE
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        print("W is being pressed")
        player_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        print("S is being pressed")
        player_pos.y +=300 * dt
    if keys[pygame.K_a]:
        print("A is being pressed")
        player_pos.x -= 300 *dt
    if keys[pygame.K_d]:
        print("D is being pressed")
        player_pos.x += 300 * dt

    #flip() seems like it displays whatever I have rendered above to the screen. Is that not what update() does?
    pygame.display.update()

    dt = clock.tick(60) / 1000
    #clock.tick(60) #Limits to 60 FPS

pygame.quit()