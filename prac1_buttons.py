from tkinter import *

root=Tk()
root.geometry("500x500")
def button():
    lbl=Label(root,text="Yee you clicked the button").pack()

button=Button(root,text="Clicke me",bg="skyblue",fg="blue",command=button,justify="right",padx=5,pady=3,relief="raised",font="ariel")
button.pack()

root.mainloop()