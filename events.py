# Create an interface that increments/decrements a value by 1, and has a reverse button
# that switches the increment and decrement function. 

from tkinter import * 
root = Tk()
root.geometry('200x100')

def increase():
    value["text"] = value["text"] + 1
    pass 

def decrease():
    value["text"] = value["text"] - 1
    pass 

def reverse():
    increase_button["command"] = decrease
    decrease_button["command"] = increase
    reverse_button["command"] = antireverse
    pass 

def antireverse():
    increase_button["command"] = increase
    decrease_button["command"] = decrease
    reverse_button["command"] = reverse

    pass 

increase_button = Button(root, text="+", command=increase)
increase_button.grid(row=0, column=2)

value = Label(root, text = 0)
value.grid(row=0, column = 1)

decrease_button = Button(root, text="-", command=decrease)
decrease_button.grid(row=0, column=0)

reverse_button = Button(root, text = "Reverse", command=reverse)
reverse_button.grid(row=1, column=1)


root.mainloop()