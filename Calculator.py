"""
Let's make a calculator in tkinter with
better GUI.
"""
from tkinter import *
from tkinter import messagebox
root = Tk()
root.configure(background='light blue')
root.geometry("500x300")
#main function to calculate the expression
def calc():
    try:
        a = Entry.get(t1)
        b= Entry.get(t2)
        operator = Entry.get(t3)
        a = int(a)
        b = int(b)
        if operator=='+':
            Answer = a+b
        if operator=='-':
            Answer = a-b
        if operator=='*':
            Answer = a*b
        if operator=='/':
            Answer = a/b
            
        if operator=='%':
            Answer = a%b
            
        Entry.insert(t4,0,Answer)
    except ValueError:
        messagebox.showinfo("Warning","Invalid Input by the user!!")
        #Clear the textbox
def clear():
    t1.delete(0,END)
    t2.delete(0,END)
    t3.delete(0,END)
    t4.delete(0,END)
    
    #Text Fields
label = Label(root,text="Calculator With tkinter GUI",fg="blue",font=("bold",17)).grid(row=0,column=1)
label = Label(root,text="First Number",font="bold",highlightcolor="red").grid(row=1,column=0)
label = Label(root,text="Second Number",font="bold").grid(row=2,column=0)
label = Label(root,text="Operator",font="bold").grid(row=3,column=0)
label = Label(root,text="Answer",font="bold").grid(row=4,column=0)
t1 = Entry(root,bd=5)
t1.grid(row=1,column=1)

t2 = Entry(root,bd=5)
t2.grid(row=2,column=1)

t3 = Entry(root,bd=5)
t3.grid(row=3,column=1)

t4 = Entry(root,bd=5)
t4.grid(row=4,column=1)
#Submit Button
b1=Button(root,text="Submit",relief="ridge",fg="white",bg="light green",bd=7,width="15",command=calc)
b1.grid(row=5,column=0,pady=5,ipadx=10,ipady=3,columnspan=5)
#Reset button
b2=Button(root,text="Reset",relief="ridge",fg="white",bg="red",bd=7,width="15",command=clear)
b2.grid(row=6,column=0,pady=5,ipadx=10,ipady=3,columnspan=6)


