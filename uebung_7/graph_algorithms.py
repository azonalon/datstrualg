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
        'A': { 'B': 1.5, 'C': 0.1 },
        'B': { 'A': 3.2, 'C': 0.5 },
        'C': { 'A': 5.1, 'B': 3.0 }
    })
    """
    def __init__(self, graph):
        self.graph = graph

    def outAdjacent(self, node):
        return graph[node].keys()

    def inAdjacent(self, node):
        # TODO: implement
        pass

    def weight(self, a, b):
        return self.graph[a].get(b, 0.0)

    def nodes(self):
        return list(self.graph.keys())

    def edges(self):
        return sum(
            [
                [(node[0], adjacent[0], adjacent[1]) for adjacent in node[1].items()]
                for node in self.graph.items()
            ], [])



graph = Graph({
    'A': ['B', 'C'],
    'B': ['A', 'C'],
    'C': ['A', 'B']
})

wgraph = WeightedGraph({
    's': {'t': 10, 'y': 5},
    't': {'y': 2, 'x': 1},
    'x': {'z': 4         },
    'y': {'t':  3, 'x': 9, 'z': 2},
    'z': {'s':  7, 'x': 6},
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
    graph = graph
    if is_directed:
        g = graphviz.Digraph()
    else:
        g = graphviz.Graph()

    for n in graph.nodes():
        g.node(n)
    for e in graph.edges():
        g.edge(*map(str,e))

    g.view()

print(graph.edges())
print(graph.nodes())
print(wgraph.edges())
print(wgraph.nodes())
# BreadthFirstSearch(graph,  'A')
# DepthFirstSearch(graph,  'A')
# View(graph)
View(wgraph)
