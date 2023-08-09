from Graph import Graph
from ChromaticPolynomial import ChromaticPolynomial

g = Graph()
g.addVertex("A")
g.addVertex("B")

polynomial = ChromaticPolynomial(g)
print(polynomial.simplify(polynomial.calculatePolynomial(), "x"))
