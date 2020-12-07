import pygame
import math
import random


class lixos(pygame.sprite.Sprite): #classe dos asteróides
    def __init__(self, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load('data/img/naoreciclavel.png')
        self.image = pygame.transform.scale(self.image, [50, 50])
        self.rect = pygame.Rect(50, 50, 100, 100)

        self.rect.x = random.randint(50, 740)
        self.rect.y = random.randint(-50, -50)


        self.speed = 1 + random.random() * 1.3

    def update(self, *args):


        self.rect.y += self.speed

        if self.rect.bottom < 0:
            self.kill()