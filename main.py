from Graph import Graph
from ChromaticPolynomial import ChromaticPolynomial

g = Graph()
g.addVertex("A")
g.addVertex("B")
g.addVertex("C")
g.addVertex("D")
g.addVertex("E")
g.addVertex("F")
g.addVertex("G")
g.addVertex("H")
g.addVertex("I")
g.addVertex("J")
g.addEdge("A", "B")
g.addEdge("B", "C")
g.addEdge("C", "D")
g.addEdge("D", "E")
g.addEdge("E", "A")
g.addEdge("A", "F")
g.addEdge("B", "G")
g.addEdge("C", "H")
g.addEdge("D", "I")
g.addEdge("E", "J")
g.addEdge("F", "I")
g.addEdge("I", "G")
g.addEdge("G", "J")
g.addEdge("J", "H")
g.addEdge("H", "F")

polynomial = ChromaticPolynomial(g)
print(polynomial.simplify(polynomial.calculatePolynomial()))
