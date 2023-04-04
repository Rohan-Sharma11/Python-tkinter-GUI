from tkinter import *
class line:
    def __init__(self):
        self.parent=Tk()
        self.parent.geometry("500x500")
        self.canvas=Canvas(self.parent,height=400,width=400)
        self.canvas.create_line(60,20,20,60)
        self.canvas.pack()
        self.canvas.mainloop()
obj_line=line()