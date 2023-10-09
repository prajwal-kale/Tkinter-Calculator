from tkinter import *
from tkinter import messagebox

data= " "


def press(num):
    global data
    data= data+str(num) 
    value.set(data) #updation of the expression using set method


def equal():
    try:
        global data
        total_sum = str(eval(data))
        value.set(total_sum)
        data=""
    except:
        data="error"
        value.set(data)
        data=""

def clear():
    global data
    data=""
    value.set("")


if __name__ == "__main__":
    t=Tk()
    t.configure(background="#d5e8f9")
    t.title("WorkSpace")
    t.geometry("500x400")
    
    f0=Frame(bg="#d5e8f9")
    f0.place(width=400,height=600)
    
    f=Label(f0, text="Simple Calculator",background="white",font="Arial")
    f.place(x=140,y=40)
    
    value = StringVar()
    field=Entry(t,textvariable=value)
    field.place(x=100,y=80,width=235,height=20)
    
    button1 = Button(t, text=' 1 ', fg='black', bg='red',
                    command=lambda: press(1), height=1, width=5)
    button1.place(x=105, y=105)
    
    button2= Button(t, text="2",fg="black", bg="red", command=lambda: press(2),
                    height=1,width=5)
    button2.place(x=165,y=105)
    
    button3=Button(t, text="3", fg="black", bg="red",command=lambda:press(3),
                   height=1,width=5)
    button3.place(x=225,y=105)
    
    button4 = Button(t, text='4', fg='black', bg='red',
                    command=lambda: press(4), height=1, width=5)
    button4.place(x=105, y=135)
    
    button5= Button(t, text="5",fg="black", bg="red", command=lambda: press(5),
                    height=1,width=5)
    button5.place(x=165,y=135)
    
    button6=Button(t, text="6", fg="black", bg="red",command=lambda:press(6),
                   height=1,width=5)
    button6.place(x=225,y=135)
    
    button7 = Button(t, text='7', fg='black', bg='red',
                    command=lambda: press(7), height=1, width=5)
    button7.place(x=105, y=165)
    
    button8= Button(t, text="8",fg="black", bg="red", command=lambda: press(8),
                    height=1,width=5)
    button8.place(x=165,y=165)
    
    button9=Button(t, text="9", fg="black", bg="red",command=lambda:press(9),
                   height=1,width=5)
    button9.place(x=225,y=165)
    
    button0=Button(t, text="0", fg="black", bg="red",command=lambda:press(0),
                   height=1,width=5)
    button0.place(x=105,y=195)
    
    add=Button(t, text="+", fg="black", bg="red", command=lambda:press("+"),
               height=1, width=5)
    add.place(x=285,y=105)
    
    sub=Button(t, text="-", fg="black", bg="red", command=lambda:press("-"),
               height=1, width=5)
    sub.place(x=285,y=135)
    
    mul=Button(t, text="*", fg="black", bg="red", command=lambda:press("*"),
               height=1, width=5)
    mul.place(x=285,y=165)
    
    div=Button(t, text="/", fg="black", bg="red", command=lambda:press("/"),
               height=1, width=5)
    div.place(x=285,y=195)
    
    eql=Button(t, text="=", fg="black", bg="red", command=equal,
               height=1, width=5)
    eql.place(x=225,y=195)
    
    clr=Button(t, text="clear", fg="black", bg="red", command=clear,
                 height=1, width=5)
    clr.place(x=165,y=195)
    
    
    t.mainloop()

