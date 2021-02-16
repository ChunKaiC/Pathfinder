
import pygame
import math
from Node import Node


class Board:
    def __init__(self):
        pygame.init()
        self.program_state = True

        self.window = pygame.display.set_mode((1201, 801))
        pygame.display.set_caption("PathFinder")
        self.clock = pygame.time.Clock()

        self.start = None
        self.end = None
        self.board = [[Node(self.window, (46, 46, 46), i, j) for i in range(0, 1201, 20)]
                      for j in range(0, 801, 20)]
        self.command = None

    def run(self):
        """Run the PathFinder"""
        while self.program_state:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.program_state = False

            index = self.pos_to_index(pygame.mouse.get_pos())
            node = self.board[index[1]][index[0]]

            # Possible optimization: try only drawing coloured nodes, and display a base background
            for row in self.board:
                for node in row:
                    node.draw()
                    node.is_hovering()

            self.draw_grid()
            pygame.display.update()
            self.clock.tick(60)

        pygame.quit()

    def draw_grid(self):
        for i in range(0, 1220, 20):
            pygame.draw.line(self.window, (0, 0, 0), [i, 0], [i, 800])
        for i in range(0, 820, 20):
            pygame.draw.line(self.window, (0, 0, 0), [0, i], [1200, i])

    def pos_to_index(self, pos):
        return math.floor(pos[0] // 20), math.floor(pos[1] // 20)


if __name__ == "__main__":
    board = Board()
    board.run()
    test = [[(i, j) for i in range(0, 1201, 20)] for j in range(0, 801, 20)]
