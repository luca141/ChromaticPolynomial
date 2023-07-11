from Graph import Graph
from sympy import sympify, expand
class ChromaticPolynomial:

    def __init__(self, graph: Graph):
        self.graph: Graph = graph
        self.polynomial: str = ""

    def getPolynomial(self) -> str:
        return self.polynomial

    def calculatePolynomial(self, graph) -> str:
        if graph.isComplete():
            self.polynomial = "1"
            for i in range(0, len(self.graph.vertices)):
                self.polynomial += "*(x-{})".format(str(i))
            return self.simplify(self.polynomial)

    def simplify(self, term):  #uses the sympy library to simplify a mathematical term
        return str(expand(sympify(term)))
