from abc import ABC, abstractmethod

from src.GraphTheory.Structures.Edge import Edge
from src.GraphTheory.Structures.Node import Node


class AbstractGraph(ABC):

    def __init__(self, edge_index=0):
        self._edge_index = edge_index

    def get_new_edge_index(self):
        self._edge_index += 1
        return self._edge_index

    def build_edge(self, edge: Edge = None, first_node: Node = None, second_node: Node = None):
        final_edge = None
        if edge is not None:
            if edge.edge_id is not None:
                return edge
            edge.edge_id = self.get_new_edge_index()
            return edge

    @abstractmethod
    def add_node(self, node: Node):
        pass

    @abstractmethod
    def remove_node(self, node: Node):
        pass

    @abstractmethod
    def add_edge(self, edge, first_node, second_node):
        pass

    @abstractmethod
    def remove_edge(self, edge, first_node, second_node):
        pass

    @abstractmethod
    def get_neighbors(self, node: Node):
        pass
