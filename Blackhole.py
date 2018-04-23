#!/usr/bin/python
import sys, pygame, random, os
assert sys.version_info >= (3,4), 'This script requires at least python 3.4'


screen_size = (400,650)
FPS = 60
black = (0,0,0)
white = (255,255,255)
class Asteroid(pygame.sprite.Sprite):

    def __init__(self, white, size, position, direction):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface(size)
        self.image.fill(white)
        self.rect = self.image.get_rect()
        (self.rect.x,self.rect.y) = position
        self.direction = direction

    def update(self):
        (dx,dy) = self.direction


        self.rect.y += dy
        self.rect.x += dx
        (WIDTH, HEIGHT) = screen_size
        if self.rect.left > WIDTH:
            self.rect.right = 0
        if self.rect.right < 0:
            self.rect.left = WIDTH
        if self.rect.top > HEIGHT:
            self.rect.bottom = 0
        if self.rect.bottom < 0:
            self.rect.top = HEIGHT










class Player(pygame.sprite.Sprite):
    def __init__(self, white, size, position, direction):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface(size)
        self.image.fill(white)
        self.rect = self.image.get_rect()
        (self.rect.x,self.rect.y) = position
        self.direction = direction

    def update_position(self,position):
        (x,y) = position
        (self.rect.x,self.rect.y) = (x,600)


    def update(self):
        pass







def main():
    pygame.init()
    screen = pygame.display.set_mode(screen_size)
    screen_rect = screen.get_rect()
    clock = pygame.time.Clock()
    xblocks =[]
    yblocks = []
    playerpos = []
    block_group = pygame.sprite.Group()
    players = pygame.sprite.Group()
    spritenum = 7
    nohit = True
    z = 0


    s = 0
    font = pygame.font.SysFont('arial', 24)
    score = 0
    pposition = (random.randrange(screen_size[0]), 0)
    pydirection = pygame.mouse.get_pos()
    size = (20, 20)
    player = Player((255, 255, 255), size, pposition, pydirection)
    players.add(player)

    while True:

        while nohit == True:



            pydirection = pygame.mouse.get_pos()
            player.update_position(pydirection)




            while spritenum > 0:
                color = white

                randomposition = (random.randrange(screen_size[0]), 0)
                ydirection = (random.randrange(3,5),random.randrange(3,15))
                size = (20, 20)
                block = Asteroid(color, size, randomposition, ydirection)
                block_group.add(block)





                spritenum -= 1


            xblocks.clear()
            yblocks.clear()
            for b in block_group:

                x_pos = b.rect.x
                xblocks.append(x_pos)


                y_pos = b.rect.y
                yblocks.append(y_pos)





            '''if (player.rect.x in xblocks or player.rect.x + 1 in xblocks or player.rect.x + 2 in xblocks or player.rect.x + 3 in xblocks or player.rect.x + 4 in xblocks or player.rect.x + 5
                or player.rect.x - 1 in xblocks or player.rect.x - 2 in xblocks or player.rect.x - 3 in xblocks or player.rect.x - 4 in xblocks or player.rect.x - 5 in xblocks)\
                and (595 in yblocks or 596 in yblocks or 5910 in yblocks or 598 in yblocks or 599 in yblocks or 600 in yblocks or 601 in yblocks or 602 in yblocks
                or 603 in yblocks or 604 in yblocks or 605 in yblocks):'''


            if xblocks[0]-18 < player.rect.x < xblocks[0]+18 and yblocks[0]-18 < 600 < yblocks[0]+18 or xblocks[0]-18 < player.rect.x < xblocks[0]+18 and yblocks[0]-18 < 600 < yblocks[0]+18 or \
                xblocks[1] - 18 < player.rect.x < xblocks[1] + 18 and yblocks[1] - 18 < 600 < yblocks[1] + 18 or xblocks[1]-18 < player.rect.x < xblocks[1]+18 and yblocks[1]-18 < 600 < yblocks[1]+18 or \
                xblocks[2] - 18 < player.rect.x < xblocks[2] + 18 and yblocks[2] - 18 < 600 < yblocks[2] + 18 or xblocks[2]-18 < player.rect.x < xblocks[2]+18 and yblocks[2]-18 < 600 < yblocks[2]+18 or \
                xblocks[3] - 18 < player.rect.x < xblocks[3] + 18 and yblocks[3] - 18 < 600 < yblocks[3] + 18 or xblocks[3]-18 < player.rect.x < xblocks[3]+18 and yblocks[3]-18 < 600 < yblocks[3]+18 or \
                xblocks[4] - 18 < player.rect.x < xblocks[4] + 18 and yblocks[4] - 18 < 600 < yblocks[4] + 18 or xblocks[4] - 18 < player.rect.x < xblocks[4] + 18 and yblocks[4] - 18 < 600 < yblocks[4] + 18 or \
                xblocks[5] - 18 < player.rect.x < xblocks[5] + 18 and yblocks[5] - 18 < 600 < yblocks[5] + 18 or xblocks[5] - 18 < player.rect.x < xblocks[5] + 18 and yblocks[5] - 18 < 600 < yblocks[5] + 18 or \
                xblocks[6] - 18 < player.rect.x < xblocks[6] + 18 and yblocks[6] - 18 < 600 < yblocks[6] + 18 or xblocks[6] - 18 < player.rect.x < xblocks[6] + 18 and yblocks[6] - 18 < 600 < yblocks[6] + 18:

                    nohit = False


            clock.tick(FPS)
            screen.fill(black)


            text = "Score: {0}".format(score)
            score += 1
            f = font.render(text, True, white)
            (fwidth, fheight) = font.size(text)
            screen.blit(f, (5, 5))


            #print(xblocks, yblocks)
            #print(player.rect.x)


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit(0)
            players.update()
            players.draw(screen)
            block_group.update()
            block_group.draw(screen)
            pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                pressed = pygame.key.get_pressed()
                if pressed[pygame.K_RETURN]:
                    main()
                if pressed[pygame.K_ESCAPE]:
                    pygame.quit()
                    sys.exit(0)
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)

        clock.tick(FPS)
        screen.fill(black)
        atext = '''Game Over | Score: {0}'''.format(score)
        f = font.render(atext, True, white)
        (fwidth, fheight) = font.size(atext)
        screen.blit(f, (113, 300))
        btext = '''Press Enter to Restart | Press Esc to Quit'''
        g = font.render(btext, True, white)
        (fwidth, fheight) = font.size(atext)
        screen.blit(g, (21, 350))
        pygame.display.flip()



if __name__ == '__main__':
    main()
