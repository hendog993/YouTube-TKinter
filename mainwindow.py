from tkinter import *
from os import path as ospath 
 

_root = Tk()

software_information = {
	'Author ': "Henry Gilbert",
	'Date Created ': " 9-16-2019",
	'System Version ': 1.01
}

# TODO add executable functionality instead of just a script
# TODO add path functionality to save and load methods
# TODO add keybindings for event listener shortcuts 

def main():
	gui = Window(_root)
	gui.root.mainloop()
	return None 
	
	

def check_if_file_exists(file_name):
	if ospath.exists(file_name+'.txt'):
		return 1
	return 0

def coming_soon():
	PopupWindowAlert("Sorry!","This functionality coming soon!")
	return None 

class Window:
	list_of_fonts = ['Times', 'Calibri', 'Comic Sans', "Helvetica"]
	
	def __init__(self, root):
		self.root = root
		self.root.geometry('900x600')
		self.root.title("TKinter NotePad")
		
		# Basic textbox
		self.textspace = Text(self.root, width=100, height=90, padx=2, pady=2, border=4, relief=RAISED)
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
		self.editMenu.add_command(label="Search", command=self.edit_search)
		self.editMenu.add_command(label="Undo", command=self.edit_undo)
		self.editMenu.add_command(label='Redo', command=self.edit_redo)
		
		# Format dropdown menu
		self.formatMenu = Menu(self.menu, tearoff=0)
		self.menu.add_cascade(label="Format", menu=self.formatMenu)
		self.formatMenu.add_command(label="Change Font", command=self.change_font_window)
		self.formatMenu.add_command(label="Edit Margins", command=self.change_margins)
		self.formatMenu.add_command(label="Add Line Numbers", command=self.add_line_numbers)
		
		# Tools dropdown menu
		self.toolsMenu = Menu(self.menu, tearoff=0)
		self.menu.add_cascade(label="Tools", menu=self.toolsMenu)
		self.toolsMenu.add_command(label="Spell", command=self.check_spelling)
		
		# Help dropdown menu
		self.helpMenu = Menu(self.menu, tearoff=0)
		self.menu.add_cascade(label='Help', menu=self.helpMenu, command=self.tutorial_window)
		self.helpMenu.add_command(label="Information", command=self.information_window)
		self.helpMenu.add_command(label="Tutorial", command=self.tutorial_window)
	
	"""
	Method: save_file_window
	Nested Method: save_new_file
	Description:
		Creates a new window allowing user to declare file name to save. If a similar file name already 
		exists, the user is asked if the previous file is desired to be overwritten. If the user selects no,
		the nested function will return 0 and not proceed to the open block. If the user selects yes, the 
		open block will start and the new file will be saved. If a similar file is not detected, the open
		block will proceed as normal. After the file is saved, the save_gui is destroyed, and a popup appears
		notifying the user that the file was successfully saved. 
	Return: None
	"""
	
	def save_file_window(self):
		save_gui = Tk()
		save_gui.geometry('600x400')
		file_contents = self.textspace.get(0.0, END)
		
		def save_new_file():
			if check_if_file_exists(file_name.get()) == 1:  # If the file DOES exist already 
				
				def submit_button():
					with open(file_name.get() + '.txt', 'w+') as file:
					# Saves the file even though the file already exists. Seems inefficient. 
						file.write(file_contents)
						file.close()
						root.destroy()
						save_gui.destroy()
						PopupWindowAlert("Congrats!", "File was saved successfully!")
					return 0  
					
				def cancel_button():
					print("Cancelled")
					root.destroy()
					return 0 
					 
				root = Tk()
				root.geometry('300x300')
				root.title("Save")
				Label(root, text="File Already Exists. Do you want to overwrite?").pack()
				
				status_button = Button(root, text="Okay", command= submit_button)
				status_button.pack()
				
				cancel_button = Button(root, text="Cancel", command= cancel_button)
				cancel_button.pack()
				root.mainloop()
				# If yes, then continue. If no, return 0 and exit window. 
				
			with open(file_name.get() + '.txt', 'w+') as file:
				file.write(file_contents)
				file.close()
				save_gui.destroy()
				PopupWindowAlert("Congrats!", "File was saved successfully!")
			return None
				
		# Skeleton
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
	Description: 
		Loads a file based on the default path. Uses open block to insert text into main textbox. First deletes 
		the old contents of the 
		
		! Needs to prompt the user to save the file is not saved already. 

	"""
	
	def open_file(self):
		load_gui = Tk()
		load_gui.geometry('600x400')
		
		def load_new_file():
			status_window.delete(0.0, END)
			self.textspace.delete(0.0, END)
			try:
				with open(file_name.get() + '.txt', 'r') as file:
					prompt = str(file_name.get())   
					message = "File " + prompt + " was loaded successfully. "
					self.textspace.insert(0.0, file.read())
					status_window.insert(0.0, message)
			except FileNotFoundError:
				status_window.insert(0.0, "File not found. Try another name")
			return None
		
		Label(load_gui, text="File Name: ").grid(row=0, column=0)
		file_name = Entry(load_gui, width=40)
		file_name.grid(row=0, column=1)
		
		save_button = Button(load_gui, text="Load", command=load_new_file)
		save_button.grid(row=1, column=3)
		cancel_button = Button(load_gui, text="Cancel", command=load_gui.destroy)
		cancel_button.grid(row=1, column=4)
		
		status_window = Text(load_gui, width=40, height=4, border=3, relief=RAISED)
		status_window.grid(row=2, column=1)
		
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
	Method: information_window
	Description: Creates a popup window to give the user software information
	
	"""
	
	def information_window(self):
		info_popup = Tk()
		info_popup.geometry('600x400')
		info_popup.mainloop()
		return None
	
	def edit_undo(self):
		self.textspace.edit_undo()
		return None 
	
	def edit_redo(self):
		self.textspace.edit_redo()
		return None # 
	
	def edit_search(self):
		coming_soon()
		return None 
	
	def add_line_numbers(self):
		coming_soon()
		pass
	
	"""
	Method: change_font
	Description: Creates a popup window. Grabs all the text from the textbot widget, clears the textbox widget,
				 then inserts the new text into the widget with the updated font.
	"""
	
	def change_font_window(self):
		new_font_window = Tk()
		new_font_window.geometry('600x400')
		
		def change_font():
			font1 = font_listbox.get(ACTIVE )
			fontsize = tk_font_sizes.get()
			self.textspace.configure(font=(font1, int(fontsize)))
			return None
		
		
		font_listbox = Listbox(new_font_window)
		for x, y in enumerate(self.list_of_fonts):
			font_listbox.insert(x, y)
		font_listbox.pack()
		
		tk_font_sizes = StringVar(new_font_window)
		tk_font_sizes.set("12")
		list_of_font_sizes = OptionMenu(new_font_window, tk_font_sizes, "8", "10", "12", "14", "22", "30", "40")
		list_of_font_sizes.pack()
		
		submit_button = Button(new_font_window, text="Submit", command=change_font)
		submit_button.pack()
		new_font_window.mainloop()
		return None
	
	def change_highlighted_text(self):
		coming_soon()
		pass
	
	def change_margins(self):
		coming_soon()
		pass
	
	def check_spelling(self):
		coming_soon()
		pass
	
	def select_all(self):
		coming_soon()
		pass
	
	
	"""
	Method: exit
	Description: Exits the main window and prompts the user to save the file. 
	"""
	def exit(self):
		self.root.destroy()
		return None 
	
	
	pass
	
	
class PopupWindowAlert:

	def submit_button(self):
		self.root.destroy()
		return 1
		
	def cancel_button(self):
		self.root.destroy()
		return 0

		
	def __init__(self, title, message):
		self.root = Tk()
		self.root.geometry('300x300')
		self.root.title(title)
		Label(self.root, text=message).pack()
		
		self.status_button = Button(self.root, text="Okay", command= self.submit_button)
		self.status_button.pack()
		
		self.cancel_button = Button(self.root, text="Cancel", command= self.cancel_button)
		self.cancel_button.pack()
		self.root.mainloop()
		pass 

	pass 


if __name__ == "__main__":
	main()
	
