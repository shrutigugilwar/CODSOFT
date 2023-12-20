import random,string
from tkinter import *

#functions
def selection():
    choice.get()
def callback():
    Isum.config(text=passgen())

#window layout
root= Tk()
root.geometry("400x300")
root.title("Password Genertor")


#introduction
title=StringVar()
lable=Label(root,textvariable=title)
lable.pack()
title.set("COMPLEXITY OF PASSWORD")

choice=IntVar()
R1=Radiobutton(root,text="Only Alphabets",variable=choice,value=1,command=selection)
R1.pack()
R2=Radiobutton(root,text="Alphabets and Numbers",variable=choice,value=2,command=selection)
R2.pack()
R3=Radiobutton(root,text="Alphabets,Numbers and Special characters",variable=choice,value=3,command=selection)
R3.pack()
lablechoice=Label(root)
lablechoice.pack()
 
lenlabel=StringVar()
lenlabel.set("password lenght")
lentitle=Label(root,textvariable=lenlabel)
lentitle.pack()

val=IntVar()
spinlenght=Spinbox(root,from_=6,to_=24,textvariable=val,width=13)
spinlenght.pack()

passgenbutton=Button(root,text="Generate password",bd=3,height=2,command=callback,background="black",foreground="white")
passgenbutton.pack()
password=str(callback)

Isum=Label(root,text="")
Isum.pack(side=BOTTOM)
 
#working
poor=string.ascii_uppercase+ string.ascii_letters
average=string.ascii_lowercase + string.ascii_uppercase + string.digits
symbols="!@#$%^&*()_+-={}[]|\*/;',./<>"
advance=poor+average+symbols

def passgen():
    if choice.get()==1:
        return"".join(random.sample(poor,val.get()))
    elif choice.get()==2:
        return"".join(random.sample(average,val.get()))
    elif choice.get()==3:
        return"".join(random.sample(advance,val.get()))
    

root.mainloop()
