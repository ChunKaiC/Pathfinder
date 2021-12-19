import pygame
import math
from Node import Node

pygame.init()
window = pygame.display.set_mode((501, 501))
pygame.display.set_caption("PathFinder")
clock = pygame.time.Clock()

program_state = True
algo_state = True
queue = []

# 5x5 matrix
# Add a vertex to the dictionary
def add_vertex(v):
  global graph
  global vertices_no
  if v in graph:
    print("Vertex ", v, " already exists.")
  else:
    vertices_no = vertices_no + 1
    graph[v] = []

# Add an edge between vertex v1 and v2 with edge weight e
def add_edge(v1, v2, e):
  global graph
  # Check if vertex v1 is a valid vertex
  if v1 not in graph:
    print("Vertex ", v1, " does not exist.")
  # Check if vertex v2 is a valid vertex
  elif v2 not in graph:
    print("Vertex ", v2, " does not exist.")
  else:
    # Since this code is not restricted to a directed or 
    # an undirected graph, an edge between v1 v2 does not
    # imply that an edge exists between v2 and v1
    temp = [v2, e]
    graph[v1].append(temp)

# Print the graph
def print_graph():
  global graph
  for vertex in graph:
    for edges in graph[vertex]:
      print(vertex, " -> ", edges[0], " edge weight: ", edges[1])

# driver code
graph = {}
# stores the number of vertices in the graph
vertices_no = 0
add_vertex(1)
add_vertex(2)
add_vertex(3)
add_vertex(4)
# Add the edges between the vertices by specifying
# the from and to vertex along with the edge weights.
add_edge(1, 2, 1)
add_edge(1, 3, 1)
add_edge(2, 3, 3)
add_edge(3, 4, 4)
add_edge(4, 1, 5)
print_graph()
# Reminder: the second element of each list inside the dictionary
# denotes the edge weight.
print ("Internal representation: ", graph)

node_list = [[Node(window, (46, 46, 46), i, j, 100) for i in range(0, 501, 100)] for j in range(0, 501, 100)]

def draw_grid():
    """Draws grid for the baord according to node_size"""
    for i in range(0, 501 + 20, 100):
        pygame.draw.line(window, (0, 0, 0), [i, 0], [i, 501])
    for i in range(0, 501 + 20, 100):
        pygame.draw.line(window, (0, 0, 0), [0, i], [501, i])

while program_state:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            program_state = False

    for row in node_list:
        for curr_node in row:
            curr_node.draw()

    if algo_state:
        pass

    draw_grid()
    pygame.display.update()
    clock.tick(60)

pygame.quit()