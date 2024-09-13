from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
import mysql.connector
import random
from tkinter import messagebox
import os

import pyttsx3
import pyttsx3
engine=pyttsx3.init()
def main():
    win=Tk()
    app=Login_window(win)
    win.mainloop()
class Login_window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login System new")
        self.root.geometry("1550x800+0+0")

        #===============Background Images========================
        img = Image.open("D:\\Savingbank\\bhamare1.jpg")
        img = img.resize((1550, 800), Image.ADAPTIVE)
        self.photoimg = ImageTk.PhotoImage(img)

        lblimg = Label(self.root, image=self.photoimg, bd=4, relief=RIDGE)
        lblimg.place(x=0, y=0, width=1550, height=800)

        #============frme==========
        frame = Frame(self.root,bg='black')
        frame.place(x=610, y=170, width=340, height=450)

        #======================logo======================
        img1 = Image.open("C:\\Users\\Admin\\roshaniproject\\hotel_management_system\\patil6.jpg")
        img1 = img1.resize((100, 100), Image.ADAPTIVE)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        lblimg = Label(self.root, image=self.photoimg1,  bg='black',borderwidth=0)
        lblimg.place(x=730, y=175, width=100, height=100)

        #lable
        get_str = Label(frame, text="Get Started", font=("times new roman", 20, "bold"), bg='black',fg="white")
        get_str.place(x=95,y=100)

        username=lbl=Label(frame,text='Username',font=("times new roman", 15, "bold"), bg='black',fg="white")
        username.place(x=70,y=155)

        self.txtuser=ttk.Entry(frame,font=("times new roman", 15, "bold"))
        self.txtuser.place(x=40,y=180,width=270)

        password=lbl=Label(frame,text='Password',font=("times new roman", 15, "bold"), bg='black',fg="white")
        password.place(x=70,y=225)

        self.txtpass = ttk.Entry(frame, font=("times new roman", 15, "bold"),show='*')
        self.txtpass.place(x=40, y=250, width=270)

        #==============Icon Images=====
        img2 = Image.open("C:\\Users\\Admin\\roshaniproject\\hotel_management_system\\patil6.jpg")
        img2 = img2.resize((25, 25), Image.ADAPTIVE)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lblimg = Label(self.root, image=self.photoimg2, bg='black', borderwidth=0)
        lblimg.place(x=650, y=323, width=25, height=25)

        img3 = Image.open("C:\\Users\\Admin\\roshaniproject\\hotel_management_system\\lock4.jpg")
        img3 = img3.resize((25, 25), Image.ADAPTIVE)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        lblimg = Label(self.root, image=self.photoimg3, bg='black', borderwidth=0)
        lblimg.place(x=650, y=395, width=25, height=25)

        #login button
        loginbtn = Button(frame, text="Login", command=self.login, width=22,font=("times new roman", 15, "bold"), bg='red',activeforeground='white',activebackground='red', fg="white",relief=RIDGE, bd=3, cursor="heart")
        loginbtn.place(x=110,y=300,width=120,height=35)



        #registerbutton
        registerbtn = Button(frame, text="New User Register", width=22,font=("times new roman", 10, "bold"), bg='black',
                          activeforeground='white',activebackground='black', fg="white", border=0,
                          cursor="heart")

        registerbtn.place(x=15, y=350, width=160)




        #forget pass btn
        forgenbtn = Button(frame, text="Forget Password", command=self.forgot_password_window,width=22, font=("times new roman", 10, "bold"), bg='black',
                          activeforeground='white',activebackground='black', fg="white",border=0,
                          cursor="heart")
        forgenbtn.place(x=10, y=370, width=160)





    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            engine.say("all field required")
            engine.runAndWait()
            messagebox.showerror("Error","all field required")

        else:
            conn = mysql.connector.connect(
                username="root",
                password="",
                host="localhost",
                database="hotel"
            )
            my_cursor = conn.cursor()
            my_cursor.execute("select * from register where email=%s and password=%s",(
                self.txtuser.get(),
                self.txtpass.get()
            ))
            row=my_cursor.fetchone()
            #print(row)
            if row==None:
                messagebox.showerror("Error","Invalid Username & password")
            else:
                open_main=messagebox.askyesno("YesNo","open the project")
                if open_main>0:
                    engine.say("Hello sir....Welcome to State Bank of India.")
                    engine.runAndWait()
                    import bank_acc_sys
                else:
                    if not open_main:
                        return
            conn.commit()
            conn.close()
#=====================reset password=========================
    def reset_pass(self):
        if self.combo_security_Q.get()=="Select":
            messagebox.showerror("Error","Select sucurity Quetion",parent=self.root2)
        elif self.txt_security.get()=="":
            messagebox.showerror("Error","Please Enter the answer",parent=self.root2)
        elif self.txt_newpass.get()=="":
            messagebox.showerror("Error","Please enter the new password",parent=self.root2)
        else:
            conn = mysql.connector.connect(
                username="root",
                password="",
                host="localhost",
                database="hotel"
            )
            my_cursor = conn.cursor()
            qury=("select * from register where email=%s and securityQ=%s and securityA=%s")
            vlaue=(self.txtuser.get(),self.combo_security_Q.get(),self.txt_security.get())
            my_cursor.execute(qury,vlaue)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Plaese enter correct Answer",parent=self.root2)
            else:
                query=("update register set password=%s where email=%s")
                value=(self.txt_newpass.get(),self.txtuser.get())
                my_cursor.execute(query,value)

                conn.commit()
                conn.close()
                messagebox.showinfo("Info","Your password has been reset, plaese login new password",parent=self.root2)


#==========================forgot_password_window====================================
    def forgot_password_window(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","please Enter the Email address to reset password",parent=self.root)
        else:
            conn = mysql.connector.connect(
                username="root",
                password="",
                host="localhost",
                database="hotel"
            )
            my_cursor = conn.cursor()
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.txtuser.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            #print(row)
            if row==None:
                messagebox.showerror("My Error","Please enter the valid user name",parent=self.root)
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forget Password")
                self.root2.geometry("340x450+610+170")

                l=Label(self.root2,text="Forget Password",font=("times new roman",20,'bold','underline'),fg='red',bg='white',width=21,relief=RIDGE)
                l.place(x=0,y=20,width=339,height=40)

                security_Q = Label(self.root2, text="Select Security Quetions:", font=("times new roman", 15, "bold"),
                                   bg="white")
                security_Q.place(x=50, y=80)

                self.combo_security_Q = ttk.Combobox(self.root2, font=("arial", 13, "bold"),
                                                     width=27,
                                                     state="readonly")
                self.combo_security_Q["value"] = ("Select", "Your Birth Place", "Your BestFriend Name", "Your Pet Name")
                self.combo_security_Q.current(0)
                self.combo_security_Q.place(x=50, y=110, width=250)

                security_A = Label(self.root2, text="Security Answer:",
                                   font=("times new roman", 15, "bold"), bg="white")
                security_A.place(x=50, y=150)

                self.txt_security = ttk.Entry(self.root2, font=("times new roman", 15, "bold"))
                self.txt_security.place(x=50, y=180, width=250)

                new_password = Label(self.root2, text="New Password:",
                                   font=("times new roman", 15, "bold"), bg="white")
                new_password.place(x=50, y=220)

                self.txt_newpass = ttk.Entry(self.root2, font=("times new roman", 15, "bold"))
                self.txt_newpass.place(x=50, y=250, width=250)

                btn=Button(self.root2,text="Reset",command=self.reset_pass,font=("times new roman", 15, "bold"),fg='white',bg='dark green')
                btn.place(x=100,y=290)
                #sabir@gmail.com

    def return_login(self):
        self.root.destroy()

    def rigister_window(self):
        new_window=Toplevel(self.root)







if __name__ == "__main__":
    main()
