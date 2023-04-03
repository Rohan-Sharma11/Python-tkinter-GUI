from tkinter import *
root=Tk()
root.geometry("600x500")
def radiobtn():
    print("you clicked the radio button")

radio_button=Radiobutton(root,text="Rdio",bg="skyblue",command=radiobtn,relief="raised",padx=3,pady=2,selectcolor="yellow",state="active")
radio_button.pack()

root.mainloop()