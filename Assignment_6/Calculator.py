import tkinter as tk
from tkinter import Entry, Button

window = tk.Tk()
window.title("Calculator")
window.minsize(500,500)

e = Entry(width=56, borderwidth=5)
e.place(x=0,y=0)

def click(num):
    res = e.get()
    e.delete(0,"end")
    e.insert(0,str(res)+ str(num))

b = Button(text="1", width=12, command=lambda:click(1))
b.place(x=10, y= 60)

b = Button(text="2", width=12, command=lambda:click(2))
b.place(x=80, y= 60)

b = Button(text="3", width=12, command=lambda:click(3))
b.place(x=170, y= 60)

b = Button(text="4", width=12, command=lambda:click(4))
b.place(x=10, y= 120)

b = Button(text="5", width=12, command=lambda:click(5))
b.place(x=80, y= 120)

b = Button(text="6", width=12, command=lambda:click(6))
b.place(x=170, y= 120)

b = Button(text="7", width=12, command=lambda:click(7))
b.place(x=10, y= 180)

b = Button(text="8", width=12, command=lambda:click(8))
b.place(x=80, y= 180)

b = Button(text="9", width=12, command=lambda:click(9))
b.place(x=170, y= 180)

b = Button(text="0", width=12, command=lambda:click(0))
b.place(x=10, y= 240)

#operators

def add():
    global n1
    n1=e.get()
    global math
    math = "addition"
    e.delete(0,"end")


b = Button(text="+", width=12, command=add)
b.place(x=80, y= 240)

def sub():
    global n1
    n1 = e.get()
    global math
    math = "subtraction"
    e.delete(0, "end")

b = Button(text="-", width=12, command=sub)
b.place(x=170, y= 240)

def mul():
    global n1
    n1 = e.get()
    global math
    math = "multiplication"
    e.delete(0, "end")

b = Button(text="*", width=12, command=mul)
b.place(x=10, y= 300)

def div():
    global n1
    n1 = e.get()
    global math
    math = "division"
    e.delete(0, "end")

b = Button(text="/", width=12, command=div)
b.place(x=80, y= 300)

def equal():
    n2 = e.get()
    e.delete(0, "end")
    if math == "addition":
        e.insert(0, int(n1) + int(n2))
    elif math == "subtraction":
        e.insert(0, int(n1) - int(n2))
    elif math == "multiplication":
        e.insert(0, int(n1) * int(n2))
    elif math == "division" and int(n2)==0:
        e.insert(0, "Undefined")
    elif math == "division":
        e.insert(0, int(n1) / int(n2))


b = Button(text="=", width=12, command=equal)
b.place(x=170, y= 300)

def clear():
    e.delete(0, "end")

b = Button(text="clear", width=12, command=clear)
b.place(x=10, y= 350)

window.mainloop()