from tkinter import *
window = Tk()
window.title("My Code")
v = IntVar()
def abc():
    print(v.get())
rb1 = Radiobutton(window, text = "Yes", value = 1,variable = v)
rb1.pack()
rb2 = Radiobutton(window, text = "No", value = 0, variable = v)
rb2.pack()
b1 = Button(window, text = "Enter", command = abc, bg = "yellow")
b1.pack()
window.mainloop()