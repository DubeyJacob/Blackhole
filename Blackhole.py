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

	def check_on_screen(self, screen_size):
		if self.rect.top > screen_size[1]:
			return False
		return True

def main():
	pygame.init()
	screen = pygame.display.set_mode(screen_size)
	screen_rect = screen.get_rect()
	clock = pygame.time.Clock()
	font = pygame.font.SysFont('arial', 24)

	blocks = pygame.sprite.Group()
	spritenum = 1

	spritenum -= 1
	s = 0
	score = 0


	color = white

	randomposition = (random.randrange(screen_size[0]), 0)
	ydirection = (random.randrange(4, 10), random.randrange(4, 10))
	size = (20, 20)
	block = Asteroid(color, size, randomposition, ydirection)
	blocks.add(block)
	block_list = []
	block_list.append(block)

	while True:
		clock.tick(FPS)
		screen.fill(black)

		for b in block_list:
			if not b.check_on_screen(screen_size):
				b.rect.bottom = 0
				randomposition = (random.randrange(screen_size[0]), 0)
				ydirection = (random.randrange(4, 10), random.randrange(4, 10))
				size = (20, 20)
				block = Asteroid(color, size, randomposition, ydirection)
				blocks.add(block)
				block_list.append(block)

				s += 10
		if s == 650:
			spritenum = 1
			s = 0

		print(s)
		text = "Score: {0}".format(score)
		score += 1
		f = font.render(text, True, white)
		(fwidth, fheight) = font.size(text)
		screen.blit(f, (5,5))

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit(0)
		blocks.update()
		blocks.draw(screen)
		pygame.display.flip()
if __name__ == '__main__':
	main()
