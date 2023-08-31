from Graph import Graph
from sympy import sympify, expand
import copy
class ChromaticPolynomial:

    def __init__(self, graph: Graph):
        self.graph: Graph = graph
        self.polynomial: str = ""

    def getPolynomial(self) -> str:
        return self.polynomial

    def calculatePolynomial(self) -> str:
        isolated = self.graph.countIsolatedVertices(True) #counts and removes isolated vertices from the graph

        if len(self.graph.vertices) == 0 and isolated == 0: #if no vertices in graph
            self.polynomial = "0"
            return self.polynomial

        elif len(self.graph.vertices) == 0 and isolated > 0: #if only isolated vertices
            self.polynomial = "x**{}".format(str(isolated))
            return self.polynomial

        elif self.graph.isComplete(): #if graph is complete
            self.polynomial = "1"
            for i in range(0, len(self.graph.vertices)):
                self.polynomial += "*(x-{})".format(str(i))
            self.polynomial += "*x**{}".format(str(isolated))
            #self.polynomial = self.simplify(self.polynomial)
            return self.polynomial

        else: #if neither of the above use the deletion-contraction algorythm
            lowest_degree_vertex = self.graph.vertices[self.graph.getLowestDegreeVertex()].getContent() # look for lowest degree vertex, prevents unnecessary amount calculations
            for i in range(0, len(self.graph.edges)): #get closest vertex to the lowest degree vertex
                if self.graph.edges[self.graph._getIndex(lowest_degree_vertex)][i] > 0:
                    nearest_vertex = self.graph.vertices[i].getContent()
                    break

            graph_removed = copy.deepcopy(self.graph) #copy graph
            graph_removed.removeEdge(lowest_degree_vertex, nearest_vertex) #remove edge between the two vertices chosen above
            polynomial_removed = ChromaticPolynomial(graph_removed)
            del graph_removed
            polynomial_removed_string = polynomial_removed.calculatePolynomial() #calculate polynomial of graph without edge
            del polynomial_removed

            #same as the block above but merges the vertices instead of removing the edge
            graph_merged = copy.deepcopy(self.graph)
            graph_merged.merge(lowest_degree_vertex, nearest_vertex)
            polynomial_merged = ChromaticPolynomial(graph_merged)
            del graph_merged
            polynomial_merged_string = polynomial_merged.calculatePolynomial()
            del polynomial_merged

            self.polynomial = "(" + polynomial_removed_string + "-" + polynomial_merged_string + ")" + "*x**{}".format(str(isolated))
            return self.polynomial

    def simplify(self, term: str, variable: str):  #uses the sympy library to simplify a mathematical term
        term = term.replace("x", variable)
        return str(expand(sympify(term)))
