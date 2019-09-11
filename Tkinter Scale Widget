from tkinter import * 

root = Tk()
root.title("Slider Widget")
root.geometry('600x400')


def calculate():
    val1 = slider1.get()
    val2 = slider2.get()
    try: print("Number 1 : {} \nNumber 2 : {} \nSum: {}\nDifference:  {} \nProduct: {}\nQuotient: {}\n".format(val1, val2, val1+val2, val1-val2, val1*val2, val1/val2))
    except ZeroDivisionError:
        print("Can not divide by zero. Try another number")
    pass 


slider1 = Scale(root, from_=0, to=150, length=400, resolution=1, orient=HORIZONTAL)
slider1.pack()

slider2 = Scale(root, from_=0, to=150, length=400, resolution=1, orient=HORIZONTAL)
slider2.pack()



button1 = Button(root, text="Calculate", command=calculate)
button1.pack()

root.mainloop()
