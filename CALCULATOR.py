from tkinter import *
root=Tk()
root.geometry("330x420")
root.minsize(330,420)
root.maxsize(330,420)
root.title("Calculator")
root.wm_iconbitmap("bitimage.png")

def click(e):
    global scvalue
    text=e.widget.cget("text")
    print(text)
    if text=="=":
        if scvalue.get().isdigit():
            value=int(scvalue.get())
        else:
            try:
                value=eval(screen.get())
            except Exception as e:
                print(e)
                value="ERROR"
        scvalue.set(value)
        screen.update()
        
    elif text =="C":
        scvalue.set("")
        screen.update()
    else:
        scvalue.set(scvalue.get()+text)
        screen.update()
    
scvalue=StringVar()
scvalue.set("")
screen=Entry(root,textvar=scvalue,font="lucida 30 bold")
screen.pack(fill=X,padx=10,pady=20)

f=Frame(root,bg="grey")
b=Button(f,text="9",padx=28,pady=22 ,font="bold")
b.pack(side=LEFT)
b.bind("<Button-1>",click)

b=Button(f,text="8",padx=28,pady=22 ,font="bold")
b.pack(side=LEFT)
b.bind("<Button-1>",click)

b=Button(f,text="7",padx=28,pady=22 ,font="bold")
b.pack(side=LEFT)
b.bind("<Button-1>",click)

b=Button(f,text="C",padx=28,pady=22 ,font="bold")
b.pack(side=LEFT)
b.bind("<Button-1>",click)

f.pack()

f=Frame(root,bg="grey")
b=Button(f,text="6",padx=28,pady=22 ,font="bold")
b.pack(side=LEFT)
b.bind("<Button-1>",click)

b=Button(f,text="5",padx=28,pady=22 ,font="bold")
b.pack(side=LEFT)
b.bind("<Button-1>",click)

b=Button(f,text="4",padx=28,pady=22 ,font="bold")
b.pack(side=LEFT)
b.bind("<Button-1>",click)

b=Button(f,text="/",padx=28,pady=22 ,font="bold")
b.pack(side=LEFT)
b.bind("<Button-1>",click)

f.pack()

f=Frame(root,bg="grey")
b=Button(f,text="3",padx=28,pady=22 ,font="bold")
b.pack(side=LEFT)
b.bind("<Button-1>",click)

b=Button(f,text="2",padx=28,pady=22 ,font="bold")
b.pack(side=LEFT)
b.bind("<Button-1>",click)

b=Button(f,text="1",padx=28,pady=22 ,font="bold")
b.pack(side=LEFT)
b.bind("<Button-1>",click)

b=Button(f,text="%",padx=28,pady=22 ,font="bold")
b.pack(side=LEFT)
b.bind("<Button-1>",click)

f.pack()

f=Frame(root,bg="grey")
b=Button(f,text="+",padx=28,pady=22 ,font="bold")
b.pack(side=LEFT)
b.bind("<Button-1>",click)

b=Button(f,text="0",padx=28,pady=22 ,font="bold")
b.pack(side=LEFT)
b.bind("<Button-1>",click)

b=Button(f,text="-",padx=28,pady=22 ,font="bold")
b.pack(side=LEFT)
b.bind("<Button-1>",click)

b=Button(f,text="=",padx=28,pady=22 ,font="bold")
b.pack(side=LEFT)
b.bind("<Button-1>",click)

f.pack()

root.mainloop()
