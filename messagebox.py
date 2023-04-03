from tkinter import *
from tkinter import messagebox
root=Tk()
root.title("Message Box")
root.geometry("500x400")

messagebox.showinfo("showinfo","information")
messagebox.askquestion("askquestion","do you want to quit?")
messagebox.askyesno("yes or no","say yes or no")
root.mainloop()