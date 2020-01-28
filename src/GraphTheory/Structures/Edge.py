from collections import Hashable
from typing import Set, Collection

from src.GraphTheory.Structures.Node import Node


class Edge(Hashable):


    def __hash__(self) -> int:
        return hash(self.nodes)

    def __init__(self, nodes: Collection[Node]):
        if len(nodes) != 2:
            raise ValueError("Number of nodes does not equal 2")
        self.nodes = nodes

    def get_other_node(self, node):
        return_next = False
        for n in self.nodes:
            if return_next or n != node:
                return n
            return_next = True
        raise ValueError("Node ", node, " not in edge")


