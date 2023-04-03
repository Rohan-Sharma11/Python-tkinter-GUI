from tkinter import *
parent=Tk()

def menuWidget():
    mylbl=Label(parent,text="this is menu widget")
    mylbl.pack()

Mobject=Menu(parent)
Mobject.add_command(label="computer",command=menuWidget)
Mobject.add_command(label="Exit",command=parent.quit)

parent.config(menu=Mobject)
parent.mainloop()