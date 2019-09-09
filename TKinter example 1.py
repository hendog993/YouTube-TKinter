from tkinter import Entry, Button, Text, Label, Tk, END, RAISED 

root = Tk()




# Create title label
title_label = Label(root, text="Title")
title_label.pack(anchor='n')

# Create title entry 
title_entry = Entry(root, width=25)
title_entry.pack(anchor='nw')

# Create save button and function 
def save():
    # Get contents of title entry and text entry
    # Create a file to write these contents to, with title from title box. 
    file_title = title_entry.get()
    file_contents = text_entry.get(0.0, END)
    with open(file_title + ".txt", "w") as file:
        file.write(file_contents)
        print("File successfully created")
        file.close()
    pass 

save_button = Button(root, text="Save", command=save)
save_button.pack()


# Create text entry 
text_entry = Text(root, width=40, height=30, border=4, relief=RAISED)
text_entry.pack()


root.mainloop() 
