from tkinter import *

class rectangle:
    def __init__(self):
        self.parent=Tk()
        self.parent.geometry("500x500")
        self.canvas=Canvas(self.parent,width=400,height=400)
        self.canvas.create_rectangle(60,30,10,00,outline="blue",fill="grey")
        self.canvas.pack()
        self.parent.mainloop()
rectangle()