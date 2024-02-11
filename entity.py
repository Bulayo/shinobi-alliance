import pygame
import random
import spritesheet

class Player():

    def __init__(self, win):
            self.win = win
            self.walk_cycle_image = pygame.image.load("assets/Walk.png").convert_alpha()
            self.walk_cycle = spritesheet.SpriteSheet(self.walk_cycle_image)
            self.frame = []

            for i in range(4):
                self.frame.append(self.walk_cycle.get_image_0(i, 16, 16, 2, "black"))

            for i in range(4):
                self.frame.append(self.walk_cycle.get_image_1(i, 16, 16, 2, "black"))

            for i in range(4):
                self.frame.append(self.walk_cycle.get_image_2(i, 16, 16, 2, "black"))

            for i in range(4):
                self.frame.append(self.walk_cycle.get_image_3(i, 16, 16, 2, "black"))


    def up_animation(self):
        self.win.blit(self.frame[4], (0, 32))
        self.win.blit(self.frame[5], (32, 32))
        self.win.blit(self.frame[6], (64, 32)) 
        self.win.blit(self.frame[7], (98, 32))

    def left_animation(self):
        self.win.blit(self.frame[8], (0, 64))
        self.win.blit(self.frame[9], (32, 64))
        self.win.blit(self.frame[10], (64, 64)) 
        self.win.blit(self.frame[11], (98, 64))

    def down_animation(self):
        self.win.blit(self.frame[0], (0, 0))
        self.win.blit(self.frame[1], (32, 0))
        self.win.blit(self.frame[2], (64, 0)) 
        self.win.blit(self.frame[3], (98, 0))

    def right_animation(self):
        self.win.blit(self.frame[12], (0, 98))
        self.win.blit(self.frame[13], (32, 98))
        self.win.blit(self.frame[14], (64, 98)) 
        self.win.blit(self.frame[15], (98, 98))