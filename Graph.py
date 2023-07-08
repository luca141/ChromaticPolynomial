class Graph:

    def __init__(self):

        self.edges = []
        self.vertices = []
        self.current_vertices = 0
        self.current_edges = 0

    def addVertex(self, name: str):  # add a new Vertex to the Graph
        self.vertices.append(name)
        self.current_vertices += 1
        self.__matrix()

    def addEdge(self, start: str, end: str):  # add a new Edge to the Graph
        self.current_edges += 1

    def __matrix(self):  #updates the Adjacency Matrix when a new Vertex is added
        self.edges.append([])  #creates a new row in the matrix
        for j in range(0, len(self.edges) - 1):  #fill the new row without the last element
            self.edges[len(self.edges) - 1].append(0)
        for i in range(0, len(self.edges)):  #create a new column. same vertex intersections are numbered "-1" everything else "0"
            if i == len(self.edges) - 1:
                self.edges[i].append(-1)
            else:
                self.edges[i].append(0)

#matrix update test
"""x = Graph()
for i in range(0, 9):
    x.addVertex(str(i))
    print(x.vertices)
    for j in range(0, len(x.edges)):
        print(x.edges[j])"""