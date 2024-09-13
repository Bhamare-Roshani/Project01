from tkinter import *
from PIL import Image,ImageTk
from datetime import date
from tkinter import messagebox
import mysql.connector
from tkinter.ttk import Combobox
win=Toplevel()
win.title("Cl_Acc_Form")
win.geometry("1500x850")
win.resizable(False,False)
#back image
img = Image.open("D:\\Savingbank\\bhamare2.jpg")
img=img.resize((1600,850))
my = ImageTk.PhotoImage(img)
label = Label(win, image=my)
label.pack(side=LEFT,fill=BOTH,expand=True)

def clrfield():
    t2.delete(0,END)
    t3.delete(0, END)
    t4.delete(0, END)


def showrec(event):
    mydb = mysql.connector.connect(
        user="root",
        password="",
        host="localhost",
        database="bank"
    )
    mycur = mydb.cursor()
    s1=t2.get()
    mycur.execute("select * from applicant where apno="+s1)
    mybug=mycur.fetchone()
    ln.config(text=""+str(mybug[1]))
    opbal=int(mybug[8])
    sum1=0
    sum2=0
    mycur.execute("select * from withdraw where apno="+s1)
    mybug1=mycur.fetchall()
    for i in mybug1:
        sum1=sum1+int(i[4])
    mycur.execute("select * from deposit where apno="+s1)
    mybug2=mycur.fetchall()
    for i in mybug2:
        sum2=sum2+int(i[4])
    sum3= opbal+sum2-sum1
    t4.insert(0,""+str(sum3))
    l2.config(text=""+str(sum3))

def maxrec():
    mydb = mysql.connector.connect(
        user="root",
        password="",
        host="localhost",
        database="bank"
    )
    mycur = mydb.cursor()
    mycur.execute("select max(slno) from accountclose")
    mybug=mycur.fetchone()
    mx=int(mybug[0])
    mx=int(mx)+1
    t1.delete(0,END)
    t1.insert(0,""+str(mx))
    clrfield()
    x=date.today()
    de.delete(0,END)
    clrfield()
    de.insert(0, x.strftime("%Y") + "-" + x.strftime("%m") + "-" + x.strftime("%d"))
    clrfield()
    data=[]
    mycur.execute("select apno from applicant ")
    bug=mycur.fetchall()
    for i in bug:
        data.append(i)
    t2.config(value=data)

def saverec():
    s1 = t1.get()
    s2 = de.get()
    s3 = t2.get()
    s4 = t3.get()
    s5 = t4.get()

    if s1 == "":
        messagebox.showwarning("warn..", "plz enter Slip no",parent=win)
        return
    if s2 == "":
        messagebox.showwarning("warn..", "plz enter Slip Date",parent=win)
        return
    if s3 == "":
        messagebox.showwarning("warn..", "plz enter applicant No",parent=win)
        return
    if s4 == "":
        messagebox.showwarning("warn..", "plz enter Particular",parent=win)
        return
    if s5 == "":
        messagebox.showwarning("warn..", "plz enter amount",parent=win)
        return

    mydb = mysql.connector.connect(
        user="root",
        password="",
        host="localhost",
        database="bank"
    )
    mycur = mydb.cursor()
    mycur.execute("insert into accountclose values("+s1+",'"+s2+"','"+s3+"','"+s4+"','"+s5+"')")
    mydb.commit()
    mycur.execute("update applicant set apno="+s3)
    messagebox.showinfo("Confirm...","Account is close")
    t1.delete(0,END)
    clrfield()

def serrec():
    s1 = t1.get()
    clrfield()
    mydb = mysql.connector.connect(
            user="root",
            password="",
            host="localhost",
            database="bank"
        )
    mycur = mydb.cursor()
    mycur.execute("select * from accountclose where slno=" + s1+"")
    mybug = mycur.fetchone()
    try:
        de.insert(0, str(mybug[1]))
        t2.insert(0, str(mybug[2]))
        t3.insert(0,str(mybug[3]))
        t4.insert(0, str(mybug[4]))
    except:
        messagebox.showerror("Warn..", "Rec is Not found",parent=win)

def uprec():
    s1=t1.get()
    s2=de.get()
    s3=t2.get()
    s4=t3.get()
    s5 = t4.get()

    if s2 == "":
        messagebox.showwarning("warn..", "plz enter apno",parent=win)
        return
    if s3 == "":
        messagebox.showwarning("warn..", "plz enter app name",parent=win)
        return
    if s4 == "":
        messagebox.showwarning("warn..", "plz enter add",parent=win)
        return
    if s5 == "":
        messagebox.showwarning("warn..", "plz enter city",parent=win)
        return

    mydb = mysql.connector.connect(
        user="root",
        password="",
        host="localhost",
        database="bank"
    )
    mycur = mydb.cursor()
    mycur.execute("insert into applicant values("+s1+",'"+s2+"','"+s3+"','"+s4+"','"+s5+"')")
    mydb.commit()
    messagebox.showinfo("Confirm...","Record is update")
    t1.delete(0,END)
    clrfield()

def delrec():
    s1 = t1.get()
    mydb = mysql.connector.connect(
        user="root",
        password="",
        host="localhost",
        database="bank"
    )
    ans = messagebox.askyesnocancel("confirm", "Are U sure delete?",parent=win)
    if ans == True:
        mycur = mydb.cursor()
        mycur.execute("delete from accountclose where slno=" + s1 + "")
        mydb.commit()
        messagebox.showinfo("confirm", "Rec is deleted",parent=win)
        t1.delete(0, END)
    clrfield()

#frame
Frame_Login=Frame(win,bg="black",highlightbackground="gray",highlightthickness=3)
Frame_Login.place(x=680,y=100,width=660,height=430)
#title on Frame
title=Label(Frame_Login,text="Close Account",font=("algerian",35,"underline","bold"),bg="black",fg="#cff8f9")
title.place(x=110,y=30)

#form content
l1=Label(Frame_Login,text="Slip_No_ ",font=("times in roman",15),bg="black",fg="#cff8f9")
l1.place(x=90,y=120)
t1=Entry(Frame_Login,font=("times new roman",15))
t1.place(x=280,y=120)
#cldate
l2=Label(Frame_Login,text="Sl_date_ ",font=("times in roman",15),bg="black",fg="#cff8f9")
l2.place(x=90,y=170)
Date=StringVar(Frame_Login)
today=date.today()
d1=today.strftime("%d/%m/%Y")
de=Entry(Frame_Login,textvariable=Date,width=20,font=("times new roman",15))
de.place(x=280,y=170)
Date.set(d1)
#apno
l3=Label(Frame_Login,text="App_no_ ",font=("times in roman",15),bg="black",fg="#cff8f9")
l3.place(x=90,y=220)
t2=Combobox(Frame_Login,font=("times new roman",13))
t2.place(x=280,y=220)
t2.bind('<<ComboboxSelected>>',showrec)

ln=Label(Frame_Login,text=" ",font=("times in roman",15),bg="black",fg="#cff8f9")
ln.place(x=500,y=220)

#reason
l4=Label(Frame_Login,text="Reason_ ",font=("times in roman",15),bg="black",fg="#cff8f9")
l4.place(x=90,y=270)
data=("Not satissfied with service","I have another acc","Death of acc holder","other")
t3=Combobox(Frame_Login,values=data,font=("times new roman",13))
t3.place(x=280,y=270)

#amt
l5=Label(Frame_Login,text="Reamount_ ",font=("times in roman",15),bg="black",fg="#cff8f9")
l5.place(x=90,y=320)
t4=Entry(Frame_Login,font=("times new roman",15))
t4.place(x=280,y=320)

ln1=Label(Frame_Login,text="Total_Bal_  ",font=("times in roman",15),bg="black",fg="#cff8f9")
ln1.place(x=90,y=370)
l2=Label(Frame_Login,text=" ",font=("times in roman",15),bg="black",fg="#cff8f9")
l2.place(x=200,y=370)



#buttons
b1=Button(win,text="ADD",font=("times new roman",16),bd=5,fg="black",bg="#cff8f9",width=8,command=maxrec)
b1.place(x=670,y=570)

b2=Button(win,text="SAVE",font=("times new roman",16),bd=5,fg="black",bg="#cff8f9",width=8,command=saverec)
b2.place(x=780,y=570)

b3=Button(win,text="SERCH",font=("times new roman",16),bd=5,fg="black",bg="#cff8f9",width=8,command=serrec)
b3.place(x=890,y=570)
#delete
b4=Button(win,text="UPDATE",font=("times new roman",16),bd=5,fg="black",bg="#cff8f9",width=10,command=uprec)
b4.place(x=1000,y=570)

b5=Button(win,text="DELETE",font=("times new roman",16),bd=5,fg="black",bg="#cff8f9",width=8,command=delrec)
b5.place(x=1135,y=570)

b5=Button(win,text="EXIT",font=("times new roman",16),bd=5,fg="black",bg="#cff8f9",width=8,command=quit)
b5.place(x=1248,y=570)

win.mainloop()