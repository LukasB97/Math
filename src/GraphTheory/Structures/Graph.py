from typing import Dict, Set

from src.GraphTheory.Structures.AbstractGraph import AbstractGraph
from src.GraphTheory.Structures.Edge import Edge
from src.GraphTheory.Structures.Node import Node


class Graph(AbstractGraph):

    def add_node(self, node: Node):
        self.nodes.add(node)

    def remove_node(self, first_node, second_node):
        self.nodes.remove(node)
        edges = self.node_to_edge_id[node]
        for edge in edges:
            connected_to = edge.get_other_node(node)



    def add_edge(self, edge: Edge):
        self.edges.add(edge)
        for node in edge.nodes:
            self.node_to_edge_id[node].add(self.__edge_id)
        self.__edge_id += 1


    def remove_edge(self, edge: Edge):
        self.edges.remove(edge)
        for node in edge.nodes:
            self.node_to_edge_id[node].remove(edge.id)

    def get_neighbors(self, node: Node):
        pass

    def __init__(self):
        self.__edge_id = 1
        self.nodes = set()
        self.edges = set()
        self.node_to_edge_id: Dict[Node, Set[int]] = dict()

