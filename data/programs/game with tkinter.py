import time,random,os
from tkinter import *

def restart():
    root.destroy()
    os.startfile(r"data\programs\game with tkinter.py")
    
def disableButton():
    global l,restartButton,start
    b1.config(state="disabled")
    b2.config(state="disabled")
    b3.config(state="disabled")
    b4.config(state="disabled")
    b5.config(state="disabled")
    b6.config(state="disabled")
    b7.config(state="disabled")
    b8.config(state="disabled")
    b9.config(state="disabled")
    start.config(state="disabled")
    restartButton.config(state="normal",command=restart,text=" --->press to restart<---   ")
    
def funForB1():
    global notPresentList,element,l,start
    ans = notPresentList[0] == element
    if ans:
        l.config(image=image1)
    else:
        l.config(image=image2)
    disableButton()

def funForB2():
    global notPresentList,element,l
    ans = notPresentList[1] == element
    if ans:
        l.config(image=image1)
    else:
        l.config(image=image2)
    disableButton()

def funForB3():
    global notPresentList,element,l
    ans = notPresentList[2] == element
    if ans:
 
        l.config(image=image1)
    else:

        l.config(image=image2)
    disableButton()

def funForB4():
    global notPresentList,element,l
    ans = notPresentList[3] == element
    if ans:

        l.config(image=image1)
    else:

        l.config(image=image2)
    disableButton()

def funForB5():
    global notPresentList,element,l
    ans = notPresentList[4] == element
    if ans:

        l.config(image=image1)
    else:

        l.config(image=image2)
    disableButton()

def funForB6():
    global notPresentList,element,l
    ans = notPresentList[5] == element
    if ans:

        l.config(image=image1)
    else:

        l.config(image=image2)
    disableButton()

def funForB7():
    global notPresentList,element,l
    ans = notPresentList[6] == element
    if ans:
        l.config(image=image1)
    else:
        l.config(image=image2)
    disableButton()

def funForB8():
    global notPresentList,element,l
    ans = notPresentList[7] == element
    if ans:
        l.config(image=image1)
    else:
        l.config(image=image2)
    disableButton()

def funForB9():
    global notPresentList,element,l
    ans = notPresentList[8] == element
    if ans:
        l.config(image=image1)
    else:
        l.config(image=image2)
    disableButton()


def present():
    with open(r"data\database\present.txt", "r") as file:
        content = file.read().split("\n")
        presentList = [
           content[random.randint(0,400)],
            content[random.randint(0,400)],
            content[random.randint(0,400)],
           content[random.randint(0,400)],
            content[random.randint(0,400)],
            content[random.randint(0,400)],
           content[random.randint(0,400)],
            content[random.randint(0,400)],
            content[random.randint(0,400)]
             ]
        
        element = presentList[random.randint(0,8)]
        return (presentList,element)

def notPresent():
    global buttonList,start
    with open(r"data\database\notpresent.txt","r") as file:
        content = file.read().split("\n")
        notPresentList = [
            content[random.randint(0,400)],
            content[random.randint(0,400)],
            content[random.randint(0,400)],
            content[random.randint(0,400)],
            content[random.randint(0,400)],
            content[random.randint(0,400)],
            content[random.randint(0,400)],
            content[random.randint(0,400)],
             ]
        start.config(state="normal")
        obj = present()
        presentList,element = obj[0],obj[1]
        for i in range(9):
            buttonList[i].config(text = presentList[i], state="disabled")
        notPresentList.insert(random.randint(0,9),element)

        return (notPresentList,element)

def start():
    global buttonList,start,notPresentList,element
    start.config(state="disabled")

    for i in range(9):
        buttonList[i].config(text = notPresentList[i], state="normal")

    
    

            
# main

root =Tk()
root.title("Memory Game")
root.geometry("400x500")
root.resizable(0,0)
root.config(bg="white")

image1 = PhotoImage(file=r"data\img\smiley.png")
image2 = PhotoImage(file=r"data\img\pleading.png")


start = Button(root, bg="black", fg="white", text="-->Start<--", font="comicsansms 15 bold", command=start, relief="raised",state="normal", bd=2)
start.place(x=150,y=110)



frameMain = Frame(root, relief="flat", bd=1, background="white", width=400, height=417)
frameMain.place(x=10, y=150)


image=PhotoImage(file=r"data\img\emoji.png")
l=Label(root,image=image ,font="comicsansms 15 bold", fg="black", bg="white")
l.place(x=180,y=5)

b1=Button(frameMain, bg='cyan', text="plz start", fg="white", width=10, height=5, relief='raised',bd=3, state="normal",disabledforeground="white",command = funForB1)
b2=Button(frameMain, bg='teal', text="plz start", fg="white", width=10, height=5, relief='raised',bd=3, state="normal",disabledforeground="white",command = funForB2)
b3=Button(frameMain, bg='cyan', text="plz start", fg="white", width=10, height=5, relief='raised',bd=3, state="normal",disabledforeground="white",command = funForB3)
b4=Button(frameMain, bg='teal', text="plz start", fg="white", width=10, height=5, relief='raised',bd=3, state="normal",disabledforeground="white",command = funForB4)
b5=Button(frameMain, bg='cyan', text="plz start", fg="white", width=10, height=5, relief='raised',bd=3, state="normal",disabledforeground="white",command = funForB5)
b6=Button(frameMain, bg='teal', text="plz start", fg="white", width=10, height=5, relief='raised',bd=3, state="normal",disabledforeground="white",command = funForB6)
b7=Button(frameMain, bg='cyan', text="plz start", fg="white", width=10, height=5, relief='raised',bd=3, state="normal",disabledforeground="white",command = funForB7)
b8=Button(frameMain, bg='teal', text="plz start", fg="white", width=10, height=5, relief='raised',bd=3, state="normal",disabledforeground="white",command = funForB8)
b9=Button(frameMain, bg='cyan', text="plz start", fg="white", width=10, height=5, relief='raised',bd=3, state="normal",disabledforeground="white",command = funForB9)


b1.place(x=10,y=16)
b2.place(x=150,y=16)
b3.place(x=290,y=16)
b4.place(x=10,y=110)
b5.place(x=150,y=110)
b6.place(x=290,y=110)
b7.place(x=10,y=204)
b8.place(x=150,y=204)
b9.place(x=290,y=204)

buttonList = [b1,b2,b3,b4,b5,b6,b7,b8,b9]


restartButton = Button(root, bg="teal", fg="white", text="!!! Remember these items !!!", font="comicsansms 15 bold", relief="raised",state="disabled",disabledforeground="white")
restartButton.place(x=60,y=460)
obj = notPresent()
notPresentList,element = obj[0],obj[1]

root.mainloop()
