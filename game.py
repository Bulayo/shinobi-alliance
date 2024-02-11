import pygame
import random
import entity
import spritesheet

pygame.init()

WIDTH, HEIGHT = 700, 550
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Shinobi Alliace")
clock = pygame.time.Clock()
FPS = 60
#pygame.display.set_icon()

#walk_cycle_image = pygame.image.load("assets/Walk.png").convert_alpha()
#walk_cycle = spritesheet.SpriteSheet(walk_cycle_image)
#frame = []

#for i in range(4):
 #   frame.append(walk_cycle.get_image(i, 16, 16, 2, "black"))

player = entity.Player(WIN)



running = True
while running:

    WIN.fill((50, 50, 50))
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player.up_animation()
    player.left_animation()
    player.right_animation()
    player.down_animation()    
    
    pygame.display.flip()

pygame.quit()