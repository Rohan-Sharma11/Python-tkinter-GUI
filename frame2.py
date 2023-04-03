from tkinter import *
root=Tk()
root.geometry("500x300")

myframe1=Frame(root).pack(side=TOP)
def button1():
    print("This is Rohan")

def button2():
    print("FYBSC CS")

def button3():
    print("2506")

b1=Button(myframe1,text="Name",command=button1).pack()
b2=Button(myframe1,text="Class",command=button2,padx=12).pack()
b3=Button(myframe1,text="Rll No",command=button3).pack()


myframe2=Frame(root).pack(side=BOTTOM)
def address():
    print("Mumbai")
def residence():
    print("Uttar Pradesh")
b1=Button(myframe2,text="Address",command=address).pack()
b2=Button(myframe2,text="Place of residence",command=residence).pack()

root.mainloop()
