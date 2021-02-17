
import pygame


class Node:
    def __init__(self, window, colour, x, y, node_size):
        self.window = window
        self.colour = colour
        self.x = x
        self.y = y
        self.node_size = node_size
        self.mutable = True

    def draw(self):
        pygame.draw.rect(self.window, self.colour, [self.x, self.y, self.node_size, self.node_size])

    def event_handler(self):
        pass
