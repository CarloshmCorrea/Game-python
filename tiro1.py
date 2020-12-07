import pygame
import math
import random


class laser1(pygame.sprite.Sprite): #classe do laser1
    def __init__(self, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load('data/img/pazinha1.png')
        self.image = pygame.transform.scale(self.image, [25, 40])
        self.rect = self.image.get_rect()




        self.speed = 3

    def update(self, *args):

        self.rect.y -= self.speed

        if self.rect.bottom > 480:
            self.kill()