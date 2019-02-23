import pygame
from random import randint
import random
import time

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


class unit(pygame.sprite.Sprite):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        pygame.sprite.Sprite.__init__(self)


class startButton(unit):
    def __init__(self, x, y):
        unit.__init__(self, x, y)
        self.image = pygame.image.load("/Users/mothership/Documents/GitHub/myGame/Space_images/STARTBUTTON.png").convert()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def display(self):
        self.draw(screen)

class gameover(unit):
    def __init__(self, x, y):
        unit.__init__(self, x, y)
        self.image = pygame.image.load("/Users/mothership/Documents/GitHub/myGame/Space_images/GAMEOVER.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def display(self):
        self.draw(screen)

class enemyBullet(unit):
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

class enemies(unit):
    def __init__(self, x, y, health):
        unit.__init__(self, x, y)
        self.dead = False
        self.xspeed = 1
        self.yspeed = 0
        self.life = health

class enemy2(enemies):
    def __init__(self, x, y, health):
        enemies.__init__(self, x, y, health)
        self.image = pygame.image.load("/Users/mothership/Documents/GitHub/myGame/Space_images/enemy2.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class enemy(enemies):
    def __init__(self, x, y, health):
        enemies.__init__(self, x, y, health)
        self.image = pygame.image.load("/Users/mothership/Documents/Tiled_stuff/MyEnemy.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class enemy3(enemies):
    def __init__(self, x, y, health):
        enemies.__init__(self, x, y, health)
        self.image = pygame.image.load("/Users/mothership/Documents/GitHub/myGame/Space_images/enemy3.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


    def display(self):
            screen.blit(self.image, (self.x, self.y))

        # Game initialization

def main():
    # declare the size of the canvas
    pygame.init()
    width = 500
    height = 500
    pygame.display.set_caption('Space Shooter')
    startscreen = pygame.image.load("/Users/mothership/Documents/Github/myGame/Space_images/SpaceShooterStartpage.png")
    screen = pygame.display.set_mode((width, height))
    KEY_UP = 273
    KEY_DOWN = 274
    KEY_LEFT = 276
    KEY_RIGHT = 275
    ball_list = []
    gameoverlist = []
    bullets = []
    enemybullets = []
    enemy_fighters = []
    player_list = []
    startlist = []
    enemyspeed = 1
    level = 0
    counter = 0
    black_color = (0, 0, 0)
    font = pygame.font.Font(None, 30)
    MyStart = startButton(200, 300)
    Mygameover = gameover(0,0)
    screen = pygame.display.set_mode((width, height))
    bulletgroup = pygame.sprite.Group()
    enemygroup = pygame.sprite.Group()
    enemybulletgroup = pygame.sprite.Group()
    playergroup = pygame.sprite.Group()
    gameovergroup = pygame.sprite.Group()
    startgroup = pygame.sprite.Group()
    gameovergroup.add(Mygameover)
    gameoverlist.append(Mygameover)
    startlist.append(MyStart)
    startgroup.add(MyStart)
    screen = pygame.display.set_mode((width, height))
    textblock = font.render("", True, (0, 255, 0))
    



    def level1():
        level = 1
        for z in range(0, 200, 80):
            for y in range(0, 450, 80):
                enemy_fighters.append(enemy(y, z, 1))
        player1 = Hero(200, 400)
        playergroup.add(player1)
        player_list.append(player1)

    def level2():
        for z in range(0, 200, 80):
            for y in range(0, 450, 80):
                enemy_fighters.append(enemy2(y, z, 2))
    
    def level3():
        for z in range(0, 160, 80):
            for y in range (0, 450, 80):
                enemy_fighters.append(enemy3(y, z, 3))

    
    for i in range(100):
        rndm_y = randint(10, 490)
        rndm_x = randint(10, 490)
        rndm_size = randint(1, 2)
        rndm_spd = randint(1, 3)
        ball_list.append(Ball(rndm_y, rndm_x, rndm_spd, rndm_size))




    stop_game = False
    while not stop_game:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
            # Set the x, y postions of the mouse click
                x, y = event.pos
                if len(startlist) > 0:
                    if MyStart.rect.collidepoint(x, y):
                        startgroup.remove(MyStart)
                        level1()
                        level += 1
                        counter = 120
                        del startlist[startlist.index(MyStart)]
            for ea_player in player_list:
                if event.type == pygame.KEYDOWN:
                    if event.key == KEY_LEFT:
                        ea_player.lspeed = -4
                    elif event.key == KEY_RIGHT:
                        ea_player.rspeed = 4
                    if event.key == KEY_UP:
                        if ea_player.lives > 0:
                            bullets.append(bullet(ea_player.rect.x + 28, ea_player.rect.y + 20))
                if event.type == pygame.KEYUP:
                    if event.key == KEY_LEFT:
                        ea_player.lspeed = 0
                    elif event.key == KEY_RIGHT:
                        ea_player.rspeed = 0

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
                ea_enemy.life -= 1
                if ea_enemy.life == 0:
                    enemygroup.remove(ea_enemy)
                    del enemy_fighters[enemy_fighters.index(ea_enemy)]
        

        if counter == 0:
            counter = 90
            rdmbullet = randint(1, 5)
            if len(enemy_fighters) < 8:
                counter = 60
            if len(enemy_fighters) < 5:
                counter = 50
            if len(enemy_fighters) < 2:
                counter = 40
            if len(enemy_fighters) == 1:
                counter = 20
            if len(enemy_fighters) < rdmbullet:
                rdmbullet = randint(0, len(enemy_fighters))
            if len(enemy_fighters) > 0:
                for i in range(rdmbullet):
                    rdmindex = randint(0, (len(enemy_fighters) - 1))
                    if len(enemy_fighters) == 1:
                        rdmindex = 0
                    enemybullets.append(enemyBullet( enemy_fighters[rdmindex].x + 35, enemy_fighters[rdmindex].y + 35))
                rdmbullet = 0

        for ea_bullet in enemybullets:

            if len(enemybullets) > 0:
                for ea_player in player_list:
                    for ea_bullet in enemybullets:
                        if ea_player.lives > 0:
                            hit = pygame.sprite.collide_rect(ea_player, ea_bullet)
                            if hit:
                                ea_player.lives -= 1
                                enemybulletgroup.remove(ea_bullet)
                                del enemybullets[enemybullets.index(ea_bullet)]
                                if ea_player.lives <= 0:
                                    playergroup.remove(ea_player)
                                    del player_list[player_list.index(ea_player)]
        
        # enemy speed settings
        if len(enemy_fighters) == 8:
            enemyspeed = 2
        if len(enemy_fighters) == 4:
            enemyspeed = 4
        if len(enemy_fighters) == 1:
            enemyspeed = 6
        for ea_enemy in enemy_fighters:
            if ea_enemy.x <= -10:
                for ea_enemy in enemy_fighters:
                    ea_enemy.xspeed = -(enemyspeed)
            if ea_enemy.x >= (width - 50):
                for ea_enemy in enemy_fighters:
                    ea_enemy.xspeed = (enemyspeed)
        
        for ea_enemy in enemy_fighters:
            ea_enemy.rect.x -= ea_enemy.xspeed
            ea_enemy.x -= ea_enemy.xspeed
        
        for ea_bullet in enemybullets:
            enemybulletgroup.add(ea_bullet)
            ea_bullet.rect.y += ea_bullet.speed
            if ea_bullet.y >= width + 10:
                ea_bullet.dead = True
        
        # blocks player from leaving
        for ea_player in player_list:
            if ea_player.lives > 0:
                ea_player.rect.x += (ea_player.rspeed + ea_player.lspeed)

            if ea_player.rect.x <= -20:
                ea_player.lspeed = 0
                ea_player.rect.x = -10
            if ea_player.rect.x >= (width - 100):
                ea_player.rspeed = 0
                ea_player.rect.x = (width - 105)

        if len(enemy_fighters) == 0 and level == 1:
            level2()
            level += 1
            counter = 120
            if len(player_list) > 0:
                player_list[0].lives += 1
            enemyspeed = 1
        if len(enemy_fighters) == 0 and level == 2:
            level3()
            level += 1
            counter = 120
            if len(player_list) > 0:
                player_list[0].lives += 1
            enemyspeed = 1
        for ball in ball_list:
            ball.update(width, height)
        
        
        # Draw background
        screen.fill(black_color)
        for ball in ball_list:
            ball.display(screen)

        # Game display

        # background
        
        playergroup.draw(screen)

        if len(startlist) > 0:
            screen.blit(startscreen, (0,0))
        startgroup.draw(screen)

        bulletgroup.draw(screen)
        enemybulletgroup.draw(screen)
        enemygroup.draw(screen)

        if len(player_list) == 0 and len(startlist) == 0:
            gameovergroup.draw(screen)
        if len(player_list) > 0:
            myphrase = ("Lives: %d" % player_list[0].lives)
            textblock = font.render(myphrase, True, (0,255,0))
            screen.blit(textblock,(20,480))
        pygame.display.update()

    pygame.quit()

if __name__ == '__main__':
    main()
