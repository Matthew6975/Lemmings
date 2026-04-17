import pygame

pygame.init()
screen = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("red")

    #RENDER THE GAME HERE

    #flip() seems like it displays whatever I have rendered above to the screen
    pygame.display.flip()

    clock.tick(60) #Limits to 60 FPS

pygame.quit()