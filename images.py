from tkinter import *
from tkinter.ttk import *
from PIL import ImageTk, Image
root=Tk()
root.title("images in tkinter")
root.geometry("500x500")



#root.iconphoto(False, 'abc.png')
#root.iconbitmap("photoo.png")

my_img=ImageTk.PhotoImage(Image.open('abc.png'))
my_label=Label(image=my_img)
my_label.pack()
quit_button=Button(root,text="Exit Program",command=root.quit)
quit_button.pack()
root.mainloop()