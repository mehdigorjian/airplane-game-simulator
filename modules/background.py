from setting import W_WIDTH, W_HEIGHT, IMAGE_BACKGROUND
from pygame import image, transform

class Background:

    def __init__(self, y):
        self.x = 0
        self.y = y
        self.img = transform.scale(image.load(IMAGE_BACKGROUND), (W_WIDTH, W_HEIGHT))
        self.vel = 2
    
    def draw(self, screen):
        screen.blit(self.img, (self.x, self.y))
    
    def move(self):
        self.y += self.vel
        if self.y == W_HEIGHT:
            self.y = - W_HEIGHT
    
