from src.GraphTheory.Structures.AbstractGraph import AbstractGraph
from src.GraphTheory.Structures.Edge import Edge
from src.GraphTheory.Structures.Node import AbstractNode


class Graph(AbstractGraph):

    def adjacent(self, *args: AbstractNode):
        if len(args) == 2:
            return args[0].node_id in self.from_to_node_id[args[1].node_id]

    @staticmethod
    def pairing_function(a, b):
        if a < b:
            c = b
            b = a
            a = c
        return ((a + b) * (a + b + 1) + b) / 2

    def build_edge(self, node_1, node_2):
        edge = Edge([node_1, node_2], self.edge_id)
        self.edge_id += 1
        return edge

    def add_node(self, *args: AbstractNode):
        """
        Removes a node and its edges from the Graph. O(|1|)
        """
        changes_made = False
        for node in args:
            if node.node_id not in self.id_to_node:
                self.id_to_node[node.node_id] = node
                changes_made = True
        return changes_made

    def remove_node(self, *args: AbstractNode):
        """
        Removes a node and its edges from the Graph. O(|E|)
        """
        changes_made = False
        for node in args:
            node_id = node.node_id
            if node_id in self.id_to_node:
                self.id_to_node.remove(node)
                edges = self.from_to_node_id[node_id]
                for edge_id in edges:
                    self.id_to_edge.pop(edge_id)
                changes_made = True
        return changes_made

    def add_edge(self, edge: Edge = None, first_node: AbstractNode = None, second_node: AbstractNode = None):
        if not (edge is None ^ (first_node is second_node is None)):
            raise ValueError("Parameter error")
        if edge is not None:
            first_node = edge.nodes[0]
            second_node = edge.nodes[1]
        else:
            edge = self.build_edge(first_node, second_node)
        self.add_node(first_node, second_node)
        if not self.adjacent(first_node, second_node):
            self.id_to_edge[edge.edge_id] = edge
            self.from_to_node_id[first_node.node_id].add(edge.edge_id)
            self.from_to_node_id[second_node.node_id].add(edge.edge_id)
            return True
        return False

    def remove_edge(self, edge: Edge, first_node: AbstractNode, second_node: AbstractNode):
        if not (edge is None ^ (first_node is second_node is None)):
            raise ValueError("Parameter error")
        # self.edges.remove(edge)
        # for node in edge.nodes:
        #     self.node_to_edge_id[node].remove(edge.id)

    def get_neighbors(self, node: AbstractNode):
        return

    def __init__(self):
        super().__init__()
        self.edge_id = 1
