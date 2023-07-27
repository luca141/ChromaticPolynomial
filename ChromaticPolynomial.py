from Graph import Graph
from sympy import sympify, expand
class ChromaticPolynomial:

    def __init__(self, graph: Graph):
        self.graph: Graph = graph
        self.polynomial: str = ""

    def getPolynomial(self) -> str:
        return self.polynomial

    def calculatePolynomial(self) -> str:
        print("calculating")
        isolated = self.graph.countIsolatedVertices(True)
        if self.graph.isComplete():
            self.polynomial = "1"
            for i in range(0, len(self.graph.vertices)):
                self.polynomial += "*(x-{})".format(str(i))
            self.polynomial += "*x**{}".format(str(isolated))
            self.polynomial = self.simplify(self.polynomial)
            return self.polynomial
        else:
            lowest_degree_vertex = self.graph.vertices[self.graph.getLowestDegreeVertex()].getContent()
            for i in range(0, len(self.graph.edges)):
                if self.graph.edges[self.graph._getIndex(lowest_degree_vertex)][i] > 0:
                    nearest_vertex = self.graph.vertices[i].getContent()
                    break
            graph_removed = self.graph
            graph_removed.removeEdge(lowest_degree_vertex, nearest_vertex)
            graph_merged = self.graph
            graph_merged.merge(lowest_degree_vertex, nearest_vertex)
            polynomial_removed = ChromaticPolynomial(graph_removed)
            polynomial_removed.calculatePolynomial()
            polynomial_merged = ChromaticPolynomial(graph_merged)
            polynomial_merged.calculatePolynomial()
            self.polynomial = self.simplify(polynomial_removed.getPolynomial() + "-" + polynomial_merged.getPolynomial())
            return self.polynomial

    def simplify(self, term):  #uses the sympy library to simplify a mathematical term
        return str(expand(sympify(term)))
