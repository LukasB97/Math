from enum import Enum
from queue import PriorityQueue
from typing import Dict, Tuple


class NodeState(Enum):
    UNKNOWN = 0
    OPEN = 1
    CLOSED = 2


class Node:

    def __init__(self, height, x, y):
        self.height = height
        self.state = NodeState.UNKNOWN
        self.coord = (x, y)

    def __gt__(self, other):
        return self.height > other.height

    def __lt__(self, other):
        return self.height < other.height

    def __eq__(self, other):
        return self.coord == other.coord

    def __hash__(self):
        return hash(self.coord)

    def __repr__(self):
        return "x:{} , y: {}, height: {}".format(*self.coord, self.height)


class MinGraph:

    def __init__(self, nodes: Dict[Tuple, Node], rows, cols):
        self.nodes = nodes
        self.rows = rows
        self.cols = cols

    def __len__(self):
        return len(self.nodes)

    def reset(self):
        for node in self.nodes.values():
            node.state = NodeState.UNKNOWN

    def __getitem__(self, item):
        return self.nodes[item]

    def get_unknown_neighbors(self, coordinate):
        neighbors = self.get_neighbors(coordinate)
        return {node for node in neighbors if node.state == NodeState.UNKNOWN}

    def get_neighbors(self, coordinate: Tuple):
        x, y = coordinate
        neighbors = set()
        if y > 0:
            neighbors.add(self.nodes[(x, y - 1)])
        if x < self.cols - 1:
            neighbors.add(self.nodes[(x + 1, y)])
        if y < self.rows - 1:
            neighbors.add(self.nodes[(x, y + 1)])
        if x > 0:
            neighbors.add(self.nodes[(x - 1, y)])
        return neighbors


def visit_node(graph: MinGraph, from_node: Node, to_node: Node,
               open_nodes: PriorityQueue, path_height: Dict[Tuple[int, int], int]):
    """
    O(1)
    @param from_node:
    @param to_node:
    @param global_target:
    @param open_nodes:
    @param graph:
    @param path_height:
    @return:
    """
    neighbors = graph.get_unknown_neighbors(to_node.coord)
    for neighbor in neighbors:
        open_nodes.put_nowait(neighbor)
    if to_node.height >= path_height.get(from_node.coord, to_node.height):
        path_height[to_node.coord] = to_node.height
    else:
        path_height[to_node.coord] = path_height[from_node.coord]
    to_node.state = NodeState.CLOSED
    return open_nodes, to_node, path_height


def get_lowest_predecessor(graph: MinGraph, to_node: Node, paths: Dict[Tuple, int]):
    """
    O(1)
    @param to_node:
    @param paths:
    @param graph:
    @return:
    """
    neighbors = graph.get_neighbors(to_node.coord)
    min_height = 1000000  # 10**6
    min_node = to_node
    for neighbor in neighbors:
        if paths.get(neighbor.coord, min_height) < min_height: #Überprüfe Pfadhöhe des nachbarn. Falls noch unbekannt gebe minheight zurück
            min_node = neighbor
            min_height = paths[neighbor.coord]
    return min_node


def next_step(
        graph: MinGraph, paths: Dict[Tuple, int],
        open_nodes):
    """
    O(log n)
    @param open_nodes:
    @param graph:
    @param target_node:
    @param paths:
    @return:
    """
    next_visit = open_nodes.get_nowait()
    visit_from = get_lowest_predecessor(graph=graph, to_node=next_visit, paths=paths)
    return visit_node(
        graph=graph, from_node=visit_from, to_node=next_visit,
        path_height=paths, open_nodes=open_nodes
    )


def find_path(graph: MinGraph, route: Tuple):
    """
    O(n log n)
    @param route: ((from_x, from_y), (to_x, to_y))
    @param graph:
    @return:
    """
    start, target = route
    start, target = graph[start], graph[target]
    open_nodes = PriorityQueue(maxsize=len(graph))
    open_nodes.put(start)
    path_height = dict()
    open_nodes, closed_node, path_height = next_step(
        graph=graph, paths=path_height,
        open_nodes=open_nodes
    )
    while closed_node != target:
        open_nodes, closed_node, path_height = next_step(
            open_nodes=open_nodes, graph=graph, paths=path_height
        )
    return path_height[target.coord]


def find_all_paths(graph: MinGraph, routes: list):
    """
    O(routes) * O(find_path)
    """
    heights = list()
    for route in routes:
        heights.append(str(find_path(graph, route)))
        graph.reset()
    return "\n".join(heights)


def main():
    dimension = input()
    rows, columns, mountaineers = dimension.split(" ")
    rows, columns, mountaineers = int(rows), int(columns), int(mountaineers)
    nodes = dict()
    for i in range(rows):
        row_heights = input().split(" ")
        for j in range(len(row_heights)):
            nodes[(j, i)] = Node(int(row_heights[j]), x=j, y=i)
    graph = MinGraph(nodes, rows, columns)
    routes = list()
    for i in range(mountaineers):
        from_y, from_x, to_y, to_x = input().split(" ")
        routes.append(((int(from_x) - 1, int(from_y) - 1), (int(to_x) - 1, int(to_y) - 1)))
    return find_all_paths(graph, routes)


if __name__ == '__main__':
    print(main())
