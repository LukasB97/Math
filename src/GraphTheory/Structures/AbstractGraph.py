from abc import ABC, abstractmethod

from src.GraphTheory.Structures.Edge import Edge
from src.GraphTheory.Structures.Node import Node


class AbstractGraph(ABC):

    @abstractmethod
    def add_node(self, node: Node):
        pass

    @abstractmethod
    def remove_node(self, node: Node):
        pass

    @abstractmethod
    def add_edge(self, first_node, second_node):
        pass

    @abstractmethod
    def remove_edge(self, first_node, second_node):
        pass

    @abstractmethod
    def get_neighbors(self, node: Node):
        pass