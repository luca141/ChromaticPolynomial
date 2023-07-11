from Graph import Graph

g = Graph()
g.addVertex("a")
g.addVertex("b")
g.addVertex("c")
g.addVertex("d")
for j in range(0, len(g.edges)):
        print(g.edges[j])
g.addEdge("a", "b")
g.addEdge("a", "c")
g.addEdge("b", "d")
g.addEdge("c", "d")
print(g.isComplete())
g.addEdge("a", "d")
g.addEdge("b", "c")
print(g.current_edges)
print(g.current_vertices)
print(g.isComplete())
for j in range(0, len(g.edges)):
        print(g.edges[j])
g.removeVertex("b")
for j in range(0, len(g.edges)):
        print(g.edges[j])