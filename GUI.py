import tkinter as tk

class GUI:
    def __init__(self, root):
        self.root = root
        root.geometry(str(root.winfo_screenwidth()) + "x" + str(root.winfo_screenheight())) #set window to screen size
        root.title("Chromatic Polynomial Calculator")

        self.button_add = tk.Button(root, text="Add Vertex", command=self.buttonAdd)
        self.button_add.grid(row=1, column=0, padx=10, pady=10)

        self.button_remove = tk.Button(root, text="Remove Vertex", command=self.buttonRemove)
        self.button_remove.grid(row=1, column=1, padx=10, pady=10)

        self.button_calculate = tk.Button(root, text="Remove Vertex", command=self.buttonRemove)
        self.button_calculate.grid(row=1, column=4, padx=10, pady=10)

        self.entry = tk.Entry(root, width=10)
        self.entry.insert(string="x", index=1)
        self.entry.grid(row=1, column=2, padx=10, pady=10, columnspan=2)


    def buttonAdd(self):
        print("add")

    def buttonRemove(self):
        print("remove")

    def buttonCalculate(self):
        print("calculate")





root = tk.Tk()
app = GUI(root)

root.mainloop()
