from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox



win=Tk()
win.title("Login system")
win.geometry("1500x850")
win.resizable(False,False)

#back image
img=Image.open("C:\\Users\\Admin\\Pictures\\roshani document\\roshani.webp")
img=img.resize((1500,850))
bg=ImageTk.PhotoImage(img)
bg_img=Label(image=bg).pack()

def logrec():
    import pyttsx3
    engine=pyttsx3.init()
    if t1.get()=="" and t2.get()=="":
        engine.say("All field are required")
        engine.runAndWait()
        messagebox.showerror("Error....","All field are required")
        return
    elif t1.get()!="roshani" and t2.get()!="9011":
        engine.say("Invalid Username & Password")
        engine.runAndWait()
        messagebox.showerror("Error....","Invalid Username & Password")
        return
    elif  t1.get()!="roshani":
        engine.say("Invalid Username...")
        engine.runAndWait()
        messagebox.showerror("Error....","Invalid Username")
        return
    elif t2.get()!="9011":
        engine.say("Invalid Password...")
        engine.runAndWait()
        messagebox.showerror("Error....","Invalid Password")
        return
    else:
        engine.say("Hello sir....Welcome to State Bank of India.")
        engine.runAndWait()
        messagebox.showinfo("Confirm","Welcome to Bank Acc system")
        import bank_acc_sys

def fpass():
    import pyttsx3
    engine=pyttsx3.init()
    engine.say("Are U sure forget Username and password ?")
    engine.runAndWait()
    ans=messagebox.askyesno("confirm", "Are U sure forget Username and password ?")
    if ans == True:
        engine.say("Your Username is Sayali  and password is 9545")
        engine.runAndWait()
        messagebox.showinfo("Error...","Your Username : Sayali\n Password :9545")




#Frame
Frame_Login=Frame(win,bg="white",highlightbackground="skyblue",highlightthickness=3)
Frame_Login.place(x=750,y=300,width=550,height=400)

title=Label(Frame_Login,text=" Login Here ",font=("impact",35,"bold"),bg="white",fg="black")
title.place(x=90,y=20)

decs=Label(Frame_Login,text="Account Login Area ",font=("goudy old style",16),bg="white",fg="black")
decs.place(x=100,y=80)

l1=Label(Frame_Login,text="Username ",font=("goudy old style",25,"bold"),bg="white",fg="gray")
l1.place(x=100,y=110)
t1=Entry(Frame_Login,font=("times new roman",25))
t1.place(x=100,y=160)

l2=Label(Frame_Login,text="Password ",font=("goudy old style",25,"bold"),bg="white",fg="gray")
l2.place(x=100,y=210)
t2=Entry(Frame_Login,font=("times new roman",25),show="*")
t2.place(x=100,y=260)

b1=Button(Frame_Login,text="Forget Password ? ",font=("times new roman",16),bd=0,bg="white",fg="black",command=fpass)
b1.place(x=100,y=310)

b2=Button(win,text=" LOGIN ",font=("impact",20,"bold"),width=20,command=logrec)
b2.place(x=880,y=660)
win.mainloop()