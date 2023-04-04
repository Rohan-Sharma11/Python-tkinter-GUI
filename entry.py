from tkinter import *
root = Tk()
e = Entry(root,width=20,borderwidth=7)
e.pack()
e.insert(0,"Enter your name ")
def myButton():
    #hello = "hello "+ e.get()
    myLabel = Label(root,text="hello"+e.get())
    myLabel.pack()
btn = Button(root,text="Enter your name",bg="skyblue",command=myButton)
btn.pack()
root.mainloop()