# from tkinter import *
# class line:
#     def __init__(self):
#         self.parent=Tk()
#         self.parent.geometry("500x500")
#         self.canvas=Canvas(self.parent,height=400,width=400)
#         self.canvas.create_line(60,20,20,60)
#         self.canvas.pack()
#         self.canvas.mainloop()
# obj_line=line()


from tkinter import *

class DrawingApp:
    def __init__(self, master):
        self.master = master
        master.title("Drawing App")

        self.canvas = Canvas(master, width=700, height=500)
        self.canvas.pack()

        self.canvas.bind("<B1-Motion>", self.draw) # bind left mouse button to draw function

        clear_button = Button(master, text="Clear", command=self.clear_canvas)
        clear_button.pack()

    def draw(self, event):
        x, y = event.x, event.y
        self.canvas.create_oval(x-5, y-5, x+5, y+5, fill="black") # create an oval shape at (x, y)

    def clear_canvas(self):
        self.canvas.delete("all") # delete all objects on the canvas

root = Tk()
app = DrawingApp(root)
root.mainloop()
