from tkinter import * 

root = Tk()
root.title("Flashcard Game")
root.geometry("700x500")

# Create states and capital dictionary 

states_and_capitals = { 
    'Alabama': 'Montgomery',
    'Alaska': 'Juneau',
    'Arizona':'Phoenix',
    'Arkansas':'Little Rock',
    'California': 'Sacramento',
    'Colorado':'Denver',
    'Connecticut':'Hartford',
    'Delaware':'Dover',
    'Florida': 'Tallahassee',
    'Georgia': 'Atlanta',
    'Hawaii': 'Honolulu',
    'Idaho': 'Boise',
    'Illinios': 'Springfield',
    'Indiana': 'Indianapolis',
    'Iowa': 'Des Monies',
    'Kansas': 'Topeka',
    'Kentucky': 'Frankfort',
    'Louisiana': 'Baton Rouge',
    'Maine': 'Augusta',
    'Maryland': 'Annapolis',
    'Massachusetts': 'Boston',
    'Michigan': 'Lansing',
    'Minnesota': 'St. Paul',
    'Mississippi': 'Jackson',
    'Missouri': 'Jefferson City',
    'Montana': 'Helena',
    'Nebraska': 'Lincoln',
    'Neveda': 'Carson City',
    'New Hampshire': 'Concord',
    'New Jersey': 'Trenton',
    'New Mexico': 'Santa Fe',
    'New York': 'Albany',
    'North Carolina': 'Raleigh',
    'North Dakota': 'Bismarck',
    'Ohio': 'Columbus',
    'Oklahoma': 'Oklahoma City',
    'Oregon': 'Salem',
    'Pennsylvania': 'Harrisburg',
    'Rhode Island': 'Providence',
    'South Carolina': 'Columbia',
    'South Dakoda': 'Pierre',
    'Tennessee': 'Nashville',
    'Texas': 'Austin',
    'Utah': 'Salt Lake City',
    'Vermont': 'Montpelier',
    'Virginia': 'Richmond',
    'Washington': 'Olympia',
    'West Virginia': 'Charleston',
    'Wisconsin': 'Madison',
    'Wyoming': 'Cheyenne'  
} 

# Create listbox 
listbox1 = Listbox(root)
for x, y in enumerate(states_and_capitals):
    listbox1.insert(x+1, y)
listbox1.pack(anchor='w')

def flash():
    # Delete previous entry in entry widget
    # get state from the listbox
    # insert capital into entry widget 
    entry1.delete(0, 'end')
    state = listbox1.get(ANCHOR)
    entry1.insert(0, states_and_capitals[state])
    pass 

# Create button to fetch state from selected item
button1 = Button(root, text="Flash", command=flash)
button1.pack()


# Create entry to place capital (answer)
label1 = Label(root, text="Answer").pack()
entry1 = Entry(root, width = 20)
entry1.pack()




root.mainloop()
