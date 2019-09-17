from tkinter import *
import os

_root = Tk()


# TODO add executable functionality instead of just a script
# TODO add path functionality to save and load methods

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
        self.fileMenu.add_command(label="Save", command=self.save_file_window)
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

    """
    Method: save_file
    Description: Opens a popup window that allows the user to save a file. Uses the open block to save
                 and create a new file. 
    TODO: if the file already exists, use w+ mode. 
    Return: None 
    """

    def save_file_window(self):
        save_gui = Tk()
        save_gui.geometry('600x400')
        file_contents = self.textspace.get(0.0, END)

        def save_new_file(text=file_contents):
            with open(file_name.get() + '.txt', 'w+') as file:
                file.write(file_contents)
                file.close()
            return None

        Label(save_gui, text="File Name: ").grid(row=0, column=0)
        file_name = Entry(save_gui, width=40)
        file_name.grid(row=0, column=1)

        Label(save_gui, text="Directory: ").grid(row=1, column=0)
        save_directory = Entry(save_gui, width=40)
        save_directory.grid(row=1, column=1)

        save_button = Button(save_gui, text="Save", command=save_new_file)
        save_button.grid(row=1, column=3)
        cancel_button = Button(save_gui, text="Cancel", command=save_gui.destroy)
        cancel_button.grid(row=1, column=4)

        save_gui.mainloop()
        return None

    """
    Method: open_file
    Description: Loads a file based on the default path. Uses open block to insert text into main textbox.
    Return: None 
    """

    def open_file(self):
        load_gui = Tk()
        load_gui.geometry('600x400')

        def load_new_file():
            with open(file_name.get() + '.txt', 'r') as file:
                pass
            # Write the file contents to the text box. Use insert method. Delete previous contents.
            return None

        Label(load_gui, text="File Name: ").grid(row=0, column=0)
        file_name = Entry(load_gui, width=40)
        file_name.grid(row=0, column=1)

        save_button = Button(load_gui, text="Load", command=load_new_file)
        save_button.grid(row=1, column=3)
        cancel_button = Button(load_gui, text="Cancel", command=load_gui.destroy)
        cancel_button.grid(row=1, column=4)

        load_gui.mainloop()
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
