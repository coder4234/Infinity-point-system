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
buttonnextpage = (200,0,0)
green = (0,200,0)
blue = (0,0,200)
FONT = pygame.font.Font("freesansbold.ttf", 50)

def loop():

    buttonnextpage = (200,0,0)
    button_next_page = pygame.Rect(508,550,80,30)
    buttonnextpagetwo = (0,0,200)
    button_next_page_two = pygame.Rect(265,550,80,30)
    clock = pygame.time.Clock()
    done = False
    image = pygame.image.load("infinity_Point.png")
    image_two = pygame.image.load("Instructions.jpg")
    button_one = pygame.Rect(50, 200, 200, 100)
    button_two = pygame.Rect(350, 200, 200, 100)
    button_half = pygame.Rect(195, 350, 200, 100)
    number = 4000



    screen.blit(image,(45,40))
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if button_next_page_two.collidepoint(event.pos):
                        screen.fill(BG_COLOR)
                        screen.blit(image_two,(45,0))
                    if button_next_page.collidepoint(event.pos):
                        

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
                    
                        



        pygame.draw.rect(screen,buttonnextpagetwo, button_next_page_two)
        pygame.draw.rect(screen,buttonnextpage, button_next_page)
        pygame.display.update()
        clock.tick(30)

loop()


pygame.quit()