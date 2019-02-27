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
        self.image = pygame.image.load("./Space_images/STARTBUTTON.png").convert()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def display(self):
        self.draw(screen)

class RetryButton(unit):
    def __init__(self, x, y):
        unit.__init__(self,x, y)
        self.image = pygame.image.load("./Space_images/TRYAGAIN.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def display(self):
        self.draw(screen)


class gameover(unit):
    def __init__(self, x, y):
        unit.__init__(self, x, y)
        self.image = pygame.image.load("./Space_images/GAMEOVER.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def display(self):
        self.draw(screen)

class playerWIN(unit):
    def __init__(self, x, y):
        unit.__init__(self, x, y)
        self.image = pygame.image.load("./Space_images/WIN.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def display(self):
        self.draw(screen)

class PlayAgainButton(unit):
    def __init__(self, x, y):
        unit.__init__(self,x, y)
        self.image = pygame.image.load("./Space_images/PLAYAGAIN.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def display(self):
        self.draw(screen)

class enemyBullet(unit):
    def __init__(self, x, y):
        unit.__init__(self, x, y)
        self.dead = False
        self.speed = 8
        self.image = pygame.image.load("./Space_images/enemybullet.png")
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
        self.image = pygame.image.load("./Space_images/myhero.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def display(self):
        self.draw(screen)

class bullet(unit):
    def __init__(self, x, y):
        unit.__init__(self, x, y)
        self.speed = 10
        self.image = pygame.image.load("./Space_images/MyBullet.png")
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
        self.image = pygame.image.load("./Space_images/Enemies/enemy2.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class enemy(enemies):
    def __init__(self, x, y, health):
        enemies.__init__(self, x, y, health)
        self.image = pygame.image.load("./Space_images/Enemies/MyEnemy.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class enemy3(enemies):
    def __init__(self, x, y, health):
        enemies.__init__(self, x, y, health)
        self.image = pygame.image.load("./Space_images/Enemies/enemyBlack3.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class enemy4(enemies):
    def __init__(self, x, y, health):
        enemies.__init__(self, x, y, health)
        self.image = pygame.image.load("./Space_images/Enemies/enemyRed2.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class enemy5(enemies):
    def __init__(self, x, y, health):
        enemies.__init__(self, x, y, health)
        self.image = pygame.image.load("./Space_images/Enemies/enemyBlue4.png")
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
    startscreen = pygame.image.load("./Space_images/SpaceShooterStartpage.png")
    screen = pygame.display.set_mode((width, height))
    WINscreen = pygame.image.load("./Space_images/WIN.png")
    
    # creating lists for each type of instance
    ball_list = []
    gameoverlist = []
    bullets = []
    enemybullets = []
    enemy_fighters = []
    player_list = []
    startlist = []
    retrylist = []
    playerWIN_list = []
    PLAY_AGAIN_list = []

    # initializing variables
    KEY_UP = 273
    KEY_DOWN = 274
    KEY_LEFT = 276
    KEY_RIGHT = 275
    enemyspeed = 1
    level = 0
    counter = 0
    reset = 0
    black_color = (0, 0, 0)
    font = pygame.font.Font(None, 30)

    # initializing instances of classes
    MyStart = startButton(200, 300)
    MyRetry = RetryButton(150, 300)
    Mygameover = gameover(0,0)
    MyWIN = playerWIN(0,0)
    MyPlayAgain = PlayAgainButton(150, 300)
    screen = pygame.display.set_mode((width, height))

    # sprite groups
    bulletgroup = pygame.sprite.Group()
    enemygroup = pygame.sprite.Group()
    enemybulletgroup = pygame.sprite.Group()
    playergroup = pygame.sprite.Group()
    gameovergroup = pygame.sprite.Group()
    startgroup = pygame.sprite.Group()
    retrygroup = pygame.sprite.Group()
    playerWINgroup = pygame.sprite.Group()
    PlayAgainGroup = pygame.sprite.Group()

    # adding instances to lists and groups
    playerWINgroup.add(MyWIN)
    playerWIN_list.append(MyWIN)
    gameovergroup.add(Mygameover)
    gameoverlist.append(Mygameover)
    startgroup.add(MyStart)
    startlist.append(MyStart)

    screen = pygame.display.set_mode((width, height))
    textblock = font.render("", True, (0, 255, 0))
    

    # level/difficulty setup
    def level1():
        level = 1
        for z in range(0, 200, 80):
            for y in range(0, 400, 80):
                enemy_fighters.append(enemy(y, z, 1))

        # initialize player 1
        player1 = Hero(200, 430)
        playergroup.add(player1)
        player_list.append(player1)

    def level2():
        for z in range(0, 200, 80):
            for y in range(0, 400, 100):
                enemy_fighters.append(enemy2(y, z, 2))
    
    def level3():
        for z in range(0, 160, 80):
            for y in range (0, 440, 110):
                enemy_fighters.append(enemy3(y, z, 3))

    def level4():
        for z in range(0, 240, 80):
            for y in range (0, 440, 110):
                enemy_fighters.append(enemy4(y, z, 3))

    def level5():
        for z in range(0, 200, 100):
            for y in range (0, 440, 110):
                enemy_fighters.append(enemy5(y, z, 5))

    
    # random star backgroundk generation
    for i in range(100):
        rndm_y = randint(10, 490)
        rndm_x = randint(10, 490)
        rndm_size = randint(1, 2)
        rndm_spd = randint(1, 3)
        ball_list.append(Ball(rndm_y, rndm_x, rndm_spd, rndm_size))




    stop_game = False
    while not stop_game:
        for event in pygame.event.get():
            
            # event handling for mouse clicks
            if event.type == pygame.MOUSEBUTTONDOWN:
            
            # Set the x, y postions of the mouse click
                x, y = event.pos

                # start button
                if len(startlist) > 0:
                    if MyStart.rect.collidepoint(x, y):
                        startgroup.remove(MyStart)
                        level1()
                        level += 1
                        counter = 120
                        del startlist[startlist.index(MyStart)]
                
                # retry button
                if len(retrylist) > 0:
                    if MyRetry.rect.collidepoint(x, y):
                        retrygroup.remove(MyRetry)
                        retrylist.pop()
                        reset = 1

                # play again button
                if len(PLAY_AGAIN_list) > 0:
                    if MyPlayAgain.rect.collidepoint(x, y):
                        PlayAgainGroup.remove(MyPlayAgain)
                        PLAY_AGAIN_list.pop()
                        reset = 1

            # event handling for player controls
            for ea_player in player_list:
                if event.type == pygame.KEYDOWN:
                    if event.key == KEY_LEFT:
                        ea_player.lspeed = -4
                    elif event.key == KEY_RIGHT:
                        ea_player.rspeed = 4
                    elif event.key == KEY_UP:
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

        # game reset - for play again, and retry button
        if reset == 1:
            for ea_enemy in enemy_fighters:
                enemygroup.remove(ea_enemy)
            enemy_fighters = []
            player_list = []
            playergroup = pygame.sprite.Group()
            level = 1
            counter = 120
            enemyspeed = 1
            level1()
            reset = 0


        # player 1 bullet movement
        for ea_bullet in bullets:
            bulletgroup.add(ea_bullet)
            ea_bullet.rect.y -= ea_bullet.speed
            if ea_bullet.y <= -10:
                ea_bullet.dead = True

        # enemy bullet movement
        for ea_bullet in enemybullets:
            enemybulletgroup.add(ea_bullet)
            ea_bullet.rect.y += ea_bullet.speed
            if ea_bullet.y >= height + 10:
                enemybulletgroup.add(ea_bullet)
                del enemybullets[enemybullets.index(ea_bullet)]
        
        # player 1 bullet to enemy hit detection
        for ea_enemy in enemy_fighters:
            enemygroup.add(ea_enemy)
            enemyhit = pygame.sprite.spritecollide(ea_enemy, bulletgroup, False)
            if enemyhit:
                for ea_bullet in bullets:
                    bullethit = pygame.sprite.spritecollide(ea_bullet, enemygroup, False)
                    
                    # if the bullet hits, delete the bullet
                    if bullethit:
                        bulletgroup.remove(ea_bullet)
                        del bullets[bullets.index(ea_bullet)]
                
                # if the bullet hits, take 1 away from enemy life/health
                ea_enemy.life -= 1
                
                # if the enemy has no life, delete the enemy
                if ea_enemy.life == 0:
                    enemygroup.remove(ea_enemy)
                    del enemy_fighters[enemy_fighters.index(ea_enemy)]

        # random enemy bullet generator
        if counter == 0:

            # random amount of bullets within a range
            rdmbullet = randint(1, 5)
            # check that enemies are still alive
            if len(enemy_fighters) > 0:

                # check the amount of bullets vs the amount of enemies alive
                if len(enemy_fighters) < rdmbullet:

                    # if there are more bullets than enemies
                    # reset the bullet amount to a max of the amount of enemies available
                    rdmbullet = randint(1, len(enemy_fighters))
                
                # for each bullet that we want to create
                for i in range(rdmbullet):

                    # select a random index in the enemy_fighters list
                    rdmindex = randint(0, (len(enemy_fighters) -1))

                    # assign a bullet at the location of the randomly selected enemy
                    enemybullets.append(enemyBullet( enemy_fighters[rdmindex].x + 35, enemy_fighters[rdmindex].y + 35))
                # after the for-loop, reset the rdmbullet amount to 0
                rdmbullet = 0
            
            # alter how often enemies shoot as they die
            counter = 90
            if len(enemy_fighters) < 8:
                counter = 60
            if len(enemy_fighters) < 5:
                counter = 50
            if len(enemy_fighters) < 2:
                counter = 40
            if len(enemy_fighters) == 1:
                counter = 20
        
        # hit detection for enemy bullets to player 1

        # if enemy bullets exist
        if len(enemybullets) > 0:

            # for each player
            for ea_player in player_list:

                # for each bullet
                for ea_bullet in enemybullets:

                    # if a player is still alive
                    if ea_player.lives > 0:

                        # hit = True if a player and an enemy bullet collide
                        hit = pygame.sprite.collide_rect(ea_player, ea_bullet)

                        # if hit/True
                        if hit:

                            # remove a player life
                            ea_player.lives -= 1

                            # delete enemy bullet
                            enemybulletgroup.remove(ea_bullet)
                            del enemybullets[enemybullets.index(ea_bullet)]

                            # if player has no lives
                            if ea_player.lives <= 0:

                                # delete player
                                playergroup.remove(ea_player)
                                del player_list[player_list.index(ea_player)]
        
        # enemy speed settings

        # if there are 8 enemies left
        if len(enemy_fighters) == 8:
            for ea_enemy in enemy_fighters:

                # change the enemy speed to 2
                enemyspeed = 2
                if ea_enemy.xspeed > 0:
                    ea_enemy.xspeed = enemyspeed
                else:
                    ea_enemy.xspeed = -(enemyspeed)
        
        # if there are 6 enemies left
        elif len(enemy_fighters) == 6:
            for ea_enemy in enemy_fighters:

                # change the enemy speed to 3
                enemyspeed = 3
                if ea_enemy.xspeed > 0:
                    ea_enemy.xspeed = enemyspeed
                else:
                    ea_enemy.xspeed = -(enemyspeed)
        
        # if there are 4 enemies left
        elif len(enemy_fighters) == 4:
            for ea_enemy in enemy_fighters:

                # change the enemy speed to 4
                enemyspeed = 4
                if ea_enemy.xspeed > 0:
                    ea_enemy.xspeed = enemyspeed
                else:
                    ea_enemy.xspeed = -(enemyspeed)
        
        # if there are 2 enemies left
        elif len(enemy_fighters) == 2:
            for ea_enemy in enemy_fighters:

                # change the enemy speed to 5
                enemyspeed = 5
                if ea_enemy.xspeed > 0:
                    ea_enemy.xspeed = enemyspeed
                else:
                    ea_enemy.xspeed = -(enemyspeed)

        # if there is 1 enemy left
        elif len(enemy_fighters) == 1:
            for ea_enemy in enemy_fighters:

                # change the enemy speed to 6
                enemyspeed = 6
                if ea_enemy.xspeed > 0:
                    ea_enemy.xspeed = enemyspeed
                if ea_enemy.xspeed < 0:
                    ea_enemy.xspeed = -(enemyspeed)
        
        # enemy direction change
        for ea_enemy in enemy_fighters:
            
            # if a single enemy touches the left wall
            if ea_enemy.x <= -10:

                # change every enemies direction
                for ea_enemy in enemy_fighters:
                    ea_enemy.xspeed = -(enemyspeed)
                    ea_enemy.x += 1
                    ea_enemy.rect.x += 1

                    # move each enemy down 6 pixels
                    ea_enemy.y += 6
                    ea_enemy.rect.y += 6

                    # if there is only 1 enemy,
                    # move the enemy down an extra 6 pixels
                    if len(enemy_fighters) == 1:
                        ea_enemy.y += 6
                        ea_enemy.rect.y += 6 
    
            # if a single enemy touches the right wall
            if ea_enemy.x >= (width - 40):

                # change every enemies direction
                for ea_enemy in enemy_fighters:
                    ea_enemy.xspeed = (enemyspeed)
                    ea_enemy.x -= 1
                    ea_enemy.rect.x -= 1

                    # move each enemy down 6 pixels
                    ea_enemy.y += 6
                    ea_enemy.rect.y += 6

                    # if there is only 1 enemy,
                    # move the enemy down an extra 6 pixels
                    if len(enemy_fighters) == 1:
                        ea_enemy.y += 6
                        ea_enemy.rect.y += 6 
        
        # for each frame, move each enemy by their set speed.
        for ea_enemy in enemy_fighters:
            ea_enemy.rect.x -= ea_enemy.xspeed
            ea_enemy.x -= ea_enemy.xspeed
        

        # player movement and movement block
        for ea_player in player_list:

            # if a player is alive
            if ea_player.lives > 0:

                # move the player, by the set speeds.
                ea_player.rect.x += (ea_player.rspeed + ea_player.lspeed)

            # if the player touches the left side
            if ea_player.rect.x <= -20:

                # stop the player from moving further
                ea_player.lspeed = 0
                ea_player.rect.x = -10
            
            # if the player touches the right side
            if ea_player.rect.x >= (width - 100):

                # stop the player from moving further
                ea_player.rspeed = 0
                ea_player.rect.x = (width - 105)


        # level initializer
        if len(enemy_fighters) == 0 and level == 1:
            enemygroup = pygame.sprite.Group()
            bulletgroup = pygame.sprite.Group()
            enemybulletgroup = pygame.sprite.Group()
            enemybullets = []
            bullets = []
            enemyspeed = 1
            level2()
            level += 1
            counter = 120
            if len(player_list) > 0:
                player_list[0].lives += 1
        
        if len(enemy_fighters) == 0 and level == 2:
            enemygroup = pygame.sprite.Group()
            bulletgroup = pygame.sprite.Group()
            enemybulletgroup = pygame.sprite.Group()
            enemybullets = []
            bullets = []
            enemyspeed = 1
            level3()
            level += 1
            counter = 120
            if len(player_list) > 0:
                player_list[0].lives += 1
        
        if len(enemy_fighters) == 0 and level == 3:
            enemygroup = pygame.sprite.Group()
            bulletgroup = pygame.sprite.Group()
            enemybulletgroup = pygame.sprite.Group()
            enemybullets = []
            bullets = []
            enemyspeed = 1
            level4()
            level += 1
            counter = 120
            if len(player_list) > 0:
                player_list[0].lives += 1
        
        if len(enemy_fighters) == 0 and level == 4:
            enemygroup = pygame.sprite.Group()
            bulletgroup = pygame.sprite.Group()
            enemybulletgroup = pygame.sprite.Group()
            enemybullets = []
            bullets = []
            enemyspeed = 1
            level5()
            level += 1
            counter = 120
            if len(player_list) > 0:
                player_list[0].lives += 1
        
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
            retrygroup.draw(screen)

            retrygroup.add(MyRetry)
            retrylist.append(MyRetry)

        if len(enemy_fighters) == 0 and level == 5:
            playerWINgroup.draw(screen)
            PlayAgainGroup.add(MyPlayAgain)
            PLAY_AGAIN_list.append(MyPlayAgain)
            PlayAgainGroup.draw(screen)

        if len(player_list) > 0:
            myphrase = ("Lives: %d" % player_list[0].lives)
            textblock = font.render(myphrase, True, (0,255,0))
            screen.blit(textblock,(20,480))
        pygame.display.update()

    pygame.quit()

if __name__ == '__main__':
    main()
