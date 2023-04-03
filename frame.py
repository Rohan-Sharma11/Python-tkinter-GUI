from tkinter import *
root=Tk()
root.geometry("600x300")

root.title("This is frame")

def func():
    myLabel=Label(root,text="Happy Birthday to me:)")
    myLabel.pack()

my_frame=LabelFrame(root,padx=120,pady=120)
my_frame.pack(padx=20,pady=20)
b=Button(my_frame,text="wish",bg="sky blue",fg="blue",command=func)
b.pack()

root.mainloop()