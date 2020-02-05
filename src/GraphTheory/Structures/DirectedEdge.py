from src.GraphTheory.Structures.Edge import Edge


class DirectedEdge(Edge):

    def __init__(self, from_node, to_node):
        super().__init__([from_node, to_node])

    @property
    def start(self):
        return self.nodes[0]

    @property
    def end(self):
        return self.nodes[1]
