
import pygame
from Node import Node


class Board:
    def __init__(self):
        pygame.init()
        self.window_res = (1200, 800)
        self.node_res = (20, 20)

        self.window = pygame.display.set_mode((self.window_res[0], self.window_res[1]))
        pygame.display.set_caption("PathFinder")
        self.clock = pygame.time.Clock()

        self.start = None
        self.end = None
        self.board = [[Node(self.window, (46, 46, 46), i, j) for i in range(0, self.window_res[0], self.node_res[1])]
                      for j in range(0, self.window_res[1], self.node_res[0])]
        self.command = None
        self.program_state = True

    def run(self):
        """Run the PathFinder"""
        while self.program_state:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.program_state = False

            # Possible optimization: try only drawing coloured nodes, and display a base background
            for row in self.board:
                for node in row:
                    node.is_hovering()
                    node.draw()

            self.draw_grid()
            pygame.display.update()
            self.clock.tick(60)

        pygame.quit()

    def draw_grid(self):
        for i in range(0, 1220, 20):
            pygame.draw.line(self.window, (0, 0, 0), [i, 0], [i, 800])
        for i in range(0, 820, 20):
            pygame.draw.line(self.window, (0, 0, 0), [0, i], [1200, i])


if __name__ == "__main__":
    board = Board()
    board.run()
