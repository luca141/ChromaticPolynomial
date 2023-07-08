class Graph:

    def __init__(self):

        self.edges = []
        self.vertices = []
        self.current_vertices = 0
        self.current_edges = 0

    def addVertex(self, name: str):  # add a new Vertex to the Graph
        self.vertices.append(name)
        self.current_vertices += 1

    def addEdge(self, start: str, end: str):  # add a new Edge to the Graph
        self.current_edges += 1

    def  __matrix(self): #updates the Adjecency Matrix when a new Vertex is added
        for i in range(0, len(self.edges)):
            for j in range(0, len(self.edges)):



