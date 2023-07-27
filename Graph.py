from Vertex import Vertex
class Graph:

    def __init__(self):

        self.edges = []
        self.vertices : list[Vertex] = []
        self.current_vertices = 0
        self.current_edges = 0
        self.isolated_Vertices = 0

    def addVertex(self, name: str) -> bool:
        """add a new Vertex to the Graph"""
        if self._getIndex(name) == -1:  #if vertex doesn't exist already
            self.vertices.append(Vertex(name))
            self.current_vertices += 1
            self.__matrixAdd()
            return True
        else:
            return False

    def removeVertex(self, name: str) -> bool:
        """removes existing vertex from Graph"""
        if self._getIndex(name) == -1:  #if Vertex doesn't exist
            return False
        else:  #remove Vertex from array
            self.current_vertices -= 1
            self.__matrixRemove(name)
            self.vertices.pop(self._getIndex(name))
            return False

    def addEdge(self, start: str, end: str) -> bool:
        """add a new Edge to the Graph"""
        x = self._getIndex(start)
        y = self._getIndex(end)
        if x == y:  #if start and end vertex are the same (to avoid loops)
            return False
        elif x == -1 or y == -1:  #if at least one vertex doesn't exist
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

    def removeEdge(self, start: str, end: str) -> bool:
        """remove an existing edge from the graph"""
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

    def __matrixAdd(self) -> None:
        """updates the Adjacency Matrix when a new Vertex is added"""
        self.edges.append([])  #creates a new row in the matrix
        for j in range(0, len(self.edges) - 1):  #fill the new row without the last element (which is added with the column)
            self.edges[len(self.edges) - 1].append(0)
        for i in range(0, len(self.edges)):  #create a new column. same vertex intersections are numbered "-1" everything else "0"
            if i == len(self.edges) - 1:
                self.edges[i].append(-1)
            else:
                self.edges[i].append(0)

    def __matrixRemove(self, name) -> None:
        """updates the Adjacency Matrix when a Vertex is removed"""
        x = self._getIndex(name)
        for j in range(0, len(self.edges)):  #update edge counter and Vertex degrees
            if self.edges[x][j] > 0:  #if the Vertex that will be removed is connected to other Vertices
                self.current_edges -= 1
                self.vertices[j].setDegree(self.vertices[j].getDegree() - 1)
        for i in range(0, len(self.edges)):  #remove column
            self.edges[i].pop(x)
        self.edges.pop(x)  #remove row

    def _getIndex(self, name) -> int:
        """returns the index of a Vertex in the vertex array, returns -1 if vertex doesn't exist"""
        for i in range(0, len(self.edges)):
            if self.vertices[i].getContent() == name:
                return i
        return -1

    def isComplete(self) -> bool:
        """checks if a graph is complete"""
        if (self.current_vertices*(self.current_vertices - 1))/2 == self.current_edges:  #if the formula for maximum edges in a Graph is equal to the current number of edges in the Graph
            return True
        else:
            return False

    def countIsolatedVertices(self, remove_Isolated: bool) -> int:
        """counts isolated vertices, takes a boolean parameter to decide if isolated vertices are deleted from the graph or not"""
        self.isolated_Vertices = 0  #reset counter
        for i in range(0, len(self.vertices)):
            if self.vertices[i].getDegree() == 0:  #if vertex is not connected to any other Vertices
                self.isolated_Vertices += 1
                if remove_Isolated:
                    self.removeVertex(self.vertices[i].getContent())
        return self.isolated_Vertices


    def merge(self, vertex1: str, vertex2: str) -> None:
        """merges two vertices"""
        if vertex1 == vertex2:
            pass
        else:
            x = self._getIndex(vertex1)
            y = self._getIndex(vertex2)
            for i in range(0, len(self.edges)):  #transfer edges of vertex2 to vertex1
                if self.edges[y][i] > 0:  #if vertex2 is connected to any other vertices
                    self.addEdge(vertex1, self.vertices[i].getContent())
            self.removeVertex(vertex2)

    def getLowestDegreeVertex(self) -> int:
        """returns the array index of the Vertex with the lowest degree, if multiple vertices have the same degree it returns the first of those"""
        a = self.vertices[0].getDegree()
        index = 0
        for i in range(0, len(self.vertices)):
            if self.vertices[i].getDegree() < a:
                a = self.vertices[i].getDegree()
                index = i
        return index


#matrix update test
"""x = Graph()
for i in range(0, 9):
    x.addVertex(str(i))
    print(x.vertices)
    for j in range(0, len(x.edges)):
        print(x.edges[j])"""