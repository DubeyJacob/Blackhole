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


def main():
    pygame.init()
    screen = pygame.display.set_mode(screen_size)
    screen_rect = screen.get_rect()
    clock = pygame.time.Clock()

    blocks = pygame.sprite.Group()
    spritenum = 5

    spritenum -= 1
    s = 0


    while True:
        while spritenum > 0:
            color = white

            randomposition = (random.randrange(screen_size[0]), 0)
            ydirection = (0, 10)
            size = (20, 20)
            block = Asteroid(color, size, randomposition, ydirection)
            blocks.add(block)
            spritenum -= 1
        s += 10
        if s == 650:
            spritenum = 1
            s = 0
        print(s)

        clock.tick(FPS)
        screen.fill(black)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
        blocks.update()
        blocks.draw(screen)
        pygame.display.flip()
if __name__ == '__main__':
    main()
