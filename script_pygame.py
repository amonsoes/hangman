import pygame
import random
import game_logic
import word_processing
import time

pygame.init()
window = pygame.display.set_mode((1000, 800))

black = (0, 0, 0)
red = (255, 130, 130)
light_red = (255, 200, 200)
blue = (130, 180, 255)
white = (255, 255, 255)

headline_font = pygame.font.Font("freesansbold.ttf",50)
small_font = pygame.font.Font("freesansbold.ttf",20)

pygame.display.set_caption("Hangman by Amon")

words = word_processing.get_words()
random_word = words[random.randint(0, len(words))]
enumerated_word = word_processing.enum_word(random_word)
display_word = word_processing.display_word(random_word)


run = True
start = True
main = True
win = False


print(random_word,enumerated_word,display_word)


def headline(x, y, text, font):
    textSurf,textRect = text_objects(text, font)
    textRect.center = (x, y)
    return window.blit(textSurf, textRect)


def start_button(x_window, y_window, x, y, text, font=pygame.font.Font("freesansbold.ttf", 20), color=(0, 0, 0), hovercolor=(0, 0, 0)):
    global start
    if x_window + x > mouse[0] > x_window and y_window + y > mouse[1] > y_window:
        pygame.draw.rect(window, hovercolor, (x_window, y_window, x, y))
        if click[0] == 1:
            pygame.draw.rect(window, color, (x_window, y_window, x, y))
            start = False
    else:
        pygame.draw.rect(window, color, (x_window, y_window, x, y))

    return text_render(text,font,(x_window+(x/2)),(y_window+(y/2)))


def text_objects(text,font):
    textSurface = font.render(text,True,black)
    return textSurface, textSurface.get_rect()


def text_render(text,font,x,y):
    textSurf,textRect = text_objects(text,font)
    textRect.center = (x,y)
    return window.blit(textSurf,textRect)


def game():
    global main
    global win
    global display_word
    global run
    guesses = 8
    while guesses != 0:
        if win:
            break
        eventhandler()
        window.fill(blue)
        text_render(" ".join(display_word.values()), headline_font, 500, 700)
        text_render("The word has {} letters.".format(len(random_word)), small_font, 500, 750)
        text_render("Guesses left: {}".format(guesses),small_font,200,750)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key not in [i for i in range(97,122)]:
                text_render("no digits and other funny stuff, obviously...",small_font,500,100)
                guesses -= 1
            else:
                if " ".join(display_word.values()) == " ".join(enumerated_word.values()):
                    win = True
                elif event.type == pygame.KEYDOWN and event.key in [i for i in range(97,122)]:
                    if chr(event.key) in enumerated_word.values():
                        for index, char in enumerated_word.items():
                            if event.key == ord(char):
                                display_word[index] = char
                    elif chr(event.key) not in enumerated_word.values():
                        guesses -= 1
    window.fill(blue)
    if win == True:
        text_render("You won!", headline_font, 500, 400)
        main = False
    else:
        text_render("You lost!", headline_font, 500, 400)
        main = False
    pygame.display.update()



def eventhandler():
    global run
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


while run:
    eventhandler()

    # ______start______

    while start:
        eventhandler()
        print("start loop")
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        window.fill(blue)
        headline(500, 200, "Welcome to Hangman", headline_font)
        start_button(450, 400, 100, 50, "Start", small_font, red, light_red)
        pygame.display.update()

    #_________________

    #_______main______

    while main:
        #print("main loop")
        eventhandler()
        game()
        pygame.display.update()

    #__________________


    pygame.display.update()

pygame.quit()