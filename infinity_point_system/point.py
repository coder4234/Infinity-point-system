import pygame

pygame.init()
width, height = (600, 600)
screen = pygame.display.set_mode((width, height))

BG_COLOR = (0, 0, 0)
life_point = (200,200,200)
buttonone = (0, 27.84, 67.06)
buttontwo = (87.8, 6.7, 37.3)
buttonhalf = (0,190,0)
white = (200,200,200)
buttonnextpage = (200,200,200)
green = (0,200,0)
blue = (0,0,200)
FONT = pygame.font.Font("freesansbold.ttf", 50)

def loop():

    clock = pygame.time.Clock()
    done = False
    image = pygame.image.load("infinity_Point.png")
    image_three = pygame.image.load("notice.jpg")
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        screen.blit(image_three, (0,537))
        screen.blit(image, (50,25))
        pygame.display.update()
        clock.tick(30)

loop()

def loop():


    clock = pygame.time.Clock()
    done = False
    image_two = pygame.image.load("Instructions.jpg")

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        
        screen.blit(image_two,(0,0))        
        pygame.display.update()
        clock.tick(30)

loop()

def loop():

    clock = pygame.time.Clock()
    number = 4000
    button_one = pygame.Rect(50, 200, 200, 100)
    button_two = pygame.Rect(350, 200, 200, 100)
    button_half = pygame.Rect(195, 350, 200, 100)
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if button_two.collidepoint(event.pos):
                        number -= 100
                    if button_one.collidepoint(event.pos):
                        number += 100
                    if button_half.collidepoint(event.pos):
                        number /= 2
                        
        screen.fill(BG_COLOR)
        pygame.draw.rect(screen, buttonhalf, button_half)
        pygame.draw.rect(screen, buttonone, button_one)
        pygame.draw.rect(screen, buttontwo, button_two)
        text_surf = FONT.render(str(number), True, life_point)
        text_rect = text_surf.get_rect(center=(width/2,30))
        screen.blit(text_surf, text_rect)
        pygame.display.update()
        clock.tick(30)

loop()



pygame.quit()