#!/usr/bin/python
import sys, pygame, random, os
assert sys.version_info >= (3,4), 'This script requires at least python 3.4'

screen_size = (600,700)
FPS = 60
black = (0,0,0)
white = (255,255,255)
class Block(pygame.sprite.Sprite):
	def __init__(self, white, size, position, direction):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface(size)
		self.image.fill(white)
		self.rect = self.image.get_rect()
		(self.rect.x,self.rect.y) = position
		self.direction = direction

	def update(self):
		(dx,dy) = self.direction
		self.rect.x += dx
		self.rect.y += dy
		(WIDTH,HEIGHT) = screen_size
		if self.rect.left > WIDTH:
			self.rect.right = 0
		if self.rect.right < 0:
			self.rect.left = WIDTH
		if self.rect.top > HEIGHT:
			self.rect.bottom = 0
		if self.rect.bottom < 0:
			self.rect.top = HEIGHT
def main():
    pygame.init()
    screen = pygame.display.set_mode(screen_size)
    screen_rect = screen.get_rect()
    clock = pygame.time.Clock()

    blocks = pygame.sprite.Group()
    spritenum = random.randrange(10)
    while spritenum > 0:
        color = (255,255,255)
        randomposition = (random.randrange(screen_size[0]), random.randrange(screen_size[1]))
        randomdirection = (random.randrange(10), random.randrange(10))
        size = (10,10)
        block = Block(color, size, randomposition, randomdirection)
        blocks.add(block)
        spritenum -= 1
    while True:
        clock.tick(FPS)
        screen.fill(black)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)

if __name__ == '__main__':
    main()
