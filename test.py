import pygame
import os

pygame.init()

display_width = 1000
display_height = 800
window = pygame.display.set_mode((display_width, display_height))

def from_dir(path):
    image_files = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(".png"):
                image_files.append(pygame.image.load(os.path.join(file)))
    return image_files[::-1]

def blit_image(image, surface, x, y):
    return surface.blit(image, (x, y))


def image_generator(img_lst,surface,x,y):
    generator = [blit_image(i, surface, x, y) for i in img_lst]
    yield generator

window.fill((255,0,0))
images = from_dir(".")
image_generator = image_generator(images,window,350,200)
next(image_generator)
pygame.display.update()
