from tkinter import *
root=Tk()
root.geometry("500x400")

def msg():
    lbl=Label(root,text="You clicked the button").pack()

root.config()
var=IntVar()
radiobtn1=Radiobutton(root,text="Submit",bg="skyblue",fg="blue",command=msg,value=1,variable=var)
radiobtn1.pack()

radiobtn2=Radiobutton(root,text="Reset",bg="skyblue",fg="blue",command=msg,variable=var)
radiobtn2.pack()

root.mainloop()
