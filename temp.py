from tkinter import *
root=Tk()

def func():
    lbl=Label(root,text="this is menu")
    lbl.pack()

menu_object=Menu(root)
menu_object.add_command(label="menu",command=func)
menu_object.add_command(label="exit",command=root.quit)

root.config(menu=menu_object)
root.mainloop() 