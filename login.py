from tkinter import*
# from tkinter import tk
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from time import strftime
from datetime import datetime
from PIL import Image , ImageTk
from registration import Student
from train import Train
from face_recognition import Face_Recognition_sys 
from attendance import Attendance
from chatbot import Chatbot
from developer import Developer
import os


#----------------------------------main function ---------------------------------------------
def main():
   win=Tk()
   app=Login_window(win)
   win.mainloop()


#@@@@@@@@@@@@@@@@@@@@@@@-----class login_window-------@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
class Login_window:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1410x710+0+0")
        self.root.title("Login")
        

        #bg img 
        self.bg=ImageTk.PhotoImage(file=r"img\signin.png")
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relheight=1,relwidth=1)
 
        # frame
        frame=Frame(self.root,bd=5,bg="white")
        frame.place(x=745,y=75,width=525,height=564)

        #label
        title_lbl = Label(frame,text="User Login",font =("Ink Free",40,"bold underline"),justify="center",bg = "white",fg="purple")
        title_lbl.place(x=130,y=20)

        #username
        username = Label(frame,text="Username",font =("Ink Free",20,"bold "),bg = "white",fg="purple")
        username.place(x=20,y=110)

        self.txtuser=ttk.Entry(frame,width=34,font=("times new roman",20,"bold"))
        self.txtuser.place(x=20,y=155)

        #password
        password = Label(frame,text="Password",font =("Ink Free",20,"bold "),justify="center",bg = "white",fg="purple")
        password.place(x=20,y=220)

        self.txtpass=ttk.Entry(frame,width=34,font=("times new roman",20,"bold"))
        self.txtpass.place(x=20,y=265)

        #login button
        login_bt=Button(frame,text="Login",command=self.login,font=("times new roman",18,"bold"),width=27,cursor='hand2',bg="purple",fg="white",activebackground='white',activeforeground='purple')
        login_bt.place(x=70,y=350)

        #New User Registerbutton
        new_user_bt=Button(frame,text="New User Register",command=self.register_window,font=("times new roman",15,"bold"),borderwidth=0,bg="white",fg="purple",activebackground='white',activeforeground='purple')
        new_user_bt.place(x=20,y=440)

        #forget Password button
        forget_bt=Button(frame,text="Forget Password?",command=self.forget_password_window,font=("times new roman",15,"bold"),borderwidth=0,bg="white",fg="purple",activebackground='white',activeforeground='purple')
        forget_bt.place(x=20,y=490)

    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=signup_window(self.new_window)
       
    #================login button functionality=============
    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
          messagebox.showerror("error","All field required")
        elif self.txtuser.get()=="rishit" and self.txtpass.get()=="rishit":
          messagebox.showinfo("success","rishit you are in ")
        else:
          conn=mysql.connector.connect(host="localhost",user="root",password="MYSQL123",database="face_db")
          my_cursor=conn.cursor()
          query="select * from register_user where email=%s and password=%s"
          values=(self.txtuser.get(),self.txtpass.get())
          my_cursor.execute(query,values)
          row=my_cursor.fetchone()
          if row is None:
            messagebox.showerror("Error","Invalid Username & Password")
          else:
            open_main=messagebox.askyesno("YesNo","Access Only Admin")
            if open_main>0:
              self.new_window=Toplevel(self.root)
              self.app=Face_Recognition_System(self.new_window)
            else:
              if not open_main:
                return
            conn.commit()
            conn.close()

    #================reset password   functionality=============
    def reset_pass(self):
        if self.sec_q_combo.get()=="Select":
          messagebox.showerror("Error","Please select security question",parent=self.root2)
        elif self.secansw_.get()=="":
          messagebox.showerror("Error","Please select security question",parent=self.root2)
        elif self.newpassword.get()=="":
          messagebox.showerror("Error","Please select security question",parent=self.root2)
        else:
          conn=mysql.connector.connect(host="localhost",user="root",password="MYSQL123",database="face_db")
          my_cursor=conn.cursor()
          query="select * from register_user where email=%s and securityQ=%s"
          value=(self.txtuser.get(),self.sec_q_combo.get(),self.secansw_)
          my_cursor.execute(query,value)
          row=my_cursor.fetchone()
          if row is None:
            messagebox.showerror("Error","Please enter correct Answer ",parent=self.root2)
          else:
            query="update register set password=%s where email=%s"
            value=(self.newpassword.get(),self.txtuser.get())
            my_cursor.execute(query,value)

            conn.commit()
            conn.close()
            messagebox.showinfo("Info","Your password has been reset,Please login with new password",parent=self.root2)
            self.root2.destroy() 


    #================forgot password  window functionality=============
    def forget_password_window(self):
        if self.txtuser.get()=="":
          messagebox.showerror("Error","Please enter email address to reset password") 
        else:
          conn=mysql.connector.connect(host="localhost",user="root",password="MYSQL123",database="face_db")
          my_cursor=conn.cursor()
          query="select * from register_user where email=%s"
          value=(self.txtuser.get(),)
          my_cursor.execute(query,value)
          row=my_cursor.fetchone()
          if row is None:
            messagebox.showerror("Error","Please enter the valid username ")
          else:
            self.root2=Toplevel()
            self.root2.geometry("850x455+270+130")  #850x455+270+130
            self.root2.title("Forget Password")

            # frame
            frame=Frame(self.root2,bd=5,bg="white")
            frame.place(x=0,y=0,width=850,height=455)

            #bg img 
            bg_img=Image.open(r"img/111.png")
            bg_img=bg_img.resize((850,455),Image.LANCZOS)
            self.photoimg_bg=ImageTk.PhotoImage(bg_img)

            bg_img=Label(frame,image=self.photoimg_bg)
            bg_img.place(x=0,y=0,width=850,height=455)

            #inner frame
            inn_frame=Frame(self.root2,bd=5,bg="white")
            inn_frame.place(x=450,y=30,width=381,height=395)

            title_lbl = Label(inn_frame,text="Forget Password",font =("Ink Free",20,"bold underline"),bg = "white",fg="purple")
            title_lbl.place(x=80,y=20)

            #Security question

            
            Sec_q=Label(inn_frame,text="Select Security Question",font=("Ink Free",14,"bold"),width=30,bg="white",fg="purple",anchor=W)
            Sec_q.place(x=25,y=80)

            sec_q_combo=ttk.Combobox(inn_frame,font=("times new roman",15),width=30,state="readonly",foreground='purple') #dropdown box create combobox
            sec_q_combo["values"]=("Select","Your Birth Place","Your Nickname","Your favourite Color")
            sec_q_combo.current(0)
            sec_q_combo.place(x=25,y=110)

            
            

            #security answer
            sec_answ = Label(inn_frame,text="Security Answer",font =("Ink Free",14,"bold "),bg = "white",fg="purple")
            sec_answ.place(x=25,y=150)

            self.secansw_=ttk.Entry(inn_frame,width=32,font=("times new roman",14,"bold"))
            self.secansw_.place(x=25,y=180)

            #new password
            newpass = Label(inn_frame,text="New Password",font =("Ink Free",14,"bold "),bg = "white",fg="purple")
            newpass.place(x=25,y=220)

            self.newpassword=ttk.Entry(inn_frame,width=32,font=("times new roman",14,"bold"))
            self.newpassword.place(x=25,y=250)

             #RESET BUTTON
            reset=Button(inn_frame,text="RESET",command=self.reset_pass,font=("times new roman",14,"bold"),width=13,bg="purple",fg="white")
            reset.place(x=100,y=320)



#@@@@@@@@@@@@@@@@@@@@@@@-----class signup_window-------@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@        
class signup_window:
  def __init__(self,root):
    self.root=root
    self.root.geometry("1410x710+0+0")
    self.root.title("Signup")

    #==============variables declaration=============================
    self.var_fname=StringVar()
    self.var_lname=StringVar()
    self.var_contact=StringVar()
    self.var_email=StringVar()
    self.var_securityQ=StringVar()
    self.var_securityA=StringVar()
    self.var_pass=StringVar()
    self.var_confpass=StringVar()
    

    #bg img 
    self.bg=ImageTk.PhotoImage(file=r"img\login.png")
    lbl_bg=Label(self.root,image=self.bg)
    lbl_bg.place(x=0,y=0,relheight=1,relwidth=1)
 
    # frame
    frame=Frame(self.root,bd=5,bg="white")
    frame.place(x=640,y=70,width=636,height=576)

    #label
    title_lbl = Label(frame,text="Register Here",font =("Ink Free",40,"bold underline"),bg = "white",fg="purple")
    title_lbl.place(x=130,y=10)

    #First name
    f_name = Label(frame,text="First Name",font =("Ink Free",18,"bold "),bg = "white",fg="purple")
    f_name.place(x=20,y=90)

    self.fname=ttk.Entry(frame,width=22,font=("times new roman",18,"bold"),textvariable=self.var_fname)
    self.fname.place(x=20,y=135)

        
    #last name
    f_name = Label(frame,text="Last Name",font =("Ink Free",18,"bold "),bg = "white",fg="purple")
    f_name.place(x=320,y=90)

    self.txtuser=ttk.Entry(frame,width=22,font=("times new roman",18,"bold"),textvariable=self.var_lname)
    self.txtuser.place(x=320,y=135)

    #number
    number = Label(frame,text="Contact No.",font =("Ink Free",18,"bold "),bg = "white",fg="purple")
    number.place(x=20,y=180)
    
    self.no=ttk.Entry(frame,width=22,font=("times new roman",18,"bold"),textvariable=self.var_contact)
    self.no.place(x=20,y=225)

        
    #EMail
    email = Label(frame,text="EMail",font =("Ink Free",18,"bold "),bg = "white",fg="purple")
    email.place(x=320,y=180)

    self.txtemail=ttk.Entry(frame,width=22,font=("times new roman",18,"bold"),textvariable=self.var_email)
    self.txtemail.place(x=320,y=225)

    # Security question
    Sec_q=Label(frame,text="Select Security Question",font=("Ink Free",18,"bold"),width=30,bg="white",fg="purple",anchor=W)
    Sec_q.place(x=20,y=270)

    sec_q_combo=ttk.Combobox(frame,font=("times new roman",18),width=21,state="readonly",foreground='purple',textvariable=self.var_securityQ) #dropdown box create combobox
    sec_q_combo["values"]=("Select","Your Birth Place","Your Nickname","Your favourite Color")
    sec_q_combo.current(0)
    sec_q_combo.place(x=20,y=315)

    #security answer
    sec_ans = Label(frame,text="Security Answer",font =("Ink Free",18,"bold "),bg = "white",fg="purple")
    sec_ans.place(x=320,y=270)

    self.txt_sec_ans=ttk.Entry(frame,width=22,font=("times new roman",18,"bold"),textvariable=self.var_securityA)
    self.txt_sec_ans.place(x=320,y=315)

    #password
    passwd = Label(frame,text="Password",font =("Ink Free",18,"bold "),bg = "white",fg="purple")
    passwd.place(x=20,y=360)

    self.txtpass=ttk.Entry(frame,width=22,font=("times new roman",18,"bold"),textvariable=self.var_pass)
    self.txtpass.place(x=20,y=405)

    #C pass
    conf_pass = Label(frame,text="Confirm Password",font =("Ink Free",18,"bold "),bg = "white",fg="purple")
    conf_pass.place(x=320,y=360)

    self.conf_passwd=ttk.Entry(frame,width=22,font=("times new roman",18,"bold"),textvariable=self.var_confpass)
    self.conf_passwd.place(x=320,y=405)

    #check botton
    self.var_check=IntVar()
    check=Checkbutton(frame,variable=self.var_check,text="I Agree to the terms & condition",font=("times new roman",15,"bold"),bg = "white",fg="purple",activebackground="white",activeforeground="purple",onvalue=1,offvalue=0)
    check.place(x=20,y=450)

    #register button
    login_bt=Button(frame,text="Register",command=self.register_data,font=("times new roman",18,"bold"),width=20,cursor='hand2',bg="purple",fg="white",activebackground='white',activeforeground='purple')
    login_bt.place(x=170,y=490)

    #login
    f_name = Button(frame,text="Login",command=self.return_login,font =("Ink Free",14,"bold underline "),border=0,bg = "white",fg="purple")
    f_name.place(x=285,y=540)

  #================================functions =============================================================
  def register_data(self):
    if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="Select":
      messagebox.showerror("Error","All field are required",parent=self.root)
    elif self.var_pass.get()!=self.var_confpass.get():
      messagebox.showerror("Error","Password & Confirm Password must be same",parent=self.root)
    elif self.var_check.get()==0:
      messagebox.showerror("Error","Please agree our terms & condition",parent=self.root)
    else:
      conn=mysql.connector.connect(host="localhost",user="root",password="MYSQL123",database="face_db")
      my_cursor=conn.cursor()
      query=("select * from register_user where email=%s")
      value=(self.var_email.get(),)
      my_cursor.execute(query,value)
      row=my_cursor.fetchone()
      if row!=None:
        messagebox.showerror("Error","User already exist,please try with another email",parent=self.root)
      else:
        my_cursor.execute("insert into register_user values(%s,%s,%s,%s,%s,%s,%s)",(self.var_fname.get(),self.var_lname.get(),self.var_contact.get(),self.var_email.get(),self.var_securityQ.get(),self.var_securityA.get(),self.var_pass.get()))
        messagebox.showinfo("Success","Registered successfully ",parent=self.root)
      conn.commit()
      conn.close()

  def return_login(self):
     self.root.destroy()
      
    
#@@@@@@@@@@@@@@@@@@@@@@@-----class main_window-------@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1410x710+0+0")
        self.root.title("face Recognition System")

        
        #main frame
        main_frame=Frame(self.root,bd=5,bg="white")
        main_frame.place(x=0,y=0,width=1410,height=710)

        bg_img=Image.open(r"img/bg.jpg")
        bg_img=bg_img.resize((650,650),Image.LANCZOS)
        self.photoimg_bg=ImageTk.PhotoImage(bg_img)

        bg_img=Label(main_frame,image=self.photoimg_bg)
        bg_img.place(x=700,y=15,width=650,height=650)

        title_lbl = Label(main_frame,text="FACE  RECOGNITION  ATTENDANCE  SYSTEM",font =("Ink Free",35,"bold"),justify="center",bg = "purple",fg="white")
        title_lbl.place(x=0,y=0,width=1410,height=100)

        #student button img
        img1=Image.open("img/stu_form.jpg")
        img1=img1.resize((150,150),Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        b1=Button(main_frame,image=self.photoimg1,command=self.student_details,cursor="hand2",border=0)
        b1.place(x=50,y=130,width=150,height=150)

        b1_1=Button(main_frame,text="Registration",command=self.student_details,cursor="hand2",font =("Ink Free",16,"bold underline"),bg = "white",fg="purple",activebackground="purple",activeforeground="white",bd=0)
        b1_1.place(x=52,y=280,width=155,height=30)

        #face detection  button img
        img2=Image.open(r"img/face.jpg")
        img2=img2.resize((150,150),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        b2=Button(main_frame,image=self.photoimg2,command=self.face_data,cursor="hand2",border=0)
        b2.place(x=300,y=130,width=150,height=150)

        b2_1=Button(main_frame,text="Face Detector",command=self.face_data,cursor="hand2",font =("Ink Free",16,"bold underline"),bg = "white",fg="purple",activebackground="purple",activeforeground="white",bd=0)
        b2_1.place(x=302,y=280,width=150,height=30)

        #train data   button img
        img3=Image.open(r"img/train_data.jpg")
        img3=img3.resize((150,150),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        b3=Button(main_frame,image=self.photoimg3,cursor="hand2",command=self.train_data,border=0)
        b3.place(x=540,y=130,width=150,height=150)

        b3_1=Button(main_frame,text="Train Data",cursor="hand2",command=self.train_data,font =("Ink Free",18,"bold underline"),bg = "white",fg="purple",activebackground="purple",activeforeground="white",bd=0)
        b3_1.place(x=542,y=280,width=150,height=30)

        #help button img
        img4=Image.open(r"img/helpp.jpg")
        img4=img4.resize((150,150),Image.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b4=Button(main_frame,image=self.photoimg4,cursor="hand2",command=self.chat_data,border=0)
        b4.place(x=50,y=510,width=150,height=150)

        b4_1=Button(main_frame,text="Help",cursor="hand2",font =("Ink Free",18,"bold underline"),command=self.chat_data,bg = "white",fg="purple",activebackground="purple",activeforeground="white",bd=0)
        b4_1.place(x=52,y=660,width=150,height=30)

        #attendance  button img
        img5=Image.open(r"img/attendance.png")
        img5=img5.resize((560,150),Image.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b5=Button(main_frame,image=self.photoimg5,cursor="hand2",command=self.attendance_data,border=0)
        b5.place(x=80,y=320,width=560,height=150)

        b5_1=Button(main_frame,text="Attendance",cursor="hand2",command=self.attendance_data,font =("Ink Free",18,"bold underline"),bg = "white",fg="purple",activebackground="purple",activeforeground="white",bd=0)
        b5_1.place(x=80,y=470,width=560,height=30)

        #photos button img
        img7=Image.open(r"img/photo1.jpg")
        img7=img7.resize((150,150),Image.LANCZOS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        b7=Button(main_frame,image=self.photoimg7,cursor="hand2",command=self.open_img,border=0)
        b7.place(x=300,y=510,width=150,height=150)

        b7_1=Button(main_frame,text="Photos",cursor="hand2",command=self.open_img,font =("Ink Free",18,"bold underline"),bg = "white",fg="purple",activebackground="purple",activeforeground="white",bd=0)
        b7_1.place(x=302,y=660,width=150,height=30)

        #developer button img
        img6=Image.open("img/dev.jpg")
        img6=img6.resize((150,150),Image.LANCZOS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b6=Button(main_frame,image=self.photoimg6,command=self.developer_data,cursor="hand2",border=0)
        b6.place(x=540,y=510,width=150,height=150)

        b6_1=Button(main_frame,text="Developer",command=self.developer_data,cursor="hand2",font =("Ink Free",18,"bold underline"),bg = "white",fg="purple",activebackground="purple",activeforeground="white",bd=0)
        b6_1.place(x=542,y=660,width=150,height=30)

        #exit button
        b8_1=Button(main_frame,text="Exit",cursor="hand2",font =("Ink Free",18,"bold"),command=self.exit,bg = "white",fg="purple",activebackground="purple",activeforeground="white",bd=0)
        b8_1.place(x=1280,y=100,width=50,height=30)

        #time button
        b7_1=Button(main_frame,font =("times new roman",18,"bold"),command=self.present_time)
        b7_1.place(x=764,y=610,width=560,height=40)

        # Label for displaying time
        self.lbl = Label(main_frame, font=("times new roman", 18, "bold"), bg="purple", fg="white")
        self.lbl.place(x=764, y=610, width=560, height=40)
        self.present_time()  
    

   #=============time function======================================================

    def present_time(self):
        string = strftime('%I:%M:%S %p')
        self.lbl.config(text=string)
        self.lbl.after(1000, self.present_time)
  
    

    #================open image ======================================================
    def open_img(self):
            os.startfile("faces")

    #================exit ======================================================
    def exit(self):
        self.exit=messagebox.askyesno("Face Recognition ","Do you want to Exit ")
        if self.exit>0:
            self.root.destroy()
        else:
            return


        #================ function buttons  ======================================================

    def student_details(self):
            self.new_window=Toplevel(self.root)
            self.app=Student(self.new_window) 
    def train_data(self):
            self.new_window=Toplevel(self.root)
            self.app=Train(self.new_window)  
        
    def face_data(self):
            self.new_window=Toplevel(self.root)
            self.app=Face_Recognition_sys(self.new_window) 
    def attendance_data(self):
            self.new_window=Toplevel(self.root)
            self.app=Attendance(self.new_window) 
    def developer_data(self):
            self.new_window=Toplevel(self.root)
            self.app=Developer(self.new_window) 
    def chat_data(self):
            self.new_window=Toplevel(self.root)
            self.app=Chatbot(self.new_window) 





if __name__=="__main__":
    main()