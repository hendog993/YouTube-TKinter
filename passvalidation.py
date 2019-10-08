from tkinter import * 
import hashlib
import json 

def main():
	root = Tk()
	win1 = Window(root, "User Validation", '500x400')
	return None 
 

class Window:
	username = ''
	password = ''
	new_username = ''
	new_password = ''
	login_options = ["Existing User", "New User"]
	login_status = ''
	data = ''
	
	
	def __init__(self, root, title, size):
    	self.root = root
    	self.root.geometry(size)
    	self.root.title(title)
    	Label(self.root, text="Username").grid(row=0, column=0)
    	Label(self.root, text="Password").grid(row=1, column=0)
    
    	self.username_entry=Entry(self.root, width=50)
    	self.username_entry.grid(row=0, column=1)
    	self.password_entry = Entry(self.root, width=50)
    	self.password_entry.grid(row=1, column=1)
    
    	self.login_type = Spinbox(self.root, values=self.login_options)
		self.login_type.grid(row=2, column=0)
    	self.submit_button=Button(self.root, text="Submit", command=self.update_database)
    	self.submit_button.grid(row=2, column=1)
		pass 
    
    def str_to_hex_digest(self, input_string):
		result = hashlib.md5(input_string.encode())
		return result.hexdigest()
      
    def submit(self):
		self.login_status = self.login_type.get()
		self.password = self.password_entry.get()
		self.username = self.username_entry.get()
		return None 
     
    
	def new_user_creation(self):
		pass 
      
    def check_if_username_exists(self):
		pass 
    
    def existing_user_login(self):
		pass 
      
    
    def update_database(self):
		username_index = 0
		password_index = 0
		new_dic = {}
      
		with open('userdatabase.json', "w+") as file:
      		# Use the class variables here to write the new databse with new user information
        	pass 
     
    
    def popup_login_successful(self):	
		root = Tk()
		PopupWindow(root, "Login Successful")
		return None 
    
    def popup_creation_successful(self):
		root = Tk()
		PopupWindow(root, "Account Creation Successful")
		return None 
    
    def popup_username_taken(self):
		root = Tk()
		PopupWindow(root, "That username is already taken. Try another")
		return None 
    
    def popup_bad_match(self):
		root = Tk() 
		PopupWindow(root, "Your credentials do not match ours. Please try again.")
		return None 
    


class PopupWindow:
  	def __init__(self, root, message):
    	self.root = root
    	self.root.geometry('400x300')
    	self.root.title("Message")
    	Label(self.root, text=message).pack()
    	self.okay_button = Button(self.root, text="Okay", command=self.root.destroy)
    	self.okay_buton.pack()
    	self.root.mainloop()
  pass 
    
