from tkinter import *
from PIL import Image,ImageTk
from tkcalendar import DateEntry
from tkinter import messagebox
from tkinter.ttk import Combobox
import mysql.connector
win=Toplevel()
win.title("App Form")
win.geometry("1500x850")
win.resizable(False,False)

def clfield():
    t2.delete(0,END)
    t3.delete(0,END)
    t4.delete(0,END)
    t5.delete(0,END)
    cal.delete(0,END)
    sp.delete(0,END)
    t6.delete(0,END)
    t7.delete(0,END)
    t8.delete(0,END)

def maxrec():
    mydb=mysql.connector.connect(
        user="root",
        password="",
        host="localhost",
        database="bank"
    )
    mycur=mydb.cursor()
    mycur.execute("select max(apno) from applicant")
    mybug=mycur.fetchone()
    mx=int(mybug[0])
    mx=int(mx)+1
    t1.delete(0,END)
    t1.insert(0,""+str(mx))
    clfield()

def saverec():
    s1 = t1.get()
    s2 = t2.get()
    s3 = t3.get()
    s4 = t4.get()
    s5 = t5.get()
    s6 = cal.get()
    s7 = sp.get()
    s8 = t6.get()
    s9 = t7.get()
    s10= t8.get()


    if s2=="" or str(s2).isdigit():
        messagebox.showwarning("warn..","plz enter valid applicant name",parent=win)
        return
    if s3=="":
        messagebox.showwarning("warn..","plz enter applicant Address",parent=win)
        return
    if s4=="":
        messagebox.showwarning("warn..","plz enter applicant City",parent=win)
        return
    if s5=="":
        messagebox.showwarning("warn..","plz enter valid Contact No",parent=win)
        return
    if s6=="":
        messagebox.showwarning("warn..","plz enter applicant Birthdate",parent=win)
        return
    if s7=="":
        messagebox.showwarning("warn..","plz enter applicant Age",parent=win)
        return
    if s8=="" or str(s8).isdigit():
        messagebox.showwarning("warn..","plz enter applicant Nominee",parent=win)
        return
    if s9=="" or int(s9)<=0:
        messagebox.showwarning("warn..","plz enter applicant Valid Op bal",parent=win)
        return
    if s10=="":
        messagebox.showwarning("warn..","plz enter applicant Gender",parent=win)
        return

    mydb=mysql.connector.connect(
        user="root",
        password="",
        host="localhost",
        database="bank"
    )
    #f="Y"
    mycur=mydb.cursor()
    mycur.execute("insert into applicant values("+s1+",'"+s2+"','"+s3+"','"+s4+"','"+s5+"','"+s6+"',"+s7+",'"+s8+"',"+s9+",'"+s10+"')")#,'"+f+"')")
    mydb.commit()
    messagebox.showinfo("confirm","Rec is save",parent=win)
    t1.delete(0,END)
    clfield()

def serrec():
    s1=t1.get()
    clfield()
    mydb = mysql.connector.connect(
        user="root",
        password="",
        host="localhost",
        database="bank"
    )
    mycur=mydb.cursor()
    mycur.execute("select * from applicant where apno="+s1+"")
    mybug=mycur.fetchone()

    try:
        t2.insert(0,str(mybug[1]))
        t3.insert(0,str(mybug[2]))
        t4.insert(0,str(mybug[3]))
        t5.insert(0,str(mybug[4]))
        cal.insert(0,str(mybug[5]))
        sp.insert(0,str(mybug[6]))
        t6.insert(0,str(mybug[7]))
        t7.insert(0,str(mybug[8]))
        t8.insert(0,str(mybug[9]))
    except:
        messagebox.showerror("Warn..","Rec is Not found",parent=win)

def uprec():
    s1=t1.get()
    s2=t2.get()
    s3=t3.get()
    s4=t4.get()
    s5=t5.get()
    #s6=cal.get()
    s7=sp.get()
    s8=t6.get()
    s9=t7.get()
    #s10=gender.get()

    if s2=="":
        messagebox.showwarning("warn..", "plz enter applicant name",parent=win)
        return
    if s3=="":
        messagebox.showwarning("warn..", "plz enter applicant Address",parent=win)
        return
    if s4=="":
        messagebox.showwarning("warn..", "plz enter applicant City",parent=win)
        return
    if s5=="":
        messagebox.showwarning("warn..", "plz enter applicant Contact",parent=win)
        return
    '''if s6=="":
        messagebox.showwarning("warn..", "plz enter applicant Birthdate")
        return'''
    if s7=="":
        messagebox.showwarning("warn..", "plz enter applicant Age",parent=win)
        return
    if s8=="":
        messagebox.showwarning("warn..", "plz enter applicant Nominee",parent=win)
        return
    if s9=="":
        messagebox.showwarning("warn..", "plz enter applicant Op bal",parent=win)
        return
    #if s10=="":
       # messagebox.showwarning("warn..", "plz enter applicant Gender")
       # return

    mydb=mysql.connector.connect(
        user="root",
        password="",
        host="localhost",
        database="bank"
    )
    mycur=mydb.cursor()
    mycur.execute("update applicant set appname='"+s2+"',apadd='"+s3+"',city='"+s4+"',contact='"+s5+"',age="+s7+",nominee='"+s8+"',opbal='"+s9+"' where apno='"+s1+"'")
    mydb.commit()
    messagebox.showinfo("confirm","Rec is update",parent=win)
    t1.delete(0,END)
    clfield()

def delrec():
    s1=t1.get()
    mydb=mysql.connector.connect(
        user="root",
        password="",
        host="localhost",
        database="bank"
    )
    ans=messagebox.askyesnocancel("confirm","are U sure delete?",parent=win)
    if ans==True:
        mycur=mydb.cursor()
        mycur.execute("delete from applicant where apno="+s1+"")
        mydb.commit()
        messagebox.showinfo("confirm","Rec is delete",parent=win)
        t1.delete(0,END)
        clfield()


#back image
img = Image.open("D:\Savingbank\patil8.jpg")
img=img.resize((1600,850))
my = ImageTk.PhotoImage(img)
label = Label(win, image=my)
label.pack(side=LEFT,fill=BOTH,expand=True)

Frame_Login=Frame(win,bg="saddlebrown",highlightbackground="gray",highlightthickness=3)
Frame_Login.place(x=300,y=30,width=550,height=630)

title=Label(Frame_Login,text="Applicant Form  ",font=("impact",35,"bold","underline"),bg="#FFCCCC",fg="black")
title.place(x=90,y=20)

#apno
l1=Label(Frame_Login,text="Applicant_No  ",font=("times in roman",15),bg="#FFCCCC",fg="black")
l1.place(x=90,y=100)
t1=Entry(Frame_Login,font=("times new roman",15))
t1.place(x=280,y=100)

#apname
l2=Label(Frame_Login,text="Applicant_Name_  ",font=("times in roman",15),bg="#FFCCCC",fg="black")
l2.place(x=90,y=150)
t2=Entry(Frame_Login,font=("times new roman",15))
t2.place(x=280,y=150)

#apadd
l3=Label(Frame_Login,text="Address_  ",font=("times in roman",15),bg="#FFCCCC",fg="black")
l3.place(x=90,y=200)
t3=Entry(Frame_Login,font=("times new roman",15))
t3.place(x=280,y=200)

#city
l4=Label(Frame_Login,text="City_  ",font=("times in roman",15),bg="#FFCCCC",fg="black")
l4.place(x=90,y=250)
data=("Amalner","Bhadgaon","Chinchvad","Chicholi","Dhule","Mumbai","Pune")
t4=Combobox(Frame_Login,values=data,font=("times new roman",13))
t4.place(x=280,y=250)

#contact
l5=Label(Frame_Login,text="Contact_  ",font=("times in roman",15),bg="#FFCCCC",fg="black")
l5.place(x=90,y=300)
t5=Entry(Frame_Login,font=("times new roman",15))
t5.place(x=280,y=300)

#birth date
l6=Label(Frame_Login,text="Birth_Date_  ",font=("times in roman",15),bg="#FFCCCC",fg="black")
l6.place(x=90,y=350)
cal=DateEntry(Frame_Login,selectmode="day",font=("times in roman",13),width=20)
cal.place(x=280,y=350)

#age
l7=Label(Frame_Login,text="Age_  ",font=("times in roman",15),bg="#FFCCCC",fg="black")
l7.place(x=90,y=400)
sp=Spinbox(Frame_Login,from_=1,to_=150,font=("times in roman",13))
sp.place(x=280,y=400)


#nominee
l8=Label(Frame_Login,text="Nominee_Name  ",font=("times in roman",15),bg="#FFCCCC",fg="black")
l8.place(x=90,y=450)
t6=Entry(Frame_Login,font=("times new roman",15))
t6.place(x=280,y=450)

#opening bal
l9=Label(Frame_Login,text="Opening_Bal_  ",font=("times in roman",15),bg="#FFCCCC",fg="black")
l9.place(x=90,y=500)
t7=Entry(Frame_Login,font=("times new roman",15))
t7.place(x=280,y=500)

#Gender
l10=Label(Frame_Login,text="Gender_  ",font=("times in roman",15),bg="#FFCCCC",fg="black")
l10.place(x=90,y=550)
data=("Male","Female","other")
t8=Combobox(Frame_Login,values=data,font=("times new roman",13))
t8.place(x=280,y=550)

b1=Button(win,text="ADD",font=("times new roman",16),bg="#FFCCCC",fg="black",width=8,command=maxrec)
b1.place(x=260,y=670)

b2=Button(win,text="SAVE",font=("times new roman",16),bg="#FFCCCC",fg="black",width=8,command=saverec)
b2.place(x=370,y=670)

b3=Button(win,text="SEARCH",font=("times new roman",16),bg="#FFCCCC",fg="black",width=8,command=serrec)
b3.place(x=480,y=670)

b4=Button(win,text="UPDATE",font=("times new roman",16),bg="#FFCCCC",fg="black",width=8,command=uprec)
b4.place(x=590,y=670)

b5=Button(win,text="DELETE",font=("times new roman",16),bg="#FFCCCC",fg="black",width=8,command=delrec)
b5.place(x=700,y=670)

b6=Button(win,text="EXIT",font=("times new roman",16),bg="#FFCCCC",fg="black",width=8,command=quit)
b6.place(x=810,y=670)


win.mainloop()