import pygame

class Entity():

    def __init__(self):
        self.__x = 0
        self.__y = 0
        self.__texture = None
        self.__scene = None

    def draw(self, screen, cx, cy):
        pass

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def set_x(self, x):
        self.__x = x

    def set_y(self, y):
        self.__y = y

    def get_rect(self):
        return self.__texture.get_rect()

    def get_scene(self):
        return self.__scene

    def set_scene(self, scene):
        self.__scene = scene

    def set_texture(self, texture):
        self.__texture = texture

    def get_texture(self):
        return self.__texture
