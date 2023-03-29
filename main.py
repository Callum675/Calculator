from tkinter import *

# Function to calculate the result
def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, END)
        entry.insert(0, result)
    except:
        entry.delete(0, END)
        entry.insert(0, "Error")

# Create the GUI
root = Tk()
root.title("Calculator")

entry = Entry(root, width=35, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: entry.insert(END, "1"))
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: entry.insert(END, "2"))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: entry.insert(END, "3"))
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: entry.insert(END, "4"))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: entry.insert(END, "5"))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: entry.insert(END, "6"))
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: entry.insert(END, "7"))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: entry.insert(END, "8"))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: entry.insert(END, "9"))
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: entry.insert(END, "0"))

button_add = Button(root, text="+", padx=39, pady=20, command=lambda: entry.insert(END, "+"))
button_subtract = Button(root, text="-", padx=41, pady=20, command=lambda: entry.insert(END, "-"))
button_multiply = Button(root, text="*", padx=40, pady=20, command=lambda: entry.insert(END, "*"))
button_divide = Button(root, text="/", padx=41, pady=20, command=lambda: entry.insert(END, "/"))

button_clear = Button(root, text="Clear", padx=79, pady=20, command=lambda: entry.delete(0, END))
button_equal = Button(root, text="=", padx=91, pady=20, command=calculate)

# Put the buttons on the screen
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)

button_add.grid(row=5, column=0)
button_subtract.grid(row=6, column=0)
button_multiply.grid(row=6, column=1)
button_divide.grid(row=6, column=2)

button_clear.grid(row=4, column=1,columnspan=2)
button_equal.grid(row=5, column=1, columnspan=2)

#Start the GUI
root.mainloop()