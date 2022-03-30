import pygame

class Vertex:
    def __init__(self, pos, dimension, colour, window):
        self.pos = pos
        self.dimension = dimension 
        self.rect = pygame.Rect(pos[0] * dimension, pos[1] * dimension, dimension, dimension)
        self.colour = colour
        self.pred = None
        self.window = window

    def draw(self):
        pygame.draw.rect(self.window, self.colour, self.rect)
        pygame.draw.rect(self.window, (0, 0, 0), self.rect, 1)