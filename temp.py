import pygame
import math
import time
from Vertex import Vertex


# Draws grid outlines
def draw_grid():
    """Draws grid for the baord according to node_size"""
    for i in range(0, 501 + 20, 50):
        pygame.draw.line(window, (0, 0, 0), [i, 0], [i, 501])
    for i in range(0, 501 + 20, 50):
        pygame.draw.line(window, (0, 0, 0), [0, i], [501, i])

# Get mouse pos to corresponding vertex
def mouse_pos():
  pos = pygame.mouse.get_pos()
  return (pos[0] // 50, pos[1] // 50)

# Colour path from start to end
def light_up_path(current_vertex_pos):
  print("colouring")
  current_vertex = vertex_list[current_vertex_pos[1]][current_vertex_pos[0]]

  while current_vertex.colour != START:
    print("colouring")
    if current_vertex.colour == EXPLORED:
      current_vertex.colour = PATH

    vertex_pred_pos = current_vertex.pred
    current_vertex = vertex_list[vertex_pred_pos[1]][vertex_pred_pos[0]]
  print("done colouring")

pygame.init()
window = pygame.display.set_mode((501, 501))
pygame.display.set_caption("PathFinder")
clock = pygame.time.Clock()
program_state = True
algo_state = False

START = (0, 255, 0)
END = (255, 0, 0)
EXPLORED = (0, 0, 255)
UNEXPLORED = (46, 46, 46)
PATH = (255, 255, 0)
BLOCKADE = (0, 0, 0)

# Init vertex list
vertex_list = []
for i in range(10):
  temp = []
  for j in range(10):
    temp.append(Vertex((j, i), 50, UNEXPLORED, window))
  vertex_list.append(temp)

# Init adjacency list
adjacency_list = {}
for row in vertex_list:
  for vertex in row:
    adjacency_list[vertex.pos] = []
    # Up
    if vertex.pos[1] - 1 >= 0:
      adjacency_list[vertex.pos].append((vertex.pos[0], vertex.pos[1] - 1))
    # Down
    if vertex.pos[1] + 1 <= 9:
      adjacency_list[vertex.pos].append((vertex.pos[0], vertex.pos[1] + 1))
    # Left
    if vertex.pos[0] - 1 >= 0:
      adjacency_list[vertex.pos].append((vertex.pos[0] - 1, vertex.pos[1]))
    # Right
    if vertex.pos[0] + 1 <= 9:
      adjacency_list[vertex.pos].append((vertex.pos[0] + 1, vertex.pos[1]))

# Init BFS
Q = []
# let (0, 0) be start and (9, 9) be end
vertex_list[0][0].colour = START
vertex_list[9][9].colour = END
vertex_list[3][0].colour = BLOCKADE
vertex_list[3][1].colour = BLOCKADE
vertex_list[3][2].colour = BLOCKADE
vertex_list[3][3].colour =  BLOCKADE
vertex_list[3][4].colour =  BLOCKADE
vertex_list[2][4].colour =  BLOCKADE
vertex_list[1][4].colour =  BLOCKADE

vertex_list[7][8].colour =  BLOCKADE
vertex_list[8][8].colour =  BLOCKADE
vertex_list[9][8].colour =  BLOCKADE

vertex_list[5][1].colour =  BLOCKADE
vertex_list[5][2].colour =  BLOCKADE
vertex_list[5][3].colour =  BLOCKADE
vertex_list[5][4].colour =  BLOCKADE
vertex_list[5][5].colour =  BLOCKADE
vertex_list[5][6].colour =  BLOCKADE
vertex_list[5][7].colour =  BLOCKADE
vertex_list[5][8].colour =  BLOCKADE
vertex_list[5][9].colour =  BLOCKADE
vertex_list[6][4].colour =  BLOCKADE
vertex_list[7][4].colour =  BLOCKADE

vertex_list[7][1].colour =  BLOCKADE
vertex_list[8][1].colour =  BLOCKADE
vertex_list[9][1].colour =  BLOCKADE
vertex_list[8][1].colour =  BLOCKADE
vertex_list[9][1].colour =  BLOCKADE
vertex_list[0][1].colour =  BLOCKADE
vertex_list[1][1].colour =  BLOCKADE

vertex_list[2][5].colour =  BLOCKADE
vertex_list[2][6].colour =  BLOCKADE
vertex_list[2][7].colour =  BLOCKADE
vertex_list[2][8].colour =  BLOCKADE

# Enqueue
Q.append(vertex_list[0][0].pos)

# Main loop
while program_state:
    # QUIT
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            program_state = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_s]:
      algo_state = True

    # BFS
    if algo_state:
      #print("Doing algo")
      # Check if Q empty, if so algo done
      if len(Q) != 0:
        current_vertex_pos = Q.pop(0)
        current_vertex = vertex_list[current_vertex_pos[1]][current_vertex_pos[0]]
        # If end is reached
        if current_vertex.colour == END:
          algo_state = False
          light_up_path(current_vertex.pos)

        else:
          for adjacent_vertex_pos in adjacency_list[current_vertex_pos]:
            adjacent_vertex = vertex_list[adjacent_vertex_pos[1]][adjacent_vertex_pos[0]]
            # If end is reached
            if adjacent_vertex.colour == END:
              adjacent_vertex.pred = current_vertex.pos
              algo_state = False
              light_up_path(adjacent_vertex.pos)

            elif adjacent_vertex.colour == UNEXPLORED:
              adjacent_vertex.pred = current_vertex.pos
              adjacent_vertex.colour = EXPLORED
              Q.append(adjacent_vertex_pos)

    # DRAW VERTICES
    for row in vertex_list:
        for vertex in row:
            vertex.draw()

    draw_grid()
    pygame.display.update()
    clock.tick(60)
    time.sleep(.15)

pygame.quit()