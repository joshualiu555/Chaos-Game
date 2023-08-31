import pygame
from random import randint

NUM_POINTS = int(input("Enter number of points: "))

pygame.init()
SCREEN = pygame.display.set_mode((1000, 500))
pygame.display.set_caption("Chaos Game Simulation")

c1x = 500
c1y = 100
c2x = 200
c2y = 400
c3x = 800
c3y = 400
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

count = 0
startx = (int(c1x) + int(c2x)) / 2
starty = (int(c1y) + int(c2y)) / 2

def reset():
	global startx, starty, count
	startx = (int(c1x) + int(c2x)) / 2
	starty = (int(c1y) + int(c2y)) / 2
	count = 0
	pygame.draw.circle(SCREEN, WHITE, (int(c1x), int(c1y)), 1)
	pygame.draw.circle(SCREEN, WHITE, (int(c2x), int(c2y)), 1)
	pygame.draw.circle(SCREEN, WHITE, (int(c3x), int(c3y)), 1)
	pygame.draw.circle(SCREEN, WHITE, (int(startx), int(starty)), 1)


reset()
running = True
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	count += 1
	if count == NUM_POINTS:
		SCREEN.fill(BLACK)
		reset()

	# randomly selects one of the three starting points as a pivot
	connecting_point = randint(1, 3)
	# draws a point between the current points and the pivot
	if connecting_point == 1:
		startx = (int(startx) + int(c1x)) / 2
		starty = (int(starty) + int(c1y)) / 2
	elif connecting_point == 2:
		startx = (int(startx) + int(c2x)) / 2
		starty = (int(starty) + int(c2y)) / 2
	else:
		startx = (int(startx) + int(c3x)) / 2
		starty = (int(starty) + int(c3y)) / 2

	pygame.draw.circle(SCREEN, WHITE, (int(startx), int(starty)), 1)

	pygame.display.flip()

pygame.quit()
