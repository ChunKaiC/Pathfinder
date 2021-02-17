
import pygame
import math
from Node import Node


class PathFinder:
    def __init__(self, window_res, node_size):
        """Initialize the pygame, window, clock, and the board"""
        pygame.init()
        self.program_state = True
        self.window_res = window_res
        self.node_size = node_size

        self.window = pygame.display.set_mode(window_res)
        pygame.display.set_caption("PathFinder")
        self.clock = pygame.time.Clock()

        self.start = None
        self.end = None
        self.walls = []
        self.board = [[Node(self.window, (46, 46, 46), i, j, node_size) for i in range(0, window_res[0], node_size)]
                      for j in range(0, window_res[1], node_size)]
        self.command = None

    def run(self):
        """Run the PathFinder"""
        while self.program_state:
            self.window.fill((46, 46, 46))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.program_state = False

            index = self.pos_to_index(pygame.mouse.get_pos())
            curr_node = self.board[index[1]][index[0]]

            inputs = pygame.key.get_pressed()

            # Resets the board
            if inputs[pygame.K_r]:
                self.reset_board()

            # Create start point
            if inputs[pygame.K_1]:
                if self.start is None and curr_node.mutable:
                    self.start = curr_node
                    curr_node.colour = (255, 0, 0)

            # Create end point
            if inputs[pygame.K_2]:
                if self.end is None and curr_node.mutable:
                    self.end = curr_node
                    curr_node.colour = (0, 255, 0)

            # Create walls
            if inputs[pygame.K_3]:
                if curr_node.mutable:
                    self.walls.append(curr_node)
                    curr_node.colour = (0, 0, 0)

            # Possible optimization: try only drawing coloured nodes, and display a base background
            for row in self.board:
                for curr_node in row:
                    curr_node.draw()

            self.draw_grid()
            self.window.blit(self.update_fps(), (10, 0))
            pygame.display.update()
            self.clock.tick(60)

        pygame.quit()

    def draw_grid(self):
        """Draws grid for the baord according to node_size"""
        for i in range(0, self.window_res[0] + 20, self.node_size):
            pygame.draw.line(self.window, (0, 0, 0), [i, 0], [i, self.window_res[1]])
        for i in range(0, self.window_res[1] + 20, self.node_size):
            pygame.draw.line(self.window, (0, 0, 0), [0, i], [self.window_res[0], i])

    def pos_to_index(self, pos):
        """Converts mouse coordinate to the index of the node"""
        return math.floor(pos[0] // 20), math.floor(pos[1] // 20)

    def reset_board(self):
        """Resets the board"""
        self.start = None
        self.end = None
        self.board = [[Node(self.window, (46, 46, 46), i, j, self.node_size)
                       for i in range(0, self.window_res[0], self.node_size)]
                      for j in range(0, self.window_res[1], self.node_size)]

    def update_fps(self):
        """Updates FPS to be displayed"""
        font = pygame.font.SysFont("Arial", 18)
        fps = str(int(self.clock.get_fps()))
        fps_text = font.render(fps, 1, pygame.Color("cyan"))
        return fps_text


if __name__ == "__main__":
    WINDOW_RES = (1201, 801)
    NODE_SIZE = 20
    program = PathFinder(WINDOW_RES, NODE_SIZE)
    program.run()
