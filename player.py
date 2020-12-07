import pygame

WIDTH = 840
HEIGHT = 480

class nave(pygame.sprite.Sprite): #classe da nave
    def __init__(self, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load('data/img/gari1.png')
        self.image = pygame.transform.scale(self.image, [120, 120])
        self.rect = pygame.Rect(400, 380, 100, 120)

        self.speed = 0
        self.speed1 = 0
        self.acceleration = 0.2
        self.lives = 3
        self.hidden = False
        self.hide_timer = pygame.time.get_ticks()

    def hide(self):
        self.hidden = True
        self.hide_time = pygame.time.get_ticks()
        self.rect.center = (WIDTH / 2, HEIGHT + 200)

    def update(self, *args):

        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.speed -= self.acceleration

        elif keys[pygame.K_d]:
            self.speed += self.acceleration

        #elif keys[pygame.K_w]:
            #self.speed1 -= self.acceleration

        #elif keys[pygame.K_s]:
            #self.speed1 += self.acceleration

        else:
            self.speed *= 0.1
            self.speed1 *= 0.1

        self.rect.x += self.speed
        self.rect.y += self.speed1

        if self.rect.left <0:
            self.rect.left = 0
            self.speed = 0

        elif self.rect.right > 840:
            self.rect.right = 840
            self.speed = 0

        elif self.rect.top < 0:
            self.rect.top = 0
            self.speed1 = 0

        elif self.rect.bottom > 480:
            self.rect.bottom = 480
            self.speed1 = 0

        if self.hidden and pygame.time.get_ticks() - self.hide_timer > 1000:
            self.hidden = False
            self.rect.center = (WIDTH / 2, HEIGHT -20)