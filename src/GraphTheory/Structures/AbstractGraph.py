from abc import ABC, abstractmethod
from collections import Collection
from typing import Dict, Set

from src.GraphTheory.Structures.Edge import Edge
from src.GraphTheory.Structures.Node import AbstractNode


class AbstractGraph(ABC):

    def __init__(self):
        self.id_to_node = dict()
        self.id_to_edge = dict()
        self.from_to_node_id: Dict[int, Set[int]] = dict()

    @abstractmethod
    def add_node(self, node: AbstractNode):
        pass

    @abstractmethod
    def remove_node(self, node: AbstractNode):
        pass

    @abstractmethod
    def add_edge(self, edge: Edge, first_node: AbstractNode, second_node: AbstractNode):
        pass

    @abstractmethod
    def remove_edge(self, edge: Edge, first_node: AbstractNode, second_node: AbstractNode):
        pass

    @abstractmethod
    def get_neighbors(self, node: AbstractNode):
        pass

    @abstractmethod
    def adjacent(self, *args: Collection[AbstractNode]):
        pass
