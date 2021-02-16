
import pygame


class Node:
    def __init__(self, window, colour, x, y, w=20, h=20):
        self.window = window
        self.colour = colour
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.mutable = True
        self.hovering = False
        self.is_wall = False

    def draw(self):
        pygame.draw.rect(self.window, self.colour, [self.x, self.y, self.w, self.h])

    def is_hovering(self):

        if self.mutable:

            mouse_pos = pygame.mouse.get_pos()

            if self.x <= mouse_pos[0] <= self.x + self.w and self.y <= mouse_pos[1] <= self.y + self.h:
                # Create start_node
                if pygame.mouse.get_pressed()[0] == 1:
                    self.colour = (0, 255, 0)
                    self.mutable = False

                # Create end_node
                elif pygame.mouse.get_pressed()[2] == 1:
                    self.colour = (255, 0, 0)
                    self.mutable = False
                else:
                    self.colour = (0, 0, 0)
                return True
            else:
                self.colour = (46, 46, 46)
                return False

    def event_handler(self):
        pass
