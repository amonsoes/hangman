import os
import pygame


def from_dir(path):
    image_files = []
    for root,dirs,files in os.walk(path):
        for file in files:
            if file.endswith(".png"):
                image_files.append(pygame.image.load(os.path.join(file)))
    return image_files[::-1]


def blit_image(image,surface,x,y):
    return surface.blit(image,(x,y))

def image_generator(img_lst,surface,x,y):
    generator = [blit_image(i,surface,x,y) for i in img_lst]
    yield generator
    

if __name__ == "__main__":
    images = from_dir(".")
    print(images)
