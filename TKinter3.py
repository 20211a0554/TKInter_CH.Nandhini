from tkinter import *
window = Tk()
window.title("My Code")
window.minsize(width = 200, height = 400)
window.maxsize(width = 600, height = 1000)
lb1 = Listbox(window, width = 20, bg = "Light Blue")
list1 = ["Nandhini", "Navadeep", "Saritha", "Rajireddy", "sammakka", "Mallareddy","haha"]
for i in list1:
    lb1.insert(END, i)
lb1.pack()
def remove():
    lb1.delete(ANCHOR)
b1 = Button(window, text = "Remove", command = remove)
b1.pack()
window.mainloop()