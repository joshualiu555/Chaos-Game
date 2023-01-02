"""
This program is a simulation of the chaos game, a popular topic in chaos theory and fractal theory. 
It generates the Sierpinski Triangle using random points. 
To learn more about this, watch this YouTube video by Numberphile
https://www.youtube.com/watch?v=kbKtFN71Lfs
"""

# import modules
import pygame, time, random

# input settings
num_points = int(input("Enter number of points: "))
fps = int(input("Enter frame rate: "))

# initializes pygame
pygame.init()
screen = pygame.display.set_mode((1000, 1000))
pygame.display.set_caption("Chaos Game Simulation")
clock = pygame.time.Clock()

# variables
coordinate_one_x = 500
coordinate_one_y = 30
coordinate_two_x = 200
coordinate_two_y = 370
coordinate_three_x = 800
coordinate_three_y = 370
white = (255, 255, 255)
black = (0, 0, 0)
# program loop
running = True
while running:
	# checks for events
	clock.tick(fps)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	# resets screen
	screen.fill(black)

	# draws original triangle
	pygame.draw.circle(screen, white, (int(coordinate_one_x), int(coordinate_one_y)), 1)
	pygame.draw.circle(screen, white, (int(coordinate_two_x), int(coordinate_two_y)), 1)
	pygame.draw.circle(screen, white, (int(coordinate_three_x), int(coordinate_three_y)), 1)

	# generates each point
	start_point_x = (int(coordinate_one_x) + int(coordinate_two_x)) / 2
	start_point_y = (int(coordinate_one_y) + int(coordinate_two_y)) / 2
	pygame.draw.circle(screen, white, (int(start_point_x), int(start_point_y)), 1)
	for i in range(num_points):
		# randomly generates which point the previous point connects to
		connecting_point = random.randint(1, 3)
		if connecting_point == 1:
			start_point_x = (int(start_point_x) + int(coordinate_one_x)) / 2
			start_point_y = (int(start_point_y) + int(coordinate_one_y)) / 2
		elif connecting_point == 2:
			start_point_x = (int(start_point_x) + int(coordinate_two_x)) / 2
			start_point_y = (int(start_point_y) + int(coordinate_two_y)) / 2
		else:
			start_point_x = (int(start_point_x) + int(coordinate_three_x)) / 2
			start_point_y = (int(start_point_y) + int(coordinate_three_y)) / 2

		# maintains approximate fps
		time.sleep(0.5 / fps)
		# draws the next point
		pygame.draw.circle(screen, white, (int(start_point_x), int(start_point_y)), 1)

		# updates screen
		pygame.display.flip()

# quits the program
pygame.quit()
