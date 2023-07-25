"""from sympy import sympify, expand

expression_str = "(x-0)*(x-1)*(x-2)"
expression = sympify(expression_str)

expanded_expression = expand(expression)
expanded_expression_str = str(expanded_expression)

print(expanded_expression_str)


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
g.removeVertex("c")
g.removeVertex("d")
for j in range(0, len(g.edges)):
        print(g.edges[j])
g.removeVertex("a")
for j in range(0, len(g.edges)):
        print(g.edges[j])
print(g.current_edges)"""
