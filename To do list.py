#To do list
import tkinter
import tkinter.messagebox
from tkinter import ttk

# functions
def add_task():
    task=entrytask.get()
    if task !="":
        listboxtask.insert(tkinter.END,task)
        entrytask.delete(0,tkinter.END)
    else:
        tkinter.messagebox.showwarning(title="warning!",message=" please enter a task")
def delete_task():
    try:
        taskindex=listboxtask.curselection()[0]
        listboxtask.delete(taskindex)
    except:
        tkinter.messagebox.showwarning(title="warning!",message=" please select the task to be deleted")
def done_task():
    try:
         taskindex=listboxtask.curselection()[0]
         listboxtask.delete(taskindex)
         listboxtask.insert(tkinter.END,"this task is completed")
    except:
        tkinter.messagebox.showwarning(title="warning!",message=" please select the completed task")


#window name 
root=tkinter.Tk()
root.title("TO-DO List")
root.geometry("500x500")
root.config(bg="black")

#lable added
namelable=ttk.Label(root,text="To-Do List",font="ariel,25,bold",width=10,foreground="black",border=5,background="lightblue")
namelable.pack(side="top",fill="y")

#listbox adeded
listboxtask=tkinter.Listbox(root,height=15,width=500,background="pink")
listboxtask.pack()

#entry box
entrytask=tkinter.Entry(root,width=500,background="lightblue",foreground="black",text="add tasks here") 
entrytask.pack()

#button
buttonaddtask=tkinter.Button(root,text="ADD TASK",width=400,command=add_task,background="black",foreground="lightblue")
buttonaddtask.pack()
buttondeletetask=tkinter.Button(root,text="DELETE TASK",width=400,command=delete_task,background="black",foreground="lightblue")
buttonaddtask.pack()
buttondeletetask.pack()
buttondonetask=tkinter.Button(root,text="DONE",width=400,command=done_task,background="black",foreground="lightblue")
buttondonetask.pack()

root.mainloop()

