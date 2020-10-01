from tkinter import *

def submit():
    getf=first.get()
    getl=last.get()
    geta=age.get()

    file=open('database.txt','a')
    file .write(getf+",",+getl+","+str(geta)+"\n")
    file.close()
    print("user registered")

    entry_first.delete(0,END)
    entry_last.delete(0,END)
    entry_age.delete(0,END)
    
window=Tk()
window.title("Registration Form")
window.geometry("350x350")

l1=Label(window, text="Please Register Now", bg="black", fg="white", font="times 12")
l1.pack()

first=StringVar()
last=StringVar()
age=IntVar()

Label(window, text="First Name: ",bg="black", fg="white").place(x=50,y=60)
entry_first=Entry(window,textvariable=first)
entry_first.place(x=150,y=60)

Label(window, text="Last Name: ",bg="black", fg="white").place(x=50,y=100)
entry_last=Entry(window, textvariable=last)
entry_last.place(x=150,y=120)

Label(window, text="Age: ",bg="black", fg="white").place(x=50,y=1800)
entry_age=Entry(window, textvariable=age)
entry_age.place(x=150,y=1800)

Button(window, text="Submit", bg="black", fg="white", font="times 12", command=submit).place(x=100,y=240)
