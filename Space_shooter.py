import pygame
from random import randint
import random
import time
KEY_UP = 273
KEY_DOWN = 274
KEY_LEFT = 276
KEY_RIGHT = 275

class Ball:
    def __init__(self, x, y, speed, radius):
        self.x = x
        self.y = y
        self.speed = speed
        self.radius = radius

    def display(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), (self.x, self.y), self.radius)


    def update(self, width, height):
        self.x = self.x
        self.y += self.speed
        if self.x > width:
            self.x = 0
        if self.y > height:
            self.y = 0
width = 500
height = 500
screen = pygame.display.set_mode((width, height))
bulletgroup = pygame.sprite.Group()
enemygroup = pygame.sprite.Group()
enemybulletgroup = pygame.sprite.Group()
playergroup = pygame.sprite.Group()
class unit(pygame.sprite.Sprite):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        pygame.sprite.Sprite.__init__(self)


class enemyBullet(unit, pygame.sprite.Sprite):
    def __init__(self, x, y):
        unit.__init__(self, x, y)
        self.dead = False
        self.speed = 10
        self.image = pygame.image.load("/Users/mothership/Documents/Tiled_stuff/enemybullet.png")
        self.dead = False
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def display(self):
        self.draw(screen)

class Hero(unit):
    def __init__(self, x, y):
        unit.__init__(self, x, y)
        self.rspeed = 0
        self.lives = 3
        self.lspeed = 0
        self.image = pygame.image.load("/Users/mothership/Documents/Tiled_stuff/myhero.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def display(self):
        self.draw(screen)

class bullet(unit):
    def __init__(self, x, y):
        unit.__init__(self, x, y)
        self.speed = 10
        self.image = pygame.image.load("/Users/mothership/Documents/Tiled_stuff/MyBullet.png")
        self.dead = False
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def display(self):
        self.draw(screen)



class enemy(unit, pygame.sprite.Sprite):
    def __init__(self, x, y):
        unit.__init__(self, x, y)
        self.dead = False
        self.xspeed = 0
        self.yspeed = 0
        self.image = pygame.image.load("/Users/mothership/Documents/Tiled_stuff/MyEnemy.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def display(self):
            screen.blit(self.image, (self.x, self.y))


def main():
    # declare the size of the canvas
    ball_list = []
    width = 500
    height = 500
    blue_color = (0, 0, 0)
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Ball Example')
    bullets = []
    enemybullets = []
    enemy_fighters = []
    rdmbullet = 0
    counter = 60
    screen = pygame.display.set_mode((width, height))
    
    x = 10
    for z in range(0, 200, 80):
        for y in range(0, 450, 80):
            enemy_fighters.append(enemy(y, z))
        
    for i in range(50):
        rndm_y = randint(10, 490)
        rndm_x = randint(10, 490)
        rndm_size = randint(1, 2)
        rndm_spd = randint(1, 3)
        ball_list.append(Ball(rndm_y, rndm_x, rndm_spd, rndm_size))

    player1 = Hero(200, 400)
    playergroup.add(player1)
    # Game initialization
    stop_game = False
    # for i in range(random_int):
    #     random_location = randint(10, 490)
    #     random_size = randint(1, 15)
    #     random_speed = randint(2, 15)
    #     ball_list.append(Ball(random_location, 50, random_speed, random_size))



    while not stop_game:
        for event in pygame.event.get():
            random_int = randint(8, 30)
            if event.type == pygame.KEYDOWN:
                if event.key == KEY_LEFT:
                    player1.lspeed = -4
                elif event.key == KEY_RIGHT:
                    player1.rspeed = 4
                if event.key == KEY_UP:
                    if player1.lives > 0:
                        bullets.append(bullet(player1.rect.x + 28, player1.rect.y + 20))
            if event.type == pygame.KEYUP:
                if event.key == KEY_LEFT:
                    player1.lspeed = 0
                elif event.key == KEY_RIGHT:
                    player1.rspeed = 0

            if event.type == pygame.QUIT:
                # if they closed the window, set stop_game to True
                # to exit the main loop
                stop_game = True
        # Game logic
        counter -= 1

        for ea_bullet in bullets:
            bulletgroup.add(ea_bullet)
            ea_bullet.rect.y -= ea_bullet.speed
            if ea_bullet.y <= -10:
                ea_bullet.dead = True

        for ea_enemy in enemy_fighters:
            
            enemygroup.add(ea_enemy)
            enemyhit = pygame.sprite.spritecollide(ea_enemy, bulletgroup, False)
            if enemyhit:
                for ea_bullet in bullets:
                    bullethit = pygame.sprite.spritecollide(ea_bullet, enemygroup, False)
                    if bullethit:
                        bulletgroup.remove(ea_bullet)
                        del bullets[bullets.index(ea_bullet)]
                enemygroup.remove(ea_enemy)
                del enemy_fighters[enemy_fighters.index(ea_enemy)]
        

        if counter == 0:
            counter = 60
            rdmbullet = randint(1, 5)
            if len(enemy_fighters) > 0:
                for i in range(rdmbullet):
                    rdmindex = randint(0, (len(enemy_fighters) - 1))
                    enemybullets.append(enemyBullet( enemy_fighters[rdmindex].x + 35, enemy_fighters[rdmindex].y + 35))
                rdmbullet = 0

        for ea_bullet in enemybullets:

            if len(enemybullets) > 0:
                hit = pygame.sprite.spritecollide(ea_bullet, playergroup, False)
                if hit:
                    print("hit")
                    player1.lives -= 1
                    enemybulletgroup.remove(ea_bullet)
                    del enemybullets[enemybullets.index(ea_bullet)]
        for ea_enemy in enemy_fighters:
            ea_enemy.y -= ea_enemy.yspeed
            ea_enemy.x -= ea_enemy.xspeed
        
        for ea_bullet in enemybullets:
            enemybulletgroup.add(ea_bullet)
            ea_bullet.rect.y += ea_bullet.speed
            if ea_bullet.y >= width + 10:
                ea_bullet.dead = True

        player1.rect.x += (player1.rspeed + player1.lspeed)

        if player1.rect.x <= -20:
            player1.lspeed = 0
            player1.rect.x = -10
        if player1.rect.x >= (width - 100):
            player1.rspeed = 0
            player1.rect.x = (width - 105)

        for ball in ball_list:
            ball.update(width, height)

        
        
        
        # Draw background
        screen.fill(blue_color)

        # Game display

        for ball in ball_list:
            ball.display(screen)
        if player1.lives > 0:
            playergroup.draw(screen)
        else:
            pass

        # for ea_bullet in bullets:
        #     if not ea_bullet.dead:
        #         ea_bullet.display()
        #     else:
        #         del ea_bullet
        bulletgroup.draw(screen)
        enemybulletgroup.draw(screen)
        enemygroup.draw(screen)
        # for ea_enemy in enemy_fighters:
        #     # if not hit:
        #     #     ea_enemy.display()
        #     if:
        #         del ea_enemy
        pygame.display.update()

    pygame.quit()

if __name__ == '__main__':
    main()
