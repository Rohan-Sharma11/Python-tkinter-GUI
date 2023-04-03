from tkinter import *
root=Tk()
root.title("Using grid method")
root.geometry("500x300")

science=Label(root,text="Science").grid(row=1,column=0)
Cbtn1=Checkbutton(root,text="CS").grid(row=2,column=0)
Cbtn2=Checkbutton(root,text="DS").grid(row=3,column=0)
Cbtn3=Checkbutton(root,text="IT").grid(row=4,column=0)
Cbtn4=Checkbutton(root,text="Aviation").grid(row=5,column=0)
Cbtn5=Checkbutton(root,text="Animation").grid(row=6,column=0)


def Rbttn():
    print("This is radiobutton")
commerce=Label(root,text="Commerce").grid(row=1,column=1)
Rbtn1=Radiobutton(root,text="B.Commerce",state="active").grid(row=2,column=1)
Rbtn2=Radiobutton(root,text="BMI",command=Rbttn,state="active").grid(row=3,column=1)
Rbtn3=Radiobutton(root,text="BBI",state="normal").grid(row=4,column=1)
Rbtn4=Radiobutton(root,text="BMS",state="active").grid(row=5,column=1)
Rbtn5=Radiobutton(root,text="BBA",state="normal").grid(row=6,column=1)

root.mainloop()