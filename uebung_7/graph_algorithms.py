#!/bin/python
import graphviz
from collections import deque


class Graph:
    """ Example:
    graph = Graph({
        'A': ['B', 'C'],
        'B': ['A', 'C'],
        'C': ['A', 'B']
    })
    """
    def __init__(self, graph):
        self.graph = graph

    def outAdjacent(self, node):
        return self.graph[node]

    def inAdjacent(self, node):
        # TODO: implement
        return []

    def nodes(self):
        return list(self.graph.keys())

    def edges(self):
        return sum(
            [
                [(node[0], adjacent) for adjacent in node[1]]
                for node in self.graph.items()
            ], [])

class WeightedGraph:
    """ Example:
    graph = Graph({
        'A': [('B', 1.5), ('C', 0.1)],
        'B': [('A', 3.2), ('C', 0.5)],
        'C': [('A', 5.1), ('B', 3.0)]
    })
    """
    def __init__(self):
        pass
    # TODO: Implement





graph = Graph({
    'A': ['B', 'C'],
    'B': ['A', 'C'],
    'C': ['A', 'B']
})

def BreadthFirstSearch(graph, node):
    print('Breadth First Search')
    color = dict((n, 'white') for n in graph.nodes())
    pred = {}
    visited = []

    def visit(node):
        q = deque()
        color[node] = 'grey'
        q.appendleft(node)
        while len(q) != 0:
            current_node = q.pop()
            visited.append(current_node)

            for adjacent in graph.outAdjacent(current_node):
                if color[adjacent] is 'white':
                    color[adjacent] = 'grey'
                    pred[adjacent] = current_node
                    q.appendleft(adjacent)
            color[current_node] = 'black'

    visit(node)

    for node, color in color.items():
        if color is 'white':
            visit(node)

    print('visited :', visited)
    print('predecessors :', pred)







def DepthFirstSearch(graph, node):
    print('Depth First Search')
    color = dict((n, 'white') for n in graph.nodes())
    pred = {}
    visited = []

    def visit(node):
        s = deque()
        s.append(node)
        visited.append(node)
        color[node] = 'grey'
        while len(s) != 0:
            current_node = s.pop()
            found_white = False
            for adjacent in graph.outAdjacent(current_node):
                if color[adjacent] is 'white':
                    found_white = True
                    color[adjacent] = 'grey'
                    pred[adjacent] = current_node
                    visited.append(adjacent)
                    s.append(current_node)
                    s.append(adjacent)
            if not found_white:
                color[current_node] = 'black'

    visit(node)

    for node, color in color.items():
        if color is 'white':
            visit(node)

    print('visited :', visited)
    print('predecessors :', pred)





# Plot the graph with graphviz
def View(graph, is_directed=True):
    graph = graph.graph
    if is_directed:
        g = graphviz.Digraph()
    else:
        g = graphviz.Digraph()

    for node, adjacents in graph.items():
        g.node(node)
        for adjacent in adjacents:
            g.edge(node, adjacent)

    g.view()

BreadthFirstSearch(graph,  'A')
DepthFirstSearch(graph,  'A')
View(graph)
