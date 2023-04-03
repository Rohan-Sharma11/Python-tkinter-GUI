from tkinter import *
root=Tk()
root.geometry("500x500")
cbutton=Checkbutton(root,text="Check",relief="raised",fg="black",bg="sky blue",height=2,width=15,offvalue=0,onvalue=1).pack()
root.mainloop()