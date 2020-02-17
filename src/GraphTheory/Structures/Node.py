from abc import ABC, abstractmethod
from collections import Hashable


class AbstractNode(ABC, Hashable):

    def __init__(self, data, node_id):
        self.node_id = node_id
        self.data = data

    @abstractmethod
    def __hash__(self) -> int:
        pass

    @abstractmethod
    def __eq__(self, other):
        pass


