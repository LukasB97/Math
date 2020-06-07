from collections import Collection
from typing import Dict

from src.GraphTheory.Structures.Graph import Graph
from src.GraphTheory.Structures.Node import AbstractNode


def get_unknown_neighbors(node, graph):
    """
    O(1)
    @param node:
    @param graph:
    @return:
    """
    neighbors = graph.get_neighbors(node)
    unknown_neighbors = set()
    for neighbor in neighbors:
        if neighbor.state == "UNKNOWN":
            unknown_neighbors.add(neighbor)
    return unknown_neighbors


def visit_node(from_node: AbstractNode, to_node: AbstractNode, global_target: AbstractNode, open_nodes: Collection,
               nodes, path_height: Dict[(int, int), int]):
    """
    O(1)
    @param from_node:
    @param to_node:
    @param global_target:
    @param open_nodes:
    @param nodes:
    @param path_height:
    @return:
    """
    assert to_node not in open_nodes
    neighbors = get_unknown_neighbors(to_node, nodes)
    open_nodes += neighbors
    path_height[to_node.node_id] = to_node.height if to_node.height > path_height[from_node] else path_height[from_node]
    to_node.state = "Visited"
    return neighbors, global_target in neighbors, path_height


def get_lowest_predecessor(to_node, paths, graph):
    """
    O(1)
    @param to_node:
    @param paths:
    @param graph:
    @return:
    """
    neighbors = graph.get_neighbors(to_node)
    min_height = 10 ** 6
    min_node = None
    for neighbor in neighbors:
        if paths[neighbor] < min_height:
            min_node = neighbor
            min_height = paths[neighbor]
    return min_node


def next_step(open_nodes, graph, target_node, paths):
    """
    O(log n)
    @param open_nodes:
    @param graph:
    @param target_node:
    @param paths:
    @return:
    """
    next_visit = open_nodes.get_min()
    visit_from = get_lowest_predecessor(next_visit, paths, graph)
    return visit_node(visit_from, next_visit, target_node, open_nodes, graph, paths)


def find_path(start, target, graph: Graph):
    """
    O(n log n)
    @param start:
    @param target:
    @param graph:
    @return:
    """
    path_height = dict()
    open_nodes, found, path_height = next_step((), graph, target, path_height)
    while not found:
        open_nodes, found, path_height = next_step(open_nodes, graph, target, path_height)
    return path_height[get_lowest_predecessor(found, path_height, graph)]
