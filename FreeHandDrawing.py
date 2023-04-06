
from tkinter import *
parent=Tk()
can_obj=Canvas(parent,height=500,width=400)
can_obj.pack(expand=YES,fill=BOTH)

def pen(event):
    fill_colour="red"
    x1,y1=event.x-1,event.y-1
    x2,y2=event.x+1,event.y+2
    can_obj.create_oval(x1,y1,x2,y2,fill=fill_colour)

def clearall():
    can_obj.delete('all')
    message.config(text="Press and drag the mouse to draw the shape") # corrected line
parent.title("Delete content")
message=Label(parent,text="Press and drag the mouse to draw the shape")
message.pack(side=BOTTOM)
can_obj.bind('<B1-Motion>',pen)
button=Button(parent,text="Clear All",command=clearall)
button.pack(side=BOTTOM)
parent.mainloop()
