from tkinter import *
root = Tk()
root.title("Option Menu")
root.geometry('700x500')

# Create the list of questions  done
# Pass them into an option menu
# Create an entry for answer
# Create submit button

def print_answers():
	print("Q: {}   A: {} ".format(tkvarq.get(), answer_entry.get()))
	return None

questions = ["What is your mother's maiden name?",
            "Who is your favorite author? ",
            "What was your first pets name? ",
            "What street did you grow up on? "
]

tkvarq = StringVar(root)
tkvarq.set(questions[0])
question_menu = OptionMenu(root, tkvarq, *questions)
question_menu.pack()

# Answer entry
answer_entry = Entry(root, width=30)
answer_entry.pack()

# Submit button
submit_button = Button(root, text='Submit', command=print_answers)
submit_button.pack()

root.mainloop()