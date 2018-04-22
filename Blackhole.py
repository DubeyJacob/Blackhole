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

    while nohit == True:



        pydirection = pygame.mouse.get_pos()
        player.update_position(pydirection)




        while spritenum > 0:
            color = white

            randomposition = (random.randrange(screen_size[0]), 0)
            ydirection = (random.randrange(1,5), random.randrange(1,15))
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





        if (player.rect.x in xblocks or player.rect.x + 1 in xblocks or player.rect.x + 2 in xblocks or player.rect.x + 3 in xblocks or player.rect.x + 4 in xblocks or player.rect.x + 5 in xblocks or player.rect.x + 6 in xblocks or player.rect.x +7 in xblocks \
            or player.rect.x + 8 in xblocks or player.rect.x + 10 in xblocks or player.rect.x + 11 in xblocks or player.rect.x + 12 in xblocks or player.rect.x + 13 in xblocks or player.rect.x + 14 in xblocks or player.rect.x + 15 in xblocks \
            or player.rect.x - 1 in xblocks or player.rect.x - 2 in xblocks or player.rect.x - 3 in xblocks or player.rect.x - 4 in xblocks or player.rect.x - 5 in xblocks or player.rect.x - 6 in xblocks or player.rect.x -7 in xblocks \
            or player.rect.x - 8 in xblocks or player.rect.x - 10 in xblocks or player.rect.x - 11 in xblocks or player.rect.x - 12 in xblocks or player.rect.x - 13 in xblocks or player.rect.x - 14 in xblocks or player.rect.x - 15 in xblocks)\
            and (590 in yblocks or 591 in yblocks or 592 in yblocks or 593 in yblocks or 594 in yblocks or 595 in yblocks or 596 in yblocks or 597 in yblocks or 598 in yblocks or 599 in yblocks or 600 in yblocks or 601 in yblocks or 602 in yblocks \
            or 603 in yblocks or 604 in yblocks or 605 in yblocks or 606 in yblocks or 607 in yblocks or 608 in yblocks or 609 in yblocks or 610 in yblocks):

            z += 1

            print(z)



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

if __name__ == '__main__':
    main()
