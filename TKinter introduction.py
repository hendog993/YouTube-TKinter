from tkinter import * 

# Master variable
root = Tk()

def greeting():
    print("Hello world")
    return None 


# Simple Label
label1 = Label(root, text = "Welcome to my GUI")
# Every widget needs geometry management
# 3 Main methods of geometry management: pack, grid, place.
label1.pack()


# Button: widget object, geometry management
button1 = Button(root, text = "Click me", command = greeting)
button1.pack()

root.mainloop()

# Import library, declare a master variable, start loop 
