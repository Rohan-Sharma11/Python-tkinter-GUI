# from tkinter import *

# class polygon:
#     def __init__(self):
#         self.parent=Tk()
#         self.parent.geometry("500x500")
#         self.canvas=Canvas(self.parent,width=300,height=300)
#         self.canvas.create_polygon(60,20,100,20,140,60,140,100,140,60,20,100,20,60)
#         self.canvas.pack()
# object_p=polygon()


from tkinter import *

class polygon:
    def __init__(self):
        self.parent=Tk()
        self.parent.geometry("500x500")
        self.canvas=Canvas(self.parent,width=300,height=300)
        self.canvas.create_polygon(100, 10, 150, 50, 150, 150, 50, 150, 50, 50, fill="red", outline="black")
        self.canvas.pack()
        self.parent.mainloop()  # Added mainloop() call

object_p=polygon()
