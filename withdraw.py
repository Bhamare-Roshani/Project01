from tkinter import *
from PIL import Image,ImageTk
from datetime import date
from tkinter.ttk import Combobox
import mysql.connector
from tkinter import messagebox

win=Toplevel()
win.title("Withdraw Form")
win.geometry("1500x850")
win.resizable(False,False)
#back image
img = Image.open("D:\\Savingbank\\ro.jpg")
img=img.resize((1600,850))
my = ImageTk.PhotoImage(img)
label = Label(win, image=my)
label.pack(side=LEFT,fill=BOTH,expand=True)

def clrfield():

    t2.delete(0, END)
    t3.delete(0, END)
    t4.delete(0, END)

def showrec(event):
    mydb=mysql.connector.connect(
        user="root",
        password="",
        host="localhost",
        database="bank"
    )
    s1=t2.get()
    mycur=mydb.cursor()
    mycur.execute("select * from applicant where apno="+s1)
    mybug=mycur.fetchone()
    ln1.config(text=""+str(mybug[1]))
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

    sum3=opbal+sum2-sum1
    lb1.config(text=""+str(sum3))


def maxrec():
    mydb = mysql.connector.connect(
        user="root",
        password="",
        host="localhost",
        database="bank"
    )
    mycur = mydb.cursor()
    mycur.execute("select max(slno) from withdraw")
    mybug=mycur.fetchone()
    mx=int(mybug[0])
    mx=int(mx)+1
    t1.delete(0,END)
    t1.insert(0,""+str(mx))
    data=[]
    mycur.execute("select apno from applicant")
    bug=mycur.fetchall()
    for i in bug:
        data.append(i)
    t2.config(values=data)
    x = date.today()
    de.delete(0, END)
    de.insert(0, x.strftime("%Y") + "-" + x.strftime("%m") + "-" + x.strftime("%d"))
    clrfield()

def saverec():
    s1 = t1.get()
    s2 = de.get()
    s3 = t2.get()
    s4 = t3.get()
    s5 = t4.get()

    if s1 == "":
        messagebox.showwarning("warn..", "plz enter Slip No",parent=win)
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

    '''a=int(s5)
    s=int(lb1["text"])
    if a > s:
        messagebox.showinfo("warn","insufficient balance available"+str(s)+"Rs. only")
        return
    '''
    mydb = mysql.connector.connect(
        user="root",
        password="",
        host="localhost",
        database="bank"
    )
    mycur = mydb.cursor()
    mycur.execute("insert into withdraw values(" + s1 + ",'" + s2 + "'," + s3 + ",'" + s4 + "'," + s5 + ")")
    mydb.commit()
    messagebox.showinfo("confirm", "Amount is withdraw",parent=win)
    t1.delete(0, END)
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
    mycur.execute("select * from withdraw where slno=" + s1)
    mybug = mycur.fetchone()
    try:
        de.insert(0, str(mybug[1]))
        t2.insert(0, str(mybug[2]))
        t3.insert(0, str(mybug[3]))
        t4.insert(0, str(mybug[4]))
    except:
        messagebox.showerror("Warn..", "Rec is Not found",parent=win)

def uprec():
    s1 = t1.get()
    s2 = de.get()
    s3 = t2.get()
    s4 = t3.get()
    s5 = t4.get()

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
    mycur.execute("update withdraw set sldate='" + s2 + "',apno=" + s3 + ",perticular='" + s4 + "',amount=" + s5 + " where slno=" + s1 + "")
    mydb.commit()
    messagebox.showinfo("confirm", "Record is Update",parent=win)
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
    ans = messagebox.askyesnocancel("confirm", "are U sure delete?",parent=win)
    if ans == True:
        mycur = mydb.cursor()
        mycur.execute("delete from withdraw where slno=" + s1 + "")
        mydb.commit()
        messagebox.showinfo("confirm", "Rec is deleted",parent=win)
        t1.delete(0, END)
        clrfield()


#frame
Frame_Login=Frame(win,bg="cadetblue",highlightbackground="gray",highlightthickness=3)
Frame_Login.place(x=800,y=170,width=650,height=430)
#title on Frame
title=Label(Frame_Login,text="Withdraw Form",font=("impact",35),bg="cadetblue",fg="white")
title.place(x=110,y=30)

#form content
l1=Label(Frame_Login,text="SL_No_ ",font=("times in roman",15),bg="cadetblue",fg="white")
l1.place(x=90,y=120)
t1=Entry(Frame_Login,font=("times new roman",15))
t1.place(x=280,y=120)
#sldate
l2=Label(Frame_Login,text="Sl_date_ ",font=("times in roman",15),bg="cadetblue",fg="white")
l2.place(x=90,y=170)
Date=StringVar(Frame_Login)
today=date.today()
d1=today.strftime("%Y/%m/%d")
de=Entry(Frame_Login,textvariable=Date,width=20,font=("times new roman",15))
de.place(x=280,y=170)
Date.set(d1)
#apno
l3=Label(Frame_Login,text="Ap_no_ ",font=("times in roman",15),bg="cadetblue",fg="white")
l3.place(x=90,y=220)
t2 = Combobox(Frame_Login, font=("times in roman",13))
t2.place(x=280, y=220)
t2.bind('<<ComboboxSelected>>', showrec)

ln1 = Label(Frame_Login, text="",font=("times in roman",15),bg="cadetblue",fg="white")
ln1.place(x=520, y=220)

#perticular
l4=Label(Frame_Login,text="Perticular_ ",font=("times in roman",15),bg="cadetblue",fg="white")
l4.place(x=90,y=270)
data = ("By cash", "By check", "By DD")
t3 = Combobox(Frame_Login, values=data, font=("times in roman",13))
t3.place(x=280, y=270)

#amt
l5=Label(Frame_Login,text="Amount_ ",font=("times in roman",15),bg="cadetblue",fg="white")
l5.place(x=90,y=320)
t4=Entry(Frame_Login,font=("times new roman",15))
t4.place(x=280,y=320)
#total bal
lb1 = Label(Frame_Login, text="",font=("times in roman",15),bg="cadetblue",fg="white")
lb1.place(x=520, y=320)
#buttons

b1=Button(win,text="ADD",font=("times new roman",16),bg="#cff8f9",fg="black",width=8,command=maxrec)
b1.place(x=780,y=630)

b2=Button(win,text="SAVE",font=("times new roman",16),bg="#cff8f9",fg="black",width=8,command=saverec)
b2.place(x=890,y=630)

b3=Button(win,text="SERCH",font=("times new roman",16),bg="#cff8f9",fg="black",width=10,command=serrec)
b3.place(x=1000,y=630)

b4=Button(win,text="UPDATE",font=("times new roman",16),bg="#cff8f9",fg="black",width=8,command=uprec)
b4.place(x=1135,y=630)

b5=Button(win,text="DELETE",font=("times new roman",16),bg="#cff8f9",fg="black",width=8,command=delrec)
b5.place(x=1245,y=630)

b6=Button(win,text="EXIT",font=("times new roman",16),bg="#cff8f9",fg="black",width=8,command=quit)
b6.place(x=1355,y=630)

win.mainloop()

