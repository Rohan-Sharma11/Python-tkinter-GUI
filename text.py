from tkinter import *

class text:
    def __init__(self):
        self.parent=Tk()
        self.parent.geometry("500x500")
        self.canvas=Canvas(self.parent,width=400,height=400)
        self.canvas.create_text(200,10,text="Displaying geometrical shapes")
        self.canvas.pack()
        self.parent.mainloop()
text()