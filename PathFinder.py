import pygame
from BFSCommand import BFSCommand
from Vertex import Vertex

START = (0, 255, 0)
END = (255, 0, 0)
EXPLORED = (0, 255, 255)
UNEXPLORED = (46, 46, 46)
PATH = (255, 255, 0)
BLOCKADE = (0, 0, 0)

class PathFinder:
    def __init__(self, res, vertex_dimension):
        pygame.init()
        self.window = pygame.display.set_mode(res)
        pygame.display.set_caption("PathFinder")
        self.res = res
        self.start_pos = None
        self.end_pos = None
        self.vertex_dimension = vertex_dimension
        self.command = None
        self.vertex_list = [[Vertex((j, i), vertex_dimension, UNEXPLORED, self.window) 
                            for j in range(res[0] // vertex_dimension)] 
                            for i in range(res[1] // vertex_dimension)]

    def mouse_pos(self):
        """Return index of vertex being hovered"""
        pos = pygame.mouse.get_pos()
        return (pos[0] // self.vertex_dimension, pos[1] // self.vertex_dimension)

    def draw_vertices(self):
        for row in self.vertex_list:
                for vertex in row:
                    vertex.draw()

    def key_press_events(self):
        # Get key presses and vertex index
        keys = pygame.key.get_pressed()
        pos = self.mouse_pos()

        # Make start
        if keys[pygame.K_1]:
            if self.start_pos == None:
                self.vertex_list[pos[1]][pos[0]].colour = START
                self.start_pos = self.vertex_list[pos[1]][pos[0]].pos
            else: 
                self.vertex_list[self.start_pos[1]][self.start_pos[0]].colour = UNEXPLORED
                self.vertex_list[pos[1]][pos[0]].colour = START
                self.start_pos = self.vertex_list[pos[1]][pos[0]].pos
        # Make end
        if keys[pygame.K_2]:
            if self.end_pos == None:
                self.vertex_list[pos[1]][pos[0]].colour = END
                self.end_pos = self.vertex_list[pos[1]][pos[0]].pos
            else: 
                self.vertex_list[self.end_pos[1]][self.end_pos[0]].colour = UNEXPLORED
                self.vertex_list[pos[1]][pos[0]].colour = END
                self.end_pos = self.vertex_list[pos[1]][pos[0]].pos
        # Make wall
        if keys[pygame.K_3]:
            self.vertex_list[pos[1]][pos[0]].colour = BLOCKADE
        # Start algorithm
        if keys[pygame.K_s]:
            self.command = BFSCommand(self, self.start_pos)
            self.command.execute()
        # Restart
        if keys[pygame.K_r]:
            for row in self.vertex_list:
                for vertex in row:
                    vertex.colour = UNEXPLORED
                    vertex.pred = None

    def run(self):
        # Initialization
        program_state = True
        clock = pygame.time.Clock()

        while program_state:
            # Quit
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    program_state = False
                    
            # Handle key press events
            self.key_press_events()

            # Draw all vertices
            self.draw_vertices()

            pygame.display.update()
            clock.tick(60)

        pygame.quit()

if __name__ == "__main__":
    program = PathFinder((800, 800), 50)
    program.run()