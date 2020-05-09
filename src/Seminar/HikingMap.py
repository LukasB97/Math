from enum import Enum
from typing import Tuple, Dict, List, Set

from fibheap import Fheap


class NodeState(Enum):
    UNKNOWN = 0
    OPEN = 1
    PATH = 2


class Node:

    def __init__(self, x, y, height):
        self.x = x
        self.y = y
        self.height = height
        self.state = NodeState.UNKNOWN


class HikingMap:

    def __init__(self, row_count, col_count, height_rows):
        self.row_count = row_count
        self.col_count = col_count
        height: Dict[Tuple, Node] = dict()
        for row in range(row_count):
            for col in range(col_count):
                height[(col, row)] = height_rows[row_count][col]
        self.nodes = height

    @staticmethod
    def get_neighbors(x, y):
        """
        O(1)
        Returns [North, East, South, West] heights
        @rtype: [int]
                """
        pass

    def get_lowest_neighbor(self):
        pass


class Path:

    # @property
    # def height(self) -> int:
    #     pass

    def append(self, x, y):
        pass


class MapManager:

    def __init__(self):
        pass

    def merge_paths(self, p1: Path, p2: Path):
        pass

    def visit(self, path, x, y):
        pass


class HikingPathFinderMap(HikingMap):

    def __init__(self, row_count, col_count, height_rows):
        super().__init__(row_count, col_count, height_rows)
        self.next_id = 1
        self.paths = dict()
        self.visited_by = dict()

    def visit(self, path_id, to_x, to_y):
        self.paths[path_id].append(to_x, to_y)
        self.visited_by[(to_x, to_y)].append(path_id)

    def get_paths_from(self, from_x, from_y):
        pass

    def get_lowest_path(self, from_x, from_y):
        pass

    def get_unvisited_neighbors(self, x, y):
        pass

    def get_lowest_unvisited(self, x, y):
        pass

    @staticmethod
    def get_neighbors_under(x, y, max_height):
        """
        Returns [((int,int), int] heights
        @rtype: [((int,int), int]
        """
        pass

    def get_paths_of_length(self, from_coord, length, max_height):
        pass


class HikingMapDijkstra(HikingPathFinderMap):

    def __init__(self, row_count, col_count, height_rows):
        super().__init__(row_count, col_count, height_rows)

    def start(self, from_x, from_y, to_x, to_y):
        open_nodes = Fheap()
        self._close_node(from_x, from_y, open_nodes)
        target = self.nodes[(to_x, to_y)]
        closed_node = self._next_step(open_nodes)
        while closed_node != target:
            closed_node = self._next_step(open_nodes)

    def _get_unvisited_neighbors(self, x, y):
        to_open = Fheap()
        if y > 1 and self.nodes[(x, y - 1)].state == NodeState.UNKNOWN:
            to_open.insert(self.nodes[(x, y - 1)])
        if x < self.col_count and self.nodes[(x + 1, y)].state == NodeState.UNKNOWN:
            to_open.insert(self.nodes[(x + 1, y)])
        if y < self.row_count and self.nodes[(x, y + 1)].state == NodeState.UNKNOWN:
            to_open.insert(self.nodes[(x, y + 1)])
        if x > 1 and self.nodes[(x - 1, y)].state == NodeState.UNKNOWN:
            to_open.insert(self.nodes[(x - 1, y)])
        return to_open

    def _close_node(self, x, y, open_nodes: Fheap, finished=False):
        self.nodes[(x, y)].state = NodeState.PATH
        if not finished:
            neighbors = self._get_unvisited_neighbors(x, y)
            open_nodes.union(neighbors)

    def _end_walk(self):
        self.open_nodes = []

    def _next_step(self, open_nodes: Fheap):
        to_close = open_nodes.extract_min()
        self._close_node(to_close.x, to_close.y, open_nodes)
        return to_close

    @staticmethod
    def _create_critical_coords(from_to: List[Tuple[int, int]]):
        critical_coords = set()
        for route in from_to:
            critical_coords.update(route)
        return critical_coords

    def _clear_map(self, critical_coords: Set[Tuple]):
        pass

    def optimize_paths(self, from_to: List[Tuple[int, int]]):
        pass
