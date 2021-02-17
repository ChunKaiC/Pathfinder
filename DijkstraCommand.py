import sys
from PathFinder import PathFinder
from Node import Node
from Command import Command


class DijkstraCommand:

    def __init__(self, board, start_node, end_node):
        self.board = board
        self.start_index = start_node
        self.end_index = end_node

        self.memory = {}
        for row in self.board:
            for node in row:
                self.memory[node] = float('inf')
        self.memory[start_node] = 0

    def execute(self):
        pass

    def run(self):
        pass

    def find_distance(self):
        pass

    def find_adjacent_nodes(self):
        pass


if __name__ == "__main__":
    WINDOW_RES = (301, 301)
    NODE_SIZE = 20
    program = PathFinder(WINDOW_RES, NODE_SIZE)
    program.run()



