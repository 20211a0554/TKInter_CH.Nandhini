from tkinter import *
window = Tk()
window.title("My Code")
window.minsize(width = 200, height = 600)
window.maxsize(width = 600, height = 1000)
l1 = Label(window, text = "My Label", fg = "Black", bg = "Pink")
l1.place(x = 20, y = 30)
l2 = Label(window, text = "No value", fg = "Black", bg = "Light Blue")
l2.place(x = 40, y = 140)
a = StringVar()
e1 = Entry(window, width = 10, bd = 2, font = ("Corbel",18), textvariable = a)
e1.place(x = 20, y = 60)
def Tochange():
    x = a.get()
    print(x)
    l2.config(text = x, fg = "Blue", bg = "pink")
b1 = Button(window, text = "enter", fg = "Pink", bg = "Black", command = Tochange)
b1.place(x = 50, y = 100)
cb1 = Checkbutton(window, text = "male", bg = "Yellow", fg = "Black")
cb1.place(x = 20, y = 170)
cb2 = Checkbutton(window, text = "female", bg = "Yellow", fg = "black")
cb2.place(x = 100, y = 170)
window.mainloop()