from tkinter import *

class arc:
    def __init__(self):
        self.parent=Tk()
        self.parent.geometry("500x500")
        self.canvas=Canvas(self.parent,width=400,height=400)
        self.canvas.create_arc(200,20,20,200)
        self.canvas.pack()
        self.parent.mainloop()
arc()