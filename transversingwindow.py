from tkinter import *
def main1():
    w1_root=Tk()
    w1_root.title("Student Information")
    w1_root.minsize(400,360)
    w1_root.geometry("500x300")

    L1=Label(w1_root,text="Name : Rohan",padx=3,pady=5).pack()
    L2=Label(w1_root,text="Roll NO : 2506",padx=3,pady=5).pack()
    L3=Label(w1_root,text="Class : FYBSC CS",padx=3,pady=5).pack()
    btn1=Button(w1_root,text="Next Window",command=main2).pack()
    w1_root.mainloop()

def main2():
    w2_root=Tk()
    w2_root.title("Endcation Details")
    w2_root.minsize(400,300)
    w2_root.geometry("500x300")

    L1=Label(w2_root,text="College : TCSC",padx=3,pady=5).pack()
    L2=Label(w2_root,text="Subject : GUI Python",padx=3,pady=5).pack()
    L3=Label(w2_root,text="Location : Kandivali East",padx=3,pady=5).pack()
    
    btn1=Button(w2_root,text="Previous Window",command=main1,padx=2,pady=2).pack()
    btn2=Button(w2_root,text="Next Window",command=main3,padx=2,pady=2).pack()
    w2_root.mainloop()

def main3():
    w3_root=Tk()
    w3_root.title("Hobbies")
    w3_root.minsize(400,360)
    w3_root.geometry("500x300")
    L1=Label(w3_root,text="Listening to songs",padx=3,pady=5).pack()
    L2=Label(w3_root,text="Watching Movies",padx=3,pady=5).pack()
    L3=Label(w3_root,text="Playing Video Games",padx=3,pady=5).pack()

    B1=Button(w3_root,text="Previous Window",command=main2,padx=2,pady=2).pack()
    B2=Button(w3_root,text="Next Window",command=main1,padx=2,pady=2).pack()
    w3_root.mainloop()

main1()