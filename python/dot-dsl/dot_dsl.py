NODE, EDGE, ATTR = range(3)


class Node(object):
    def __init__(self, name, attrs={}):
        self.name = name
        self.attrs = attrs

    def __eq__(self, other):
        return self.name == other.name and self.attrs == other.attrs


class Edge(object):
    def __init__(self, src, dst, attrs={}):
        self.src = src
        self.dst = dst
        self.attrs = attrs

    def __eq__(self, other):
        return (self.src == other.src and
                self.dst == other.dst and
                self.attrs == other.attrs)


class Graph(object):
    def __init__(self, data=[]):
        self.nodes = []
        self.edges = []
        self.attrs = {}

        for e in data:
            self._ensure_valid(e)
            form = e[0]
            if form == ATTR:
                self.attrs[e[1]] = e[2]
            elif form == NODE:
                self.nodes.append(Node(e[1], e[2]))
            elif form == EDGE:
                self.edges.append(Edge(e[1], e[2], e[3]))
            else:
                raise ValueError("Unknown element")

    def _ensure_valid(self, e):
        c = len(e)
        if c < 3:
            raise TypeError('malformed')
        f = e[0]
        if (f == EDGE and c != 4) or ((f == NODE or f == ATTR) and c != 3):
            raise ValueError('malformed')
