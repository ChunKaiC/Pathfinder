
# Interface
class Command:
    def __init__(self, board, start_node, end_node):
        self.board = board
        self.start_node = start_node
        self.end_node = end_node

    def execute(self):
        pass
