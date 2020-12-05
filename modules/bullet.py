from setting import IMAGE_BULLET
from pygame import image, transform

class Bullet:

    def __init__(self, x, y):
        self.x = x + 28
        self.y = y
        b_im = image.load(IMAGE_BULLET)
        self.img = transform.scale(b_im, (b_im.get_width()//4,b_im.get_height()//2))
        self.vel = -10
        self.acc = -0.5
    
    def draw(self, screen):
        screen.blit(self.img, (self.x, self.y))
    
    def move(self):
        self.y += self.vel
        self.vel += self.acc
    
    def add_to_list(self, bullet_list):
        bullet_list.append(self)
    
    def remove_from_list(self, bullet_list):
        bullet_list.pop(bullet_list.index(self))