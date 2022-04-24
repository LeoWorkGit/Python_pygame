from os import walk
import pygame


def import_folder(path):
    surface_list = []
    for _, __, img_files in walk(path):
        for image in img_files:
            full_path = path + '/' + image
            img = pygame.image.load(full_path).convert_alpha()
            surface_list.append(img)

    return surface_list
