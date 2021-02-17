import sys
from Command import Command


class DijkstraCommand(Command):

    def __init__(self, board, start_node, end_node):
        super().__init__(board, start_node, end_node)

    def execute(self):
        pass


