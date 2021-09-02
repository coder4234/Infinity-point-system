import pygame

pygame.init()
width, height = (600,600)
screen = pygame.display.set_mode((width, height))

BG_COLOR = (0, 0, 0)
life_point = (200,200,200)
buttonone = (0, 27.84, 67.06)
buttontwo = (87.8, 6.7, 37.3)
FONT = pygame.font.Font("freesansbold.ttf", 50)


def loop():

    clock = pygame.time.Clock()
    number = 4000
    button = pygame.Rect(50, 200, 200, 100)
    button_two = pygame.Rect(350, 200, 200, 100)

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
                        number -= 50
                    if button.collidepoint(event.pos):
                        number += 50
                        
        screen.fill(BG_COLOR)
        pygame.draw.rect(screen, buttonone, button)
        pygame.draw.rect(screen, buttontwo, button_two)
        text_surf = FONT.render(str(number), True, life_point)
        text_rect = text_surf.get_rect(center=(width/2,30))
        screen.blit(text_surf, text_rect)
        pygame.display.update()
        clock.tick(30)


loop()


pygame.quit()