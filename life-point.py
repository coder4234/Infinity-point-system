import pygame

pygame.init()
width = 600
height = 600
screen = pygame.display.set_mode((width, height))

BG_COLOR = (0, 0, 0)
life_point = (200,200,200)
buttonone = (0, 27.84, 67.06)
buttontwo = (87.8, 6.7, 37.3)
buttonhalf = (20, 139, 58)
FONT = pygame.font.Font("freesansbold.ttf", 50)
# import pygame module in this program
import pygame

# activate the pygame library
# initiate pygame and give permission
# to use pygame's functionality.
pygame.init()

# define the RGB value for white,
# green, blue colour .
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)

# assigning values to X and Y variable
X = 400
Y = 400

# create the display surface object
# of specific dimension..e(X, Y).
display_surface = pygame.display.set_mode((X, Y))

# set the pygame window name
pygame.display.set_caption('Show Text')

# create a font object.
# 1st parameter is the font file
# which is present in pygame.
# 2nd parameter is size of the font
font = pygame.font.Font('freesansbold.ttf', 32)

# create a text surface object,
# on which text is drawn on it.
text = font.render('GeeksForGeeks', True, green, blue)

# create a rectangular object for the
# text surface object
textRect = text.get_rect()

# set the center of the rectangular object.
textRect.center = (X // 2, Y // 2)

# infinite loop
while True:

	# completely fill the surface object
	# with white color
	display_surface.fill(white)

	# copying the text surface object
	# to the display surface object
	# at the center coordinate.
	display_surface.blit(text, textRect)

	# iterate over the list of Event objects
	# that was returned by pygame.event.get() method.
	for event in pygame.event.get():

		# if event object type is QUIT
		# then quitting the pygame
		# and program both.
		if event.type == pygame.QUIT:

			# deactivates the pygame library
			pygame.quit()

			# quit the program.
			quit()

		# Draws the surface object to the screen.
		pygame.display.update()




def loop():

    clock = pygame.time.Clock()
    number = 4000
    button = pygame.Rect(50, 200, 200, 100)
    button_two = pygame.Rect(350, 200, 200, 100)
    button_half = pygame.Rect(200, 340 , 200, 100)

    while number == 0:
        pygame.quit()
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if button_two.collidepoint(event.pos):
                        number -= 100
                    if button.collidepoint(event.pos):
                        number += 100
                    if button_half.collidepoint(event.pos):
                        number -= number / 2


        screen.fill(BG_COLOR)
        pygame.draw.rect(screen, buttonone, button)
        pygame.draw.rect(screen, buttontwo, button_two)
        pygame.draw.rect(screen, buttonhalf, button_half)
        text_surf = FONT.render(str(number), True, life_point)
        text_rect = text_surf.get_rect(center=(width/2,30))
        screen.blit(text_surf, text_rect)
        pygame.display.update()
        clock.tick(30)


loop()


pygame.quit()