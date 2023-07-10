from Vertex import Vertex
class Graph:

    def __init__(self):

        self.edges = []
        self.vertices : list[Vertex] = []
        self.current_vertices = 0
        self.current_edges = 0

    def addVertex(self, name: str) -> bool:  # add a new Vertex to the Graph
        if self._getIndex(name) == -1:
            self.vertices.append(Vertex(name))
            self.current_vertices += 1
            self.__matrix()
            return True
        else:
            return False

    def addEdge(self, start: str, end: str) -> bool:  # add a new Edge to the Graph
        x = self._getIndex(start)
        y = self._getIndex(end)
        if x == 0 or y == 0:
            return False
        elif self.edges[x][y] == 0:
            self.edges[x][y] = 1
            self.edges[y][x] = 1
            self.current_edges += 1
            return True

    def removeEdge(self, start: str, end: str) -> bool:
        x = self._getIndex(start)
        y = self._getIndex(end)
        if self.edges[x][y] == 0:
            return False
        elif x == 0 or y == 0:
            self.edges[x][y] = 0
            self.edges[y][x] = 0
            self.current_edges -= 1
            return True

    def __matrix(self) -> None:  #updates the Adjacency Matrix when a new Vertex is added
        self.edges.append([])  #creates a new row in the matrix
        for j in range(0, len(self.edges) - 1):  #fill the new row without the last element
            self.edges[len(self.edges) - 1].append(0)
        for i in range(0, len(self.edges)):  #create a new column. same vertex intersections are numbered "-1" everything else "0"
            if i == len(self.edges) - 1:
                self.edges[i].append(-1)
            else:
                self.edges[i].append(0)

    def _getIndex(self, name) -> int:  #returns the index of a Vertex in the vertex array, returns -1 if vertex doesnt exist
        for i in range(0, len(self.edges)):
            if self.vertices[i].getContent() == name:
                return i
        return -1

    def isComplete(self) -> bool:
        if (self.current_vertices*(self.current_vertices -1))/2 == self.current_edges:
            return True
        else:
            return False

#matrix update test
"""x = Graph()
for i in range(0, 9):
    x.addVertex(str(i))
    print(x.vertices)
    for j in range(0, len(x.edges)):
        print(x.edges[j])"""