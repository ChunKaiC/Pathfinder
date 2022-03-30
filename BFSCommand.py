import pygame
import time
from Vertex import Vertex

START = (0, 255, 0)
END = (255, 0, 0)
EXPLORED = (0, 255, 255)
UNEXPLORED = (46, 46, 46)
PATH = (255, 255, 0)
BLOCKADE = (0, 0, 0)

class BFSCommand:
    def __init__(self, pathfinder, start_pos):
        """Initialization"""
        self.pathfinder = pathfinder
        self.start_pos = start_pos

    def light_up_path(self, pos):
        """Light up the shortest path from start to end"""
        # Starting vertex
        current_vertex = self.pathfinder.vertex_list[pos[1]][pos[0]]
        while current_vertex.colour != START:
            if current_vertex.colour == EXPLORED:
                current_vertex.colour = PATH
            vertex_pred_pos = current_vertex.pred
            current_vertex = self.pathfinder.vertex_list[vertex_pred_pos[1]][vertex_pred_pos[0]]
    
    def execute(self):
        """Perfornm the algorithm"""
         # Init program state
        algo_state = True
        clock = pygame.time.Clock()

        # Init queue
        Q = []
        Q.append(self.start_pos)

        # Init adjacency list
        adjacency_list = {}
        for row in self.pathfinder.vertex_list:
            for vertex in row:
                adjacency_list[vertex.pos] = []
                # Up
                if vertex.pos[1] - 1 >= 0:
                    adjacency_list[vertex.pos].append((vertex.pos[0], vertex.pos[1] - 1))
                # Down
                if vertex.pos[1] + 1 <= self.pathfinder.res[1] // self.pathfinder.vertex_dimension - 1:
                    adjacency_list[vertex.pos].append((vertex.pos[0], vertex.pos[1] + 1))
                # Left
                if vertex.pos[0] - 1 >= 0:
                    adjacency_list[vertex.pos].append((vertex.pos[0] - 1, vertex.pos[1]))
                # Right
                if vertex.pos[0] + 1 <= self.pathfinder.res[0] // self.pathfinder.vertex_dimension - 1:
                    adjacency_list[vertex.pos].append((vertex.pos[0] + 1, vertex.pos[1]))

        while algo_state:
            # Quit
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

            if len(Q) != 0:
                current_vertex_pos = Q.pop(0)
                current_vertex = self.pathfinder.vertex_list[current_vertex_pos[1]][current_vertex_pos[0]]
                # If end is reached
                if current_vertex.colour == END:
                    algo_state = False
                    self.light_up_path(current_vertex.pos)
                else:
                    for adjacent_vertex_pos in adjacency_list[current_vertex_pos]:
                        adjacent_vertex = self.pathfinder.vertex_list[adjacent_vertex_pos[1]][adjacent_vertex_pos[0]]
                        # If end is reached
                        if adjacent_vertex.colour == END:
                            adjacent_vertex.pred = current_vertex.pos
                            algo_state = False
                            self.light_up_path(adjacent_vertex.pos)
                        elif adjacent_vertex.colour == UNEXPLORED:
                            adjacent_vertex.pred = current_vertex.pos
                            adjacent_vertex.colour = EXPLORED
                            Q.append(adjacent_vertex_pos)
            else: 
                algo_state = False

            # Draw all vertices
            self.pathfinder.draw_vertices()
            pygame.display.update()
            time.sleep(0.025)