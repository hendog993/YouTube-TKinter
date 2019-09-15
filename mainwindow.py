from tkinter import *

_root = Tk()


def main():
    GUI = Window(_root)
    GUI.root.mainloop()
    return None


class Window:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1100x900')

        # Basic textbox
        self.textspace = Text(self.root, width=100, height=90, padx=20, pady=20)
        self.textspace.pack()

        # Menu options: master menu
        self.menu = Menu(self.root)
        self.root.config(menu=self.menu)

        # File dropdown menu
        self.fileMenu = Menu(self.menu)
        self.menu.add_cascade(label="File", menu=self.fileMenu)
        self.fileMenu.add_command(label="Save", command=self.save_file())
        self.fileMenu.add_command(label="Open", command=self.open_file())
        self.fileMenu.add_command(label="Exit", command=self.exit())

        # Edit dropdown menu
        self.editMenu = Menu(self.menu)
        self.menu.add_cascade(label="Edit", menu=self.editMenu)
        self.editMenu.add_command(label="Select All", command=self.select_all())
        self.editMenu.add_command(label="Undo", command=self.edit_undo() )

        # Format dropdown menu
        self.formatMenu = Menu(self.menu)
        self.menu.add_cascade(label="Format", menu=self.formatMenu)
        self.formatMenu.add_command(label="Change Font", command=self.change_font())
        self.formatMenu.add_command(label="Edit Margins", command=self.change_margins())
        self.formatMenu.add_command(label="Add Line Numbers", command=self.add_line_numbers())

        # Tools dropdown menu
        self.toolsMenu = Menu(self.menu)
        self.menu.add_cascade(label="Tools", menu=self.toolsMenu)
        self.toolsMenu.add_command(label="Spell")

    def save_file(self):
        pass

    def open_file(self):
        pass

    def edit_undo(self):
        pass

    def add_line_numbers(self):
        pass

    def change_font(self):
        pass

    def change_highlighted_text(self):
        pass

    def change_margins(self):
        pass

    def check_spelling(self):
        pass

    def select_all(self):
        pass

    def exit(self):
        pass

    pass


if __name__ == "__main__":
    main()
