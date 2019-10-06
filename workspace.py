from tkinter import *

class Window:
    n = 0

    def __init__(self, root , title, geometry, message):
        self.root = root
        self.root.title(title)
        self.root.geometry(geometry)  #  input, sizexsize
        Label(self.root, text=message).pack()
        button1 = Button(self.root, text="Increment", command=self.increment)
        button1.pack()
        self.root.mainloop()
        pass

    def increment(self):
        self.n += 1
        print(self.n)
        return None

    pass



global n
n = 0
root = Tk()
def increment(variable = n):
    variable += 1
    print(variable)
    return None


button1 = Button(root, text="Increment", command=increment)
button1.pack()


root.mainloop()
