from typing import Dict, Set

from src.GraphTheory.Structures.AbstractGraph import AbstractGraph
from src.GraphTheory.Structures.Edge import Edge
from src.GraphTheory.Structures.Node import AbstractNode


class Graph(AbstractGraph):

    def pairing_function(self, a, b):
        if a < b:
            c = b
            b = a
            a = c
        return ((a + b) * (a + b + 1) + b) / 2

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
            if node.node_id in self.id_to_node:
                self.id_to_node.remove(node)
                edges = self.node_id_to_edge_id[node]
                for edge_id in edges:
                    self.edges.pop(edge_id)
                changes_made = True
        return changes_made

    def add_edge(self, edge: Edge = None, first_node: Node = None, second_node: Node = None):
        if not (edge is None ^ (first_node is second_node is None)):
            raise ValueError("Parameter error")
        if edge is not None:
            first_node = edge.nodes[0]
            second_node = edge.nodes[1]
        self.add_node(first_node, second_node)

        self.edges.add(edge)
        for node in edge.nodes:
            self.node_to_edge_id[node].add(self.__edge_id)
        self.__edge_id += 1

    def remove_edge(self, edge: Edge, first_node, second_node):
        if not (edge is None ^ (first_node is second_node is None)):
            raise ValueError("Parameter error")
        self.edges.remove(edge)
        for node in edge.nodes:
            self.node_to_edge_id[node].remove(edge.id)

    def get_neighbors(self, node: AbstractNode):
        edge_ids = self.node_id_to_edge_id[node.id]
        return

    def __init__(self):
        self.__edge_id = 1
        self.__node_id = 1
        self.id_to_node: Dict[int, AbstractNode] = dict()
        self.id_to_edge: Dict[int, Edge] = dict()
        self.node_id_to_node_id: Dict[int, Set[int]] = dict()
