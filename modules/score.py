from setting import *
from pygame import draw, Surface, transform, image

class StatusBar:
    def __init__(self):
        self.x = 10
        self.y = W_HEIGHT - 40
        self.w = W_WIDTH - 20
        self.h = 30
        self.color = GRAY
        self.s = Surface((self.w, self.h))
        
    def draw(self, screen, health):
        # draw.rect(screen, self.color, (self.x, self.y,self.w, self.h))
        if health <= 0:
            self.color = RED
        self.s.set_alpha(100)
        self.s.fill(self.color)
        screen.blit(self.s, (10, W_HEIGHT - 40))

class ScoreMeter:
    def __init__(self):
        self.x = 30
        self.y = W_HEIGHT - 35
        self.count = 0
        self.text = SMALL_FONT.render('Score : ' + str(self.count), True, WHITE)
    
    def draw(self, screen):
        screen.blit(self.text, (self.x, self.y))
    
    def increment_count(self, health):
        if health <= 0:
            self.text = SMALL_FONT.render('Score : ' + str(self.count), True, RED)
        else:
            self.count += 1
            self.text = SMALL_FONT.render('Score : ' + str(self.count), True, WHITE)

class HealthBar:
    def __init__(self):
        self.x = W_WIDTH//2 + 30
        self.y = W_HEIGHT - 35
        self.w = 100
        self.h = 17
        self.color = WHITE
        self.inner_color = GREEN
        self.inner_h = self.h
        self.img = transform.scale(image.load(IMAGE_PLAYER), (15,15))
    
    def draw(self, screen, health):
        screen.blit(self.img, (self.x - 20, self.y))
        
        if health <= 0:
            draw.rect(screen, RED, (self.x, self.y, self.w, self.h), 2)
            text = SMALLER_FONT.render(str(0) + ' %', True, RED)
            screen.blit(text, (self.x + 37, self.y + 3))
        else:
            draw.rect(screen, self.inner_color, (self.x, self.y, health, self.inner_h))
            draw.rect(screen, self.color, (self.x, self.y, self.w, self.h), 2)
            text = SMALLER_FONT.render(str(health) + ' %', True, WHITE)
            screen.blit(text, (self.x + 37, self.y + 3))
            if 0 < health <= 40:
                self.inner_color = RED
            elif health <= 70:
                self.inner_color = YELLOW
            elif health <= 100:
                self.inner_color = GREEN