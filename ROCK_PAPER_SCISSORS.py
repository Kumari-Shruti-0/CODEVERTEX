from tkinter import *
import random
root=Tk()
root.geometry("300x300")

def winner():
    user=var.get()
    choice=["Stone","Paper","Scissor"]
    system=random.choice(choice)
    winner_entry.delete(0, END)
    if(user=="Stone" and system=="Scissor" or user=="Scissor" and system=="Paper" or user=="Paper" and system=="Stone"):
        winner_entry.insert(0,f"You Win!! System chose {system}")
    elif(user==system):
        winner_entry.insert(0,f"DRAW. Both chose {system}")
    else:
        winner_entry.insert(0,f"You Lose!! System chose {system}")

var=StringVar()
var.set("Radio")

Label(root,text="What is your choice ?",font="lucida 19 bold",justify=LEFT,padx=14).pack()
radio=Radiobutton(root,text="Stone",padx=14,variable=var,value="Stone").pack(anchor="w")
radio=Radiobutton(root,text="Paper",padx=14,variable=var,value="Paper").pack(anchor="w")
radio=Radiobutton(root,text="Scissors",padx=14,variable=var,value="Scissor").pack(anchor="w")

Button(text="Submit",command=winner).pack()

winner_entry= Entry(root, width=30)
winner_entry.pack(padx=10, pady=10)

root.mainloop()