import tkinter as tk
from Graph import Graph
from ChromaticPolynomial import ChromaticPolynomial
import copy
import time
import sys


class GUI:
    def __init__(self, root):
        self.radius = 15
        self.x = 100
        self.y = 100
        self.vertices_graphic = []
        self.edges_graphic = []
        self.highlighted_circle = None

        self.root = root
        root.geometry(str(root.winfo_screenwidth()) + "x" + str(root.winfo_screenheight()))  #set window to screen size
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

        self.canvas = tk.Canvas(root, width=root.winfo_screenwidth() - 40, heigh=root.winfo_screenheight() - 150, bg="white")
        self.canvas.place(x=20, y=50)

        self.text_widget = tk.Text(root, wrap=tk.WORD, height=1)
        self.text_widget.grid(row=1, column=6, padx=10, pady=10)

        self.time_widget = tk.Text(root, wrap=tk.WORD, height=1, width=10)
        self.time_widget.grid(row=1, column=10, padx=10, pady=10)

        sys.setrecursionlimit(10000)

    def buttonAdd(self):
        vertex = self.canvas.create_oval(self.x - self.radius, self.y - self.radius, self.x + self.radius,
                                         self.y + self.radius, fill="lightgreen", width=1)
        self.canvas.tag_bind(vertex, "<B1-Motion>", lambda event: self.moveCircle(event, vertex))
        self.canvas.tag_bind(vertex, "<Button-3>", lambda event: self.highlightCircle(vertex))
        self.vertices_graphic.append(vertex)
        self.graph.addVertex(str(self.vertices_graphic[len(self.vertices_graphic) - 1]))


    def moveCircle(self, event, circle):
        x, y = event.x, event.y
        self.canvas.coords(circle, x - self.radius, y - self.radius, x + self.radius, y + self.radius)
        self.updateEdges()

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

            else:
                self.graph.removeEdge(self.graph.vertices[v1].getContent(), self.graph.vertices[v2].getContent())

            self.canvas.itemconfig(self.highlighted_circle, outline="black")
            self.canvas.itemconfig(circle, outline="black")
            self.highlighted_circle = None
            self.updateEdges()


    def buttonRemove(self):
        if self.highlighted_circle != None:
            self.graph.removeVertex(self.graph.vertices[self.vertices_graphic.index(self.highlighted_circle)].getContent())
            self.vertices_graphic.remove(self.highlighted_circle)
            self.canvas.delete(self.highlighted_circle)
            self.highlighted_circle = None

    def buttonCalculate(self):
        graph_copy = copy.deepcopy(self.graph)
        time1 = time.time() * 1000
        polynomial = ChromaticPolynomial(graph_copy)
        polynomial = polynomial.simplify(polynomial.calculatePolynomial(), str(self.entry.get()))
        time2 = (time.time() * 1000) - time1
        self.text_widget.delete("1.0", tk.END)  # Clear existing content
        self.time_widget.delete("1.0", tk.END)  # Clear existing content
        self.text_widget.insert("1.0", polynomial)
        self.time_widget.insert("1.0", str(round(time2/1000, 3)) + "s")

    def buttonReset(self):
        for i in range(len(self.graph.vertices)):
            self.canvas.delete(self.vertices_graphic[i])
        for j in range(len(self.graph.vertices)):
            self.graph.removeVertex(self.graph.vertices[0].getContent())
            self.vertices_graphic.pop(0)
        self.updateEdges()
        self.text_widget.delete("1.0", tk.END)

    def updateEdges(self):
        for l in self.edges_graphic:
            self.canvas.delete(l)

        for i in range(0, len(self.graph.edges)):
            for j in range(0, len(self.graph.edges)):
                if self.graph.edges[i][j] == -1:
                    break
                elif self.graph.edges[i][j] == 1:
                    x1, y1 = self.get_center(self.vertices_graphic[i])
                    x2, y2 = self.get_center(self.vertices_graphic[j])
                    line = self.canvas.create_line(x1, y1, x2, y2, fill="black")
                    self.canvas.tag_lower(line)
                    self.edges_graphic.append(line)


    def get_center(self, circle):
        x1, y1, x2, y2 = self.canvas.coords(circle)
        return (x1 + x2) / 2, (y1 + y2) / 2


