from Graph import Graph
from ChromaticPolynomial import ChromaticPolynomial

graph = Graph()
graph.addVertex("A")
graph.addVertex("B")
graph.addVertex("C")
graph.addVertex("D")
graph.addVertex("E")
graph.addVertex("F")
graph.addEdge("A", "B")
graph.addEdge("A", "C")
graph.addEdge("B", "D")
graph.addEdge("C", "D")
graph.addEdge("C", "E")
graph.addEdge("E", "D")
graph.addEdge("D", "F")

"""graph = Graph()
graph.addVertex("A")
graph.addVertex("B")
graph.addVertex("C")
graph.addVertex("D")
graph.addEdge("A", "B")
graph.addEdge("A", "C")
graph.addEdge("C", "B")"""

#TODO: look into why the wrong Polynomial gets returned

polynomial = ChromaticPolynomial(graph)
polynomial.calculatePolynomial()
print(polynomial.getPolynomial())

