from tkinter import *
from PIL import Image,ImageTk
from datetime import date
from tkcalendar import DateEntry
from tkinter import messagebox
from tkinter.ttk import Combobox
import mysql.connector
win=Toplevel()
win.title("Interest")
win.geometry("1500x850")
win.resizable(False,False)
#back image
img = Image.open("D:\\Savingbank\\bhamare3.jpg")
img=img.resize((1600,850))
my = ImageTk.PhotoImage(img)
label = Label(win, image=my)
label.pack(side=LEFT,fill=BOTH,expand=True)

def clfield():
    t2.delete(0, END)
    t3.delete(0, END)
    t4.delete(0, END)
    t5.delete(0, END)
    t6.delete(0, END)
    t7.delete(0,END)

def calinter(event):
    try:
        mydb=mysql.connector.connect(
            user="root",
            password="",
            host="localhost",
            database="bank"
        )
        mycur=mydb.cursor()

        s4=t4.get_date()
        a1=s4.year
        a2=s4.month
        a3=s4.day
        s5=t5.get_date()
        b1=s5.year
        b2=s5.month
        b3=s5.day
        if a2<=2:
            a2=a2+12
            a1=a1-1
        n1 = ((146097 * a1) / 400) + ((153 * a2) + 8) / 5 + a3
        if b2<=2:
            b2=b2+12
            b1=b1-1
        n2 = ((146097 * b1) / 400) + ((153 * b2) + 8) / 5 + b3
        t=int(n2-n1)

        s1 = t3.get()
        mycur.execute("select * from applicant where apno=" + s1)
        mybug = mycur.fetchone()
        opba = mybug[9]
        sum1 = 0
        mycur.execute("select * from deposit where apno=" + s1 + "")
        bug1 = mycur.fetchall()
        for i in bug1:
            sum1 = sum1 + int(i[4])
        sum2 = 0
        mycur.execute("select * from withdraw where apno=" + s1 + "")
        bug2 = mycur.fetchall()
        for i in bug2:
            sum2 = sum2 + int(i[4])
        sum3 = 0
        mycur.execute("select * from intcheck where apno=" + s1 + "")
        bug3 = mycur.fetchall()
        for i in bug3:
            sum3 = sum3 + int(i[6])
        p = opba + sum1 - sum2 + sum3

        s6 = int(t6.get())
        r=int(s6)
        si=((int(p)*int(r)*int(t))/100)*(1/365)
        t7.delete(0,END)
        t7.insert(0,""+str(si))
    except:
        print("")
def showrec(event):
    mydb = mysql.connector.connect(
        user="root",
        password="",
        host="localhost",
        database="bank"
    )
    s1 = t3.get()
    mycur = mydb.cursor()
    mycur.execute("select * from applicant where apno=" + s1)
    mybug = mycur.fetchone()
    ln.config(text="" + mybug[1])
    opbal = int(mybug[8])

    sum = 0
    mycur.execute("select * from deposit where apno=" + s1)
    mybug = mycur.fetchall()
    for i in mybug:
        sum = sum + int(i[4])
    sum = opbal + sum
    sum1 = 0
    mycur.execute("select * from withdraw where apno=" + s1)
    mybug = mycur.fetchall()
    for i in mybug:
        sum1 = sum1 + int(i[4])
    sum = opbal + sum
    sum = sum - sum1
    lb2.config(text="" + str(sum))

def maxrec():
    mydb = mysql.connector.connect(
        user="root",
        password="",
        host="localhost",
        database="bank"
    )
    mycur = mydb.cursor()
    mycur.execute("select max(trno) from intcheck")
    mybug = mycur.fetchone()
    mx=int(mybug[0])
    mx=int(mx)+1
    t1.delete(0, END)
    t1.insert(0,""+str(mx))
    data=[]
    mycur.execute("select apno from applicant")
    bug=mycur.fetchall()
    for i in bug:
        data.append(i)
    t3.config(values=data)
    x = date.today()
    t2.delete(0, END)
    t2.insert(0, x.strftime("%Y") + "-" + x.strftime("%m") + "-" + x.strftime("%d"))

def saverec():
    s1=t1.get()
    s2=t2.get()
    s3=t3.get()
    s4=t4.get()
    s5=t5.get()
    s6=t6.get()
    s7=t7.get()

    if s1=="":
        messagebox.showwarning("Warn..","Please enter Transaction No",parent=win)
        return
    if s2=="":
        messagebox.showwarning("Warn..","Please enter Transaction Date",parent=win)
        return
    if s3=="":
        messagebox.showwarning("Warn..","Please enter Applicant No",parent=win)
        return
    if s4=="":
        messagebox.showwarning("Warn..","Please enter Interest from",parent=win)
        return
    if s5=="":
        messagebox.showwarning("Warn..","Please enter Interest To",parent=win)
        return
    if s6=="":
        messagebox.showwarning("Warn..","Please enter Interest Rate",parent=win)
        return

    mydb=mysql.connector.connect(
        user="root",
        password="",
        host="localhost",
        database="bank"
    )
    mycur=mydb.cursor()
    mycur.execute("insert into intcheck values("+s1+",'"+s2+"','"+s3+"','"+s4+"','"+s5+"','"+s6+"','"+s7+"')")
    mydb.commit()
    messagebox.showinfo("Confirm","Record is Saved",parent=win)
    t1.delete(0,END)
    clfield()

def serrec():
    s1=t1.get()
    clfield()
    mydb=mysql.connector.connect(
        user="root",
        password="",
        host="localhost",
        database="bank"
    )
    mycur=mydb.cursor()
    mycur.execute("select * from intcheck where trno="+s1+"")
    mybug=mycur.fetchone()
    try:
        t2.insert(0,str(mybug[1]))
        t3.insert(0,str(mybug[2]))
        t4.insert(0,str(mybug[3]))
        t5.insert(0,str(mybug[4]))
        t6.insert(0,str(mybug[5]))
        t7.insert(0,str(float(mybug[6])))
    except:
        messagebox.showerror("Warn..","Record is not found",parent=win)

def uprec():
    s1=t1.get()
    s2=t2.get()
    s3=t3.get()
    s4=t4.get()
    s5=t5.get()
    s6=t6.get()
    if s2 == "":
        messagebox.showwarning("Warn..", "Please enter Transaction Date",parent=win)
        return
    if s3=="":
        messagebox.showwarning("Warn..","Please enter Applicant No",parent=win)
        return
    if s4 == "":
        messagebox.showwarning("Warn..", "Please enter Interest from",parent=win)
        return
    if s5 == "":
        messagebox.showwarning("Warn..", "Please enter Interest To",parent=win)
        return
    if s6 == "":
        messagebox.showwarning("Warn..", "Please enter Interest Rate",parent=win)
        return

    mydb=mysql.connector.connect(
        user="root",
        password="",
        host="localhost",
        database="bank"
    )
    mycur=mydb.cursor()
    mycur.execute("update intcheck set trdate='"+s2+"',apno='"+s3+"',ifrom='"+s4+"',ito='"+s5+"',irate='"+s6+"' where trno="+s1+"")
    mydb.commit()
    messagebox.showinfo("Confirm","Record is updated",parent=win)
    t1.delete(0,END)
    clfield()

def delrec():
    s1=t1.get()
    clfield()
    mydb=mysql.connector.connect(
        user="root",
        password="",
        host="localhost",
        database="bank"
    )
    ans=messagebox.askyesnocancel("Confirm","Are you sure delete ?",parent=win)

    if ans==True:
        mycur=mydb.cursor()
        mycur.execute("delete from intcheck where trno="+s1+"")
        mydb.commit()
        messagebox.showinfo("Info","Record is Deleted!!",parent=win)
        t1.delete(0,END)
        clfield()

#frame
Frame_Login=Frame(win,bg="midnightblue",highlightbackground="darkblue",highlightthickness=3)
Frame_Login.place(x=50,y=130,width=650,height=500)
#title on Frame
title=Label(Frame_Login,text="Interest Check",font=("Lucida Calligraphy",35,"bold","underline"),bg="#a8d4ff",fg="black")
title.place(x=110,y=30)

#form content
l1=Label(Frame_Login,text="Transaction_No_ ",font=("times in roman",15),bg="#a8d4ff",fg="black")
l1.place(x=90,y=120)
t1=Entry(Frame_Login,font=("times new roman",15))
t1.place(x=280,y=120)
#trdate
l2=Label(Frame_Login,text="Transaction_date_ ",font=("times in roman",15),bg="#a8d4ff",fg="black")
l2.place(x=90,y=170)
Date=StringVar(Frame_Login)
today=date.today()
d1=today.strftime("%Y/%m/%d")
t2=Entry(Frame_Login,textvariable=Date,width=20,font=("times new roman",15))
t2.place(x=280,y=170)
Date.set(d1)

#interest from
l3=Label(Frame_Login,text="Applicant_No_ ",font=("times in roman",15),bg="#a8d4ff",fg="black")
l3.place(x=90,y=220)
t3 = Combobox(Frame_Login, font=("times in roman",13))
t3.place(x=280, y=220)
t3.bind('<<ComboboxSelected>>', showrec)

ln = Label(Frame_Login, text="",font=("times in roman",15),bg="#a8d4ff",fg="black")
ln.place(x=520, y=220)


#Interest to
l4=Label(Frame_Login,text="I_from_date_ ",font=("times in roman",15),bg="#a8d4ff",fg="black")
l4.place(x=90,y=270)
t4=DateEntry(Frame_Login,selectmode="day",font=("times in roman",15),width=16)
t4.bind("<<DateEntrySelected>>",calinter)
t4.place(x=280,y=270)

#apno
l5=Label(Frame_Login,text="I_To_ ",font=("times in roman",15),bg="#a8d4ff",fg="black")
l5.place(x=90,y=320)
t5=DateEntry(Frame_Login,selectmode="day",font=("times in roman",15),width=16)
t5.bind("<<DateEntrySelected>>",calinter)
t5.place(x=280,y=320)


l6=Label(Frame_Login,text="I_rate_ ",font=("times in roman",15),bg="#a8d4ff",fg="black")
l6.place(x=90,y=370)
t6=Entry(Frame_Login,font=("times new roman",15))
t6.place(x=280,y=370)
t6.bind("<Key>",calinter)
#amt
l7=Label(Frame_Login,text="Amount_ ",font=("times in roman",15),bg="#a8d4ff",fg="black")
l7.place(x=90,y=420)
t7=Entry(Frame_Login,font=("times new roman",15))
t7.place(x=280,y=420)

lb1=Label(Frame_Login,text="Total bal : ",font=("times in roman",15),bg="#a8d4ff",fg="black")
lb1.place(x=280,y=460)

lb2=Label(Frame_Login,text=" ",font=("times in roman",15),bg="#a8d4ff",fg="black")
lb2.place(x=370,y=460)

#buttons
b1=Button(win,text="ADD",font=("times new roman",16),bg="#a8d4ff",fg="black",width=8,bd=3,command=maxrec)
b1.place(x=50,y=650)

b2=Button(win,text="SAVE",font=("times new roman",16),bg="#a8d4ff",fg="black",width=8,bd=3,command=saverec)
b2.place(x=160,y=650)

b3=Button(win,text="SEARCH",font=("times new roman",16),bg="#a8d4ff",fg="black",width=8,bd=3,command=serrec)
b3.place(x=270,y=650)

b4=Button(win,text="UPDATE",font=("times new roman",16),bg="#a8d4ff",fg="black",width=8,bd=3,command=uprec)
b4.place(x=380,y=650)

b5=Button(win,text="DELETE",font=("times new roman",16),bg="#a8d4ff",fg="black",width=8,bd=3,command=delrec)
b5.place(x=490,y=650)

b6=Button(win,text="EXIT",font=("times new roman",16),bg="#a8d4ff",fg="black",width=8,bd=3,command=quit)
b6.place(x=600,y=650)
win.mainloop()