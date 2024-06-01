from tkinter import*
from tkinter import ttk
import tkinter 
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
        self.exit=tkinter.messagebox.askyesno("Face Recognition ","Do you want to Exit ")
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
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()
        