'''
1) 500*400 ko window bottom ma tala sano line banaune tesma ready lekheko huna parxa sanoo wala
2)different png files haru xa from 1 to any number store garne variable ma
  tyo image ko khabar xa text.file vanne ma jaslai newspaper ko form ma lekhne
'''

from tkinter import *

# creating main window
root=Tk()
root.title("Nirika's Newspaper")
root.geometry("600x800")

# create the frame to hold all the content
frame=Frame(root)
frame.pack(fill=BOTH, expand=True,padx=10,pady=10)

# function to add an image and description in a row
def add_article(image_path, description, parent):
    # create frame for each article
    article_frame =Frame(parent)
    article_frame.pack(pady=10 , fill="x")
'''
root.geometry("500x400")
label=Label (root, text="This is my window and I am ready",bg="green",font=("Arial",12))
label.pack(side=BOTTOM,fill="x",anchor=CENTER)
'''
root.mainloop()