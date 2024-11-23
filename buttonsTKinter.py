from tkinter import *
root =Tk()

root.geometry("655x333")
def hello():
    print("hello tkinter buttons")

def name():
    print("Name is Nirika ")
    
frame =Frame(root,borderwidth=5, bg="blue",relief="sunken")
frame.pack(side= LEFT,anchor="nw")

b1=Button(frame, fg="red",text="Click here",command =hello)
b1.pack(side=LEFT, padx=23)

b2=Button(frame, fg="red",text="Tell me your name please", command =name)
b2.pack(side=LEFT, padx=23)

b3=Button(frame, fg="red",text="Click here")
b3.pack(side=LEFT, padx=23)

b4=Button(frame, fg="red",text="Click here")
b4.pack(side=LEFT, padx=23)

root.mainloop()