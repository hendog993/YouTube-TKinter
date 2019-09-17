from tkinter import *
import os

_root = Tk()


# TODO add executable functionality instead of just a script
# TODO

def main():
    gui = Window(_root)
    gui.root.mainloop()
    return None


class Window:
    def __init__(self, root):
        self.root = root
        self.root.geometry('900x600')

        # Basic textbox
        self.textspace = Text(self.root, width=100, height=90, padx=5, pady=5)
        self.textspace.pack()

        # Menu options: master menu
        self.menu = Menu(self.root)
        self.root.config(menu=self.menu)

        # File dropdown menu
        self.fileMenu = Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="File", menu=self.fileMenu)
        self.fileMenu.add_command(label="Save", command=self.save_file)
        self.fileMenu.add_command(label="Open", command=self.open_file)
        self.fileMenu.add_command(label="Exit", command=self.exit)

        # Edit dropdown menu
        self.editMenu = Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Edit", menu=self.editMenu)
        self.editMenu.add_command(label="Select All", command=self.select_all)
        self.editMenu.add_command(label="Undo", command=self.edit_undo)

        # Format dropdown menu
        self.formatMenu = Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Format", menu=self.formatMenu)
        self.formatMenu.add_command(label="Change Font", command=self.change_font)
        self.formatMenu.add_command(label="Edit Margins", command=self.change_margins)
        self.formatMenu.add_command(label="Add Line Numbers", command=self.add_line_numbers)

        # Tools dropdown menu
        self.toolsMenu = Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Tools", menu=self.toolsMenu)
        self.toolsMenu.add_command(label="Spell")

        # Help dropdown menu
        self.helpMenu = Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label='Help', menu=self.helpMenu, command=self.tutorial_window)
        self.helpMenu.add_command(label="Information", command=self.information_window)
        self.helpMenu.add_command(label="Tutorial", command=self.tutorial_window)

    def save_file(self):
        save_gui = Tk()
        save_gui.geometry('600x400')
        save_gui.mainloop()
        return None

    """
    Method: tutorial_window
    Description: Creates a popup window to give the user a quick guide for the application
    Return: None 
    """

    def tutorial_window(self):
        tut_popup = Tk()
        tut_popup.geometry('300x200')
        helper_text = "Insert your text into the typing window. Use the edit tab to change text properties." \
                      "Save with the file tab. "
        label1 = Label(tut_popup, text=helper_text, wraplength=200).pack()
        tut_popup.mainloop()
        return None

    """
    """

    def information_window(self):
        info_popup = Tk()
        info_popup.geometry('600x400')
        info_popup.mainloop()
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
