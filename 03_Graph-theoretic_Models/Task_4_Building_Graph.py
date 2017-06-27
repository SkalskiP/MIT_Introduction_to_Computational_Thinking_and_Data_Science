# CLASS NODE

class Node(object):
    def __init__(self, name):
        """Assumes name is a string"""
        self.name = name
    def getName(self):
        return self.name
    def __str__(self):
        return self.name

# CLASS EDGE

class Edge(object):
    def __init__(self, src, dest):
        """Assumes src - source and dest - destination are nodes"""
        self.src = src
        self.dest = dest
    def getSource(self):
        return self.src
    def getDestination(self):
        return self.dest
    def __str__(self):
        return self.src.getName() + '->' + self.dest.getName()

# CLASS DIGRAPH

class Digraph(object):
    """Edges is a dict mapping each node to a list of its children
    Nodes are represented as keys in dictionary"""

    def __init__(self):
        # I initialize graph with empty dictionary of edges
        self.edges = {}

    def addNode(self, node):
        # Check if the node is already in the dictionary
        if node in self.edges:
            # If node already exist in dictionary raise exception
            raise ValueError('Duplicate node')
        else:
            # If node do not exist in dictionary I go into dictionary, and I create an entry with the key node,
            # and the value is initially empty list
            self.edges[node] = []

    def addEdge(self, edge):
        """Edges are represented by destinations as values list associated with a source key"""
        src = edge.getSource()
        dest = edge.getDestination()
        # If either of nodes crating edge is not in the graph raise error
        if not (src in self.edges and dest in self.edges):
            raise ValueError('Node not in graph')
        self.edges[src].append(dest)

    def childrenOf(self, node):
        return self.edges[node]

    def hasNode(self, node):
        return node in self.edges

    def getNode(self, name):
        for n in self.edges:
            if n.getName() == name:
                return n
        raise NameError(name)

    def __str__(self):
        result = ''
        for src in self.edges:
            for dest in self.edges[src]:
                result = result + src.getName() + '->' + dest.getName() + '\n'

        return result[:-1] #omit final1 newline


class Graph(Digraph):
    def addEdge(self, edge):
        Digraph.addEdge(self, edge)
        rev = Edge(edge.getDestination(), edge.getSource())
        Digraph.addEdge(self, rev)


def buildCityGraph(graphType):
    g = graphType()
    for name in ('Boston', 'Providence', 'New York', 'Chicago',
                 'Denver', 'Phoenix', 'Los Angeles'):  # Create 7 nodes
        g.addNode(Node(name))
    g.addEdge(Edge(g.getNode('Boston'), g.getNode('Providence')))
    g.addEdge(Edge(g.getNode('Boston'), g.getNode('New York')))
    g.addEdge(Edge(g.getNode('Providence'), g.getNode('Boston')))
    g.addEdge(Edge(g.getNode('Providence'), g.getNode('New York')))
    g.addEdge(Edge(g.getNode('New York'), g.getNode('Chicago')))
    g.addEdge(Edge(g.getNode('Chicago'), g.getNode('Denver')))
    g.addEdge(Edge(g.getNode('Chicago'), g.getNode('Phoenix')))
    g.addEdge(Edge(g.getNode('Denver'), g.getNode('Phoenix')))
    g.addEdge(Edge(g.getNode('Denver'), g.getNode('New York')))
    g.addEdge(Edge(g.getNode('Los Angeles'), g.getNode('Boston')))
    return g

# SCRIPT

g = buildCityGraph(Digraph)
print(g)