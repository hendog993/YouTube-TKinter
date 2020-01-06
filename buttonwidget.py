from tkinter import *

root = Tk()
root.geometry('400x400')

def greeting():
	var = int(entry1.get())
	print(pow(var, 2))

entry1 = Entry(root, width = 10)
entry1.pack()

button1 = Button(root, text="Button 1", command=greeting)
button1.pack()

root.mainloop()
