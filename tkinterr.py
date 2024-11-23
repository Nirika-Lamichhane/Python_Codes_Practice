from tkinter import *
from PIL import Image, ImageTk

# create the  main window
hlo_root =Tk() 
hlo_root.geometry("944x434")

# to change the title of the gui
hlo_root.title("My GUI with Harry")
title_label=Label (text='''
Vijay is an Indian actor, playback singer \n
and politician who works in Tamil cinema.\n
 He made his cinematic debut in 1984 with Vetri, directed by his father,\n
 Chandrasekhar. After appearing in Chandrasekhar's films as a child artist, \n
 Vijay made his debut as a lead actor with Naalaiya Theerpu (1992) at the age of 18.\n
 He followed it with a role opposite Vijayakanth in Senthoorapandi (1993).
                   ''', bg="red",fg="blue", padx=23, pady=43, font="comicssansms 21 bold",
                   borderwidth=3, relief= SUNKEN
)

title_label.pack(side=BOTTOM, anchor="sw",fill="x",padx=23, pady=45)
title_label.pack(side=LEFT,fill="y")

# load the png image
photo =PhotoImage(file= "1.png")
nirika_label =Label (image = photo)
nirika_label.pack()

# set minimum and maximum window size
hlo_root.minsize(400,100)
hlo_root.maxsize(1500,988)

#  creating label with text
nirika= Label(text= "Nirika is a good girl and this is her GUI")
nirika.pack()

# load a jpg image using pillow
image=Image.open("photo.jpg")
photo_jpg=ImageTk.PhotoImage(image)

# create a label to display the jpg image
nirika_label_jpg =Label(image=photo_jpg)
nirika_label_jpg.pack()

# keep reference to the images to prevent the garbae collection
nirika_label.photo=photo
nirika_label_jpg.photo_jpg= photo_jpg

# start the gui event loop
hlo_root.mainloop() #root matra lekhna ni milxa variable name ho




'''
esle simple gui banaidinxa jasma hamle add garne ho
yo class ho Tk
gemoetry ma order width x height hunxa
minsize will take width, height
yo part ma label lekhda gui ma audaina if we donot pack them
so pack garnu parxa label haru

label needs to be packed to be shown in the gui

label are those in the gui interface in which the users donot interact 
photoimage vaneko class ho 

tkinter le directly photo lai jpg format ma lidaina error dekhauxa


label ra pack are functions and its attributes are:

1) Important label options
text= adds the text
bd = background  yo lekhda ni chalxa
fg= foreground
font= sets the font
padx= x padding (x direction ko )
pady = y axis ma padding
relief= border styling = SUNKEN ,RAISED,GROOVE,RIDGE

font lekhne 2 ota style xa:
a) first one chai tuple ko form ma lekhne:
font=("comicssansms",21,"bold")

b) font="comicssansms 21 bold"

2) Important pack options

anchor= "nw"
side= top,bottom,left,right
fill
padx
pady



anchor that takes the northeast like directions as ne
southeast ma se lekhda tala aunu parne ho tara taala audaina
as it is described by the another side attribute..
by default hamro top ma hunxa


'''