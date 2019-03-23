import pygame
import game_logic
import word_processing

pygame.init()
window = pygame.display.set_mode((1000, 800))

def headline(x,y,text,font):
    textSurf,textRect = text_objects(text, font)
    textRect.center = (x,y)
    return window.blit(textSurf,textRect)


def make_button(x_window,y_window,x,y,text,font=pygame.font.Font("freesansbold.ttf",20),color=(0,0,0),hovercolor=(0,0,0)):
    if x_window + x > mouse[0] > x_window and y_window + y > mouse[1] > y_window:
        pygame.draw.rect(window, hovercolor, (x_window, y_window, x, y))
        if click[0] == 1:
            pygame.draw.rect(window, color, (x_window, y_window, x, y))
            game_logic.start_game()

    else:
        pygame.draw.rect(window, color, (x_window,y_window,x,y))

    textSurf,textRect = text_objects(text, font)
    textRect.center = ( (x_window+(x/2)),(y_window+(y/2)))
    return window.blit(textSurf,textRect)


black = (0, 0, 0)
red = (255, 130, 130)
light_red = (255, 200, 200)
blue = (130, 180, 255)
white = (255, 255, 255)


headline_font = pygame.font.Font("freesansbold.ttf",50)
small_font = pygame.font.Font("freesansbold.ttf",20)

pygame.display.set_caption("Welcome to hangman ya douche")

def text_objects(text,font):
    textSurface = font.render(text,True,black)
    return textSurface, textSurface.get_rect()




run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False



    #______start______
    window.fill(blue)
    headline(500,200,"Welcome to Hangman",headline_font)
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    make_button(450,400,100,50,"Start",small_font,red,light_red)
    #_________________




    pygame.display.update()

pygame.quit()