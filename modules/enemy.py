from setting import IMAGE_ENEMY
from pygame import image

class Enemy:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.img = image.load(IMAGE_ENEMY)
        self.vel = 3
        self.damage = 10
    
    def draw(self, screen):
        screen.blit(self.img, (self.x, self.y))
    
    def move(self):
        self.y += self.vel
    
    def add_to_list(self, enemy_list):
        enemy_list.append(self)
    
    def remove_from_list(self, enemy_list):
        enemy_list.pop(enemy_list.index(self))