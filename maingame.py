import os
from tkinter import *

def withTkinter():
    os.startfile(r"data\\programs\game with tkinter.py")
    root.destroy()

def withoutTkinter():
    os.startfile(r"data\programs\game.py")
    root.destroy()
 
root = Tk()

root.geometry("500x400")
root.resizable(0,0)

topFrame = Frame(root, width=500, height=50,bg="grey")
topFrame.place(x=0,y=0)
tkinterFrame = Frame(root, width=500, height=175,bg="teal")
tkinterFrame.place(x=0,y=50)
cliFrame = Frame(root, width=500, height=175,bg="teal")
cliFrame.place(x=0,y=225)


Label(topFrame,text="Select Your Preference Mode", font="comicsansms 15 bold", fg="white", bg="grey").place(x=110,y=5)


imageWithTkinter=PhotoImage(file=r"data\img\withTkinter.png")
imageWithoutTkinter=PhotoImage(file=r"data\img\withoutTkinter.png")

buttonWithTkinter = Button(tkinterFrame, text="With Tkinter", font="comicsansms 15 bold", fg="black",command=withTkinter)
buttonWithTkinter.place(x=50,y=50)

Label(tkinterFrame, image=imageWithTkinter).place(x=300)



buttonWithoutTkinter = Button(cliFrame, text="Without Tkinter", font="comicsansms 15 bold", fg="black" ,command=withoutTkinter)
buttonWithoutTkinter.place(x=35,y=50)
Label(cliFrame, image=imageWithoutTkinter).place(x=215,y=5)

root.mainloop()