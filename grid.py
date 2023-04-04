'''Using the grid manager is easy. Just create the widgets, and use the 
grid method to tell the manager in which row and column to place them'''

from tkinter import *

root=Tk()

label1=Label(root,text="Hello there!").grid(row=0,column=0)
label2=Label(root,text="I am rohan sharma").grid(row=1,column=0)
# another method of using grid
#label1.grid(row=0,column=0)
#label2.grid(row=1,column=0) 
root.mainloop()