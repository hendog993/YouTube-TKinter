from tkinter import *
root = Tk()
root.title("Menu tutorial")
root.geometry("800x500")

def greeting():
    print("Hello user")
    return None

def kill():
    root.destroy()
    return None

# Defines top level menu
topMenu = Menu(root)
root.config(menu=topMenu)


# Create submenus and cascade them to top level menu
submenu1 = Menu(topMenu)
topMenu.add_cascade(menu=submenu1, label="Submenu 1")
submenu1.add_command(label="Command 1", command=greeting)
submenu1.add_command(label="Command 2")
submenu1.add_command(label="Command 3")
submenu1.add_command(label="Exit", command=kill)

# Create nested menus
nestedMenu = Menu(submenu1)
submenu1.add_cascade(menu=nestedMenu, label='Nested Menu')
nestedMenu.add_command(label="Nested command 1", command=greeting)
nestedMenu.add_command(label="Nested command 2")
nestedMenu.add_command(label="Nested command 3")
nestedMenu.add_command(label="Nested command 4")

root.mainloop()
