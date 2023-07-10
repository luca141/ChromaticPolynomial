from Vertex import Vertex
class Graph:

    def __init__(self):

        self.edges = []
        self.vertices : list[Vertex] = []
        self.current_vertices = 0
        self.current_edges = 0

    def addVertex(self, name: str) -> bool:  # add a new Vertex to the Graph
        if self._getIndex(name) == -1:  #if vertex doesn't exist already
            self.vertices.append(Vertex(name))
            self.current_vertices += 1
            self.__matrixAdd()
            return True
        else:
            return False

    def removeVertex(self, name: str) -> bool:
        if self._getIndex(name) == -1:  #if Vertex doesn't exist
            return False
        else:  #remove Vertex from array
            self.vertices.pop(self._getIndex(name))
            self.current_vertices -= 1
            self.__matrixRemove(name)
            return False

    def addEdge(self, start: str, end: str) -> bool:  # add a new Edge to the Graph
        x = self._getIndex(start)
        y = self._getIndex(end)
        if x == -1 or y == -1: #if at least one vertex doesn't exist
            return False
        elif self.edges[x][y] > 0:  #if edge exists
            return False
        elif self.edges[x][y] == 0:  #if edge doesn't exist
            self.edges[x][y] = 1
            self.edges[y][x] = 1
            self.current_edges += 1
            self.vertices[x].setDegree(self.vertices[x].getDegree() + 1)
            self.vertices[y].setDegree(self.vertices[y].getDegree() + 1)
            return True

    def removeEdge(self, start: str, end: str) -> bool:  #remove an existing edge from the graph
        x = self._getIndex(start)
        y = self._getIndex(end)
        if x == -1 or y == -1:  #if at least on vertex doesn't exist
            return False
        elif self.edges[x][y] == 0:  #if edge doesn't exist
            return False
        elif self.edges[x][y] > 0:  #if edge exists
            self.edges[x][y] = 0
            self.edges[y][x] = 0
            self.current_edges -= 1
            self.vertices[x].setDegree(self.vertices[x].getDegree() - 1)
            self.vertices[y].setDegree(self.vertices[y].getDegree() - 1)
            return True

    def __matrixAdd(self) -> None:  #updates the Adjacency Matrix when a new Vertex is added
        self.edges.append([])  #creates a new row in the matrix
        for j in range(0, len(self.edges) - 1):  #fill the new row without the last element (which is added with the column)
            self.edges[len(self.edges) - 1].append(0)
        for i in range(0, len(self.edges)):  #create a new column. same vertex intersections are numbered "-1" everything else "0"
            if i == len(self.edges) - 1:
                self.edges[i].append(-1)
            else:
                self.edges[i].append(0)

    #TODO: update edge counter
    def __matrixRemove(self, name) -> None:  #updates the Adjacency Matrix when a Vertex is removed
        x = self._getIndex(name)
        for i in range(0, len(self.edges)):  #remove column
            self.edges[i].pop(x)
        self.edges.pop(x)  #remove row

    def _getIndex(self, name) -> int:  #returns the index of a Vertex in the vertex array, returns -1 if vertex doesn't exist
        for i in range(0, len(self.edges)):
            if self.vertices[i].getContent() == name:
                return i
        return -1

    def isComplete(self) -> bool:  #checks if a graph is complete
        if (self.current_vertices*(self.current_vertices -1))/2 == self.current_edges:  #if the formula for maximum edges in a Graph is equal to the current number of edges in the Graph
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