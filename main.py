from setting import *
import pygame
from modules.player import Player
from modules.background import Background
from modules.bullet import Bullet
from modules.enemy import Enemy
from modules.score import *
import random, math

# -------------------------------------------------SCREEN DEFENITION
win = pygame.display.set_mode((W_WIDTH,W_HEIGHT))
title = pygame.display.set_caption(TITLE)

# -------------------------------------------------INIT OBJECTS
player = Player(W_WIDTH//2)
backgrounds = [Background(0), Background(- W_HEIGHT)]
bullets, enemies = [], []
status_bar = StatusBar()
score_meter = ScoreMeter()
health_bar = HealthBar()
# -------------------------------------------------CONTROL FUNCS
def player_control():
    player.draw(win)
    player.move()

def bullet_control():
    for bul in bullets:
        bul.draw(win)
        bul.move()
        if bul.y < 0: bul.remove_from_list(bullets)

def enemy_control():
    if len(enemies) == 0: Enemy(random.randint(0, W_WIDTH-64),random.randint(-100,0)).add_to_list(enemies) 
    if len(enemies) < ENEMY_COUNT:
        enemy = Enemy(random.randint(0, W_WIDTH-64),random.randint(-100,0))
        xS, yS = [], []
        for e in enemies:
            xS.append(e.x)
            yS.append(e.y)
        if min(xS) > 64 and min(yS) > 64:
            enemy.add_to_list(enemies)
        
    for enm in enemies:
        enm.draw(win)
        enm.move()

        if enm.y > W_HEIGHT:
            enm.remove_from_list(enemies)

        if math.dist((player.x,player.y),(enm.x,enm.y)) < 40:
            if enm in enemies:
                enm.remove_from_list(enemies)
                player.health -= enm.damage
                score_meter.increment_count(player.health)

        for b in bullets:
            if math.dist((enm.x,enm.y),(b.x,b.y)) < 35:
                if enm in enemies:
                    enm.remove_from_list(enemies)
                    score_meter.increment_count(player.health)
                b.remove_from_list(bullets)

def background_control():
    for b in backgrounds:
        b.draw(win)
        b.move()

# -------------------------------------------------REDRAW FUNC
def redraw():
    win.fill((0,0,0))
    # ****************control functions here
    background_control()
    bullet_control()
    enemy_control()
    player_control()
    status_bar.draw(win, player.health)
    score_meter.draw(win)
    health_bar.draw(win, player.health)

    # ****************end of control functions
    pygame.display.update()

# -------------------------------------------------MAIN FUNC
def main_loop():
    clock = pygame.time.Clock()
    action = True
    while action:
        for event in pygame.event.get():
            # window terminating event
            if event.type == pygame.QUIT:
                action = False
            # player move
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.vel = - VEL_ADD
                if event.key == pygame.K_RIGHT:
                    player.vel = VEL_ADD
                if event.key == pygame.K_SPACE:
                    # bullet = Bullet(player.x, player.y)
                    # bullet.add_to_list(bullets)
                    bullet1 = Bullet(player.x-10, player.y)
                    bullet2 = Bullet(player.x+10, player.y)
                    bullet1.add_to_list(bullets)
                    bullet2.add_to_list(bullets)
            # stoping infinite move
            if event.type == pygame.KEYUP:
                # if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player.vel = 0
        # setting the frame rate      
        clock.tick(60)
        redraw()
main_loop()