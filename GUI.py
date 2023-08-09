import tkinter as tk
from Graph import Graph
from ChromaticPolynomial import ChromaticPolynomial

class GUI:
    def __init__(self, root):
        self.radius = 15
        self.x = 100
        self.y = 100
        self.vertices_graphic = []
        self.edges_graphic = []
        self.highlighted_circle = None

        self.root = root
        root.geometry(str(root.winfo_screenwidth()) + "x" + str(root.winfo_screenheight())) #set window to screen size
        root.title("Chromatic Polynomial Calculator")
        root.configure(bg="grey")

        self.graph = Graph()

        self.button_add = tk.Button(root, text="Add Vertex", command=self.buttonAdd)
        self.button_add.grid(row=1, column=0, padx=10, pady=10)

        self.button_remove = tk.Button(root, text="Remove Vertex", command=self.buttonRemove)
        self.button_remove.grid(row=1, column=1, padx=10, pady=10)

        self.button_calculate = tk.Button(root, text="Calculate Polynomial", command=self.buttonCalculate)
        self.button_calculate.grid(row=1, column=4, padx=10, pady=10)

        self.button_reset = tk.Button(root, text="Reset", command=self.buttonReset)
        self.button_reset.grid(row=1, column=5, padx=10, pady=10)

        self.entry = tk.Entry(root, width=10)
        self.entry.insert(string="x", index=1)
        self.entry.grid(row=1, column=2, padx=10, pady=10, columnspan=2)

        self.canvas = tk.Canvas(root, width=root.winfo_screenwidth() - 40, heigh=root.winfo_screenheight()-150, bg="white")
        self.canvas.place(x=20, y=50)

    def buttonAdd(self):
        vertex = self.canvas.create_oval(self.x - self.radius, self.y - self.radius, self.x + self.radius, self.y +self.radius, fill="lightgreen", width=1)
        self.graph.addVertex(str(self.graph.current_vertices))
        self.canvas.tag_bind(vertex, "<B1-Motion>", lambda event: self.moveCircle(event, vertex))
        self.canvas.tag_bind(vertex, "<Button-3>", lambda event: self.highlightCircle(vertex))
        self.vertices_graphic.append(vertex)

    def moveCircle(self, event, circle):
        x, y = event.x, event.y
        self.canvas.coords(circle, x - self.radius, y - self.radius, x + self.radius, y + self.radius)

    def highlightCircle(self, circle):
        if self.highlighted_circle == None:
            self.highlighted_circle = circle
            self.canvas.itemconfig(circle, outline="red")
        elif circle == self.highlighted_circle:
            self.highlighted_circle = None
            self.canvas.itemconfig(circle, outline="black")
        else:
            v1 = self.vertices_graphic.index(circle)
            v2 = self.vertices_graphic.index(self.highlighted_circle)
            if self.graph.edges[v1][v2] == 0:
                self.graph.addEdge(self.graph.vertices[v1].getContent(), self.graph.vertices[v2].getContent())
                self.highlighted_circle = None
                self.canvas.itemconfig(circle, outline="black")
            else:
                self.graph.removeEdge(self.graph.vertices[v1].getContent(), self.graph.vertices[v2].getContent())
                self.highlighted_circle = None
                self.canvas.itemconfig(circle, outline="black")
    def buttonRemove(self):
        self.canvas.delete(self.vertices_graphic[0])
        self.vertices_graphic.pop(0)
        self.graph.removeVertex(self.graph.vertices[0].getContent())

    def buttonCalculate(self):
        polynomial = ChromaticPolynomial(self.graph)
        polynomial = polynomial.simplify(polynomial.calculatePolynomial(), str(self.entry.get()))
        print(polynomial)
    def buttonReset(self):
        pass

    def updateEdges(self):
        pass







root = tk.Tk()
app = GUI(root)

root.mainloop()
