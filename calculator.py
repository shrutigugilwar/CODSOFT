#calculator
from tkinter import *

#function
def getdigit(digit):
   current=resultlabel["text"]
   new=current+str(digit)
   resultlabel.config(text=new)
def clear():
   resultlabel.config(text="")
def getoperator(op):
   global firstnum,operator
   firstnum=int(resultlabel['text'])
   operator=op
   resultlabel.config(text=" ")
def getresult():
    global firstnum,secondnum,operator
    secondnum=int(resultlabel['text'])
    if operator == '+':
      resultlabel.config(text=str(firstnum+secondnum))
    elif operator == '-':
      resultlabel.config(text=str(firstnum-secondnum))
    elif operator =='*':
      resultlabel.config(text=str(firstnum*secondnum))
    else:
       if secondnum==0:
         resultlabel.config(text="error")
       else:
         resultlabel.config(text=str(firstnum/secondnum))
#window layout
root = Tk()
root.title("calulator")
root.geometry("280x380")
root.resizable(0,0)
root.configure(background="black")

#result
resultlabel=Label(root,text="",background="black",foreground="pink")
resultlabel.grid(row=0,column=0,columnspan=5,pady=(50,25),sticky="W")
resultlabel.config(font=("verdana",30,"bold"))

#button
b7=Button(root,text="7",background="pink",foreground="black",width=5,height=2,command=lambda :getdigit(7))
b7.grid(row=1,column=0)
b7.config(font=("verdana",14))

b8=Button(root,text="8",background="pink",foreground="black",width=5,height=2,command=lambda:getdigit(8))
b8.grid(row=1,column=1)
b8.config(font=("verdana",14))

b9=Button(root,text="9",background="pink",foreground="black",width=5,height=2,command=lambda:getdigit(9))
b9.grid(row=1,column=2)
b9.config(font=("verdana",14))

badd=Button(root,text="+",background="pink",foreground="black",width=5,height=2,command=lambda:getoperator("+"))
badd.grid(row=1,column=3)
badd.config(font=("verdana",14))

b4=Button(root,text="4",background="pink",foreground="black",width=5,height=2,command=lambda:getdigit(4))
b4.grid(row=2,column=0)
b4.config(font=("verdana",14))

b5=Button(root,text="5",background="pink",foreground="black",width=5,height=2,command=lambda:getdigit(5))
b5.grid(row=2,column=1)
b5.config(font=("verdana",14))

b6=Button(root,text="6",background="pink",foreground="black",width=5,height=2,command=lambda:getdigit(6))
b6.grid(row=2,column=2)
b6.config(font=("verdana",14))

bsub=Button(root,text="-",background="pink",foreground="black",width=5,height=2,command=lambda:getoperator("-"))
bsub.grid(row=2,column=3)
bsub.config(font=("verdana",14))

b1=Button(root,text="1",background="pink",foreground="black",width=5,height=2,command=lambda:getdigit(1))
b1.grid(row=3,column=0)
b1.config(font=("verdana",14))

b2=Button(root,text="2",background="pink",foreground="black",width=5,height=2,command=lambda:getdigit(2))
b2.grid(row=3,column=1)
b2.config(font=("verdana",14))

b3=Button(root,text="3",background="pink",foreground="black",width=5,height=2,command=lambda:getdigit(3))
b3.grid(row=3,column=2)
b3.config(font=("verdana",14))

bmul=Button(root,text="*",background="pink",foreground="black",width=5,height=2,command=lambda:getoperator("*"))
bmul.grid(row=3,column=3)
bmul.config(font=("verdana",14))

bclr=Button(root,text="c",background="pink",foreground="black",width=5,height=2,command=lambda:clear())
bclr.grid(row=4,column=0)
bclr.config(font=("verdana",14))

b0=Button(root,text="0",background="pink",foreground="black",width=5,height=2,command=lambda:getdigit(0))
b0.grid(row=4,column=1)
b0.config(font=("verdana",14))

bequls=Button(root,text="=",background="pink",foreground="black",width=5,height=2,command=lambda:getresult())
bequls.grid(row=4,column=2)
bequls.config(font=("verdana",14))

bdiv=Button(root,text="/",background="pink",foreground="black",width=5,height=2,command=lambda:getoperator("/"))
bdiv.grid(row=4,column=3)
bdiv.config(font=("verdana",14))

root.mainloop()