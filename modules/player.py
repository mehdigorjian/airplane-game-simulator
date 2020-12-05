from setting import W_WIDTH, W_HEIGHT, IMAGE_PLAYER
from pygame import image, transform

class Player:

    def __init__(self, x):
        self.img = image.load(IMAGE_PLAYER)
        self.img_width = self.img.get_width()
        self.x = x - self.img_width//2
        self.y = W_HEIGHT - 110
        self.vel = 0
        self.health = 100

    def draw(self, screen):
        screen.blit(self.img, (self.x, self.y))

    def move(self):
        if (self.x > 0 or self.vel > 0) and (self.x < W_WIDTH - self.img_width or self.vel < 0):
            self.x += self.vel
        if self.vel > 0:
            self.img = transform.rotate(image.load(IMAGE_PLAYER), -10)
            self.y = W_HEIGHT - 115
        if self.vel < 0:
            self.img = transform.rotate(image.load(IMAGE_PLAYER), 10)
            self.y = W_HEIGHT - 115
        if self.vel == 0:
            self.img = image.load(IMAGE_PLAYER)
            self.y = W_HEIGHT - 110
        
            
