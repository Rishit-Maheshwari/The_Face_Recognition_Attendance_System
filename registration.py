from  tkinter import*
from  tkinter import ttk,messagebox
from PIL import Image,ImageTk 
import pyttsx3
import mysql.connector
import cv2 
import pyttsx3

#============================variable for voice command ========================================
start=pyttsx3.init()


#============================class student===================================== 
class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1410x710+0+0")
        self.root.title("Student Management System")

        

         #================ veriables=======================
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()
        

        title_lbl = Label(self.root,text="STUDENT MANAGEMENT SYSTEM",font =("times new roman",35,"bold"),justify="center",bg = "purple",fg="white")
        title_lbl.place(x=0,y=0,width=1410,height=70)

        #main frame
        main_frame=Frame(self.root,bd=5,bg="white")
        main_frame.place(x=0,y=75,width=1410,height=620)
        
        #left label frame (STUDENT INFORMATION)
        Left_frame=LabelFrame(main_frame,border=5,bg="white",relief=RIDGE,text="Student Information",font=("times new roman",28,"bold"),fg="purple",bd=8)
        Left_frame.place(x=3,y=4,width=550,height=610)

        #current course information
        current_course_frame=LabelFrame(Left_frame,border=5,bg="white",relief=RIDGE,text="Current course information",fg="purple",font=("times new roman",16,"bold"))
        current_course_frame.place(x=5,y=7,width=300,height=175)

        #1 department
        dep_labal=Label(current_course_frame,text="Department",font=("times new roman",12,"bold"),width=10,bg="white",anchor="w")
        dep_labal.grid(row=0,column=0,padx=5,sticky=W)

        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman",12),width=17,state="readonly") #dropdown box create combobox
        dep_combo["values"]=("Select Department","Computer","IT","Civil","IOT","AIML","Web Development")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=5,sticky=W)

        #2 courses 
        course_labal=Label(current_course_frame,text="Courses",font=("times new roman",12,"bold"),width=10,bg="white",anchor="w")
        course_labal.grid(row=1,column=0,padx=5,sticky=W)

        course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman",12),width=17,state="readonly") #dropdown box create combobox
        course_combo["values"]=("Select Course","B.Tech","BCA","B.sc","M.Tech","MCA","M.sc")
        course_combo.current(0)
        course_combo.grid(row=1,column=1,padx=2,pady=5,sticky=W)
        
        #3 year
        year_labal=Label(current_course_frame,text="Year",font=("times new roman",12,"bold"),width=10,bg="white",anchor="w")
        year_labal.grid(row=2,column=0,padx=5,sticky=W)

        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman",12),width=17,state="readonly") #dropdown box create combobox
        year_combo["values"]=("Select Year",1,2,3,4,2022-24)
        year_combo.current(0)
        year_combo.grid(row=2,column=1,padx=2,pady=5,sticky=W)
        

        #4 semester
        sem_labal=Label(current_course_frame,text="Semester",font=("times new roman",12,"bold"),width=10,bg="white",anchor="w")
        sem_labal.grid(row=3,column=0,padx=5,sticky=W)

        sem_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("times new roman",12),width=17,state="readonly") #dropdown box create combobox
        sem_combo["values"]=("Select Semester","Semester-1","Semester-2","Semester-3","Semester-4","Semester-5","Semester-6","Semester-7","Semester-8")
        sem_combo.current(0)
        sem_combo.grid(row=3,column=1,padx=2,pady=5,sticky=W)

        #img 
        bg_img=Image.open(r"img/form.jpg")
        bg_img=bg_img.resize((180,180),Image.LANCZOS)
        self.photoimg_bg=ImageTk.PhotoImage(bg_img)

        bg_img=Label(self.root,image=self.photoimg_bg,border=0)
        bg_img.place(x=340,y=130,width=180,height=180)

        #Class Student Information
        class_student_frame=LabelFrame(Left_frame,border=5,bg="white",relief=RIDGE,text="Class Student Information",font=("times new roman",16,"bold"),fg="purple")
        class_student_frame.place(x=3,y=200,width=530,height=356)



        #studentId
        STU_ID_labal=Label(class_student_frame,text="StudentID:",font=("times new roman",12,"bold"),width=14,bg="white",anchor="w")
        STU_ID_labal.grid(row=0,column=0,padx=6,pady=2,sticky=W)
         
        stu_id_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_id,width=22,font=("times new roman",12,"bold"))
        stu_id_entry.grid(row=0,column=1,padx=6,pady=2)

        #student name
        STU_name=Label(class_student_frame,text="Student Name:",font=("times new roman",12,"bold"),width=12,bg="white",anchor="w")
        STU_name.grid(row=1,column=0,padx=6,pady=2,sticky=W)
         
        stu_name_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_name,width=22,font=("times new roman",12,"bold"))
        stu_name_entry.grid(row=1,column=1,padx=6,pady=2,sticky=W)

        #class Roll no 
        STU_roll=Label(class_student_frame,text="Roll No:",font=("times new roman",12,"bold"),width=12,bg="white",anchor="w")
        STU_roll.grid(row=2,column=0,padx=6,pady=2,sticky=W)
         
        stu_roll_entry=ttk.Entry(class_student_frame,textvariable=self.var_roll,width=22,font=("times new roman",12,"bold"))
        stu_roll_entry.grid(row=2,column=1,padx=6,pady=2,sticky=W)
         
        #class division 
        STU_div=Label(class_student_frame,text="Class Division:",font=("times new roman",12,"bold"),width=12,bg="white",anchor="w")
        STU_div.grid(row=2,column=2,padx=6,pady=2,sticky=W)
         
        div_combo=ttk.Combobox(class_student_frame,textvariable=self.var_div,font=("times new roman",12),width=4,state="readonly") #dropdown box create combobox
        div_combo["values"]=("A","B","C")
        div_combo.current(0)
        div_combo.grid(row=2,column=3,padx=1,pady=2,sticky=W)

        # DOB
        STU_dob=Label(class_student_frame,text="DOB:",font=("times new roman",12,"bold"),width=10,bg="white",anchor="w")
        STU_dob.grid(row=3,column=0,padx=6,pady=2,sticky=W)
         
        stu_dob_entry=ttk.Entry(class_student_frame,textvariable=self.var_dob,width=22,font=("times new roman",12,"bold"))
        stu_dob_entry.grid(row=3,column=1,padx=6,pady=2,sticky=W)

        # Gender
        STU_gender=Label(class_student_frame,text="Gender:",font=("times new roman",12,"bold"),width=10,bg="white",anchor="w")
        STU_gender.grid(row=3,column=2,padx=6,pady=2,sticky=W)

        gender_combo=ttk.Combobox(class_student_frame,textvariable=self.var_gender,font=("times new roman",12),width=4,state="readonly") #dropdown box create combobox
        gender_combo["values"]=("Male","Female","other")
        gender_combo.current(0)
        gender_combo.grid(row=3,column=3,padx=1,pady=2,sticky=W)

        #Phone No
        STU_phone=Label(class_student_frame,text="Phone No:",font=("times new roman",12,"bold"),width=12,bg="white",anchor="w")
        STU_phone.grid(row=4,column=0,padx=6,pady=2,sticky=W)
         
        stu_phone_entry=ttk.Entry(class_student_frame,textvariable=self.var_phone,width=22,font=("times new roman",12,"bold"))
        stu_phone_entry.grid(row=4,column=1,padx=6,pady=2,sticky=W)

        #EMail
        STU_email=Label(class_student_frame,text="Email:",font=("times new roman",12,"bold"),width=12,bg="white",anchor="w")
        STU_email.grid(row=5,column=0,padx=6,pady=2,sticky=W)
         
        stu_email_entry=ttk.Entry(class_student_frame,textvariable=self.var_email,width=22,font=("times new roman",12,"bold"))
        stu_email_entry.grid(row=5,column=1,padx=6,pady=2,sticky=W)

        #address
        STU_add=Label(class_student_frame,text="Address:",font=("times new roman",12,"bold"),width=12,bg="white",anchor="w")
        STU_add.grid(row=6,column=0,padx=6,pady=2,sticky=W)
         
        stu_add_entry=ttk.Entry(class_student_frame,textvariable=self.var_address,width=22,font=("times new roman",12,"bold"))
        stu_add_entry.grid(row=6,column=1,padx=6,pady=2,sticky=W)

        #Teacher name
        t_name=Label(class_student_frame,text="Teacher name:",font=("times new roman",12,"bold"),width=12,bg="white",anchor="w")
        t_name.grid(row=7,column=0,padx=6,pady=2,sticky=W)
         
        t_id_entry=ttk.Entry(class_student_frame,textvariable=self.var_teacher,width=22,font=("times new roman",12,"bold"))
        t_id_entry.grid(row=7,column=1,padx=6,pady=2,sticky=W)

        #radio button 1
        self.var_radio1=StringVar() #variable declear for db save 
        radio_btn_1=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="Take Photo Sample",value="Yes")
        radio_btn_1.grid(row=8,column=0)
        
        #radio button 2
        radio_btn_2=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="No Photo Sample",value="No")
        radio_btn_2.grid(row=8,column=1)

         #button frame 1
        btn_frame1=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=6,y=250,width=510,height=36)
      
        #ADD PHOTO SAMPLE   BUTTON
        ADD_PHOTO=Button(btn_frame1,text="CAPTURE PHOTO SAMPLE",command=self.generate_dataset,font=("times new roman",12,"bold"),width=27,bg="purple",fg="white")
        ADD_PHOTO.grid(row=0,column=0)
        
        #UPDATE PHOTO SAMPLE 
        UP_PHOTO=Button(btn_frame1,text="UPDATE PHOTO SAMPLE",font=("times new roman",12,"bold"),width=28,bg="purple",fg="white")
        UP_PHOTO.grid(row=0,column=1)

        #button frame  2
        btn_frame2=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame2.place(x=6,y=288,width=510,height=36)

        #SAVE BUTTON
        save=Button(btn_frame2,text="SAVE",command=self.add_data,font=("times new roman",12,"bold"),width=13,bg="purple",fg="white")
        save.grid(row=0,column=0)
        #UPDATE  BUTTON
        update=Button(btn_frame2,text="UPDATE",command=self.update_data,font=("times new roman",12,"bold"),width=13,bg="purple",fg="white")
        update.grid(row=0,column=1)
        #DELETE  BUTTON
        delete=Button(btn_frame2,text="DELETE",command=self.delete_data,font=("times new roman",12,"bold"),width=13,bg="purple",fg="white")
        delete.grid(row=0,column=2)
        #RESET BUTTON
        reset=Button(btn_frame2,text="RESET",command=self.reset_data,font=("times new roman",12,"bold"),width=13,bg="purple",fg="white")
        reset.grid(row=0,column=3)

       

        #Right label frame 
        Right_frame=LabelFrame(main_frame,border=5,bg="white",relief=RIDGE,text="Student Detail",font=("times new roman",28,"bold"),fg="purple",bd=8)
        Right_frame.place(x=560,y=4,width=780,height=610)


         #======search system =============
        
        search_frame=LabelFrame(Right_frame,border=5,bg="white",relief=RIDGE,text="Search System",font=("times new roman",16,"bold"),fg="purple")
        search_frame.place(x=5,y=5,width=755,height=70)

        #search by 
        STU_name=Label(search_frame,text="Search by :",font=("times new roman",12,"bold"),width=8,bg="white")
        STU_name.grid(row=0,column=0,padx=10,pady=6,sticky=W)
        #combo of search by
        search_combo=ttk.Combobox(search_frame,font=("times new roman",12),width=12,state="readonly") #dropdown box create combobox
        search_combo["values"]=("Select","Roll No","Student ID","Phone No")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=8,sticky=W)
        #ENTERY FIELD
        SEARCH_entry=ttk.Entry(search_frame,width=16,font=("times new roman",16,"bold"))
        SEARCH_entry.grid(row=0,column=2,padx=6,pady=2,sticky=W)

        #SEARCH  BUTTON
        delete=Button(search_frame,text="Search",font=("times new roman",12,"bold"),width=15,bg="purple",fg="white")
        delete.grid(row=0,column=3,padx=4)
        #SHOW ALL BUTTON
        reset=Button(search_frame,text="Show All",font=("times new roman",12,"bold"),width=15,bg="purple",fg="white")
        reset.grid(row=0,column=4,padx=4)

        #table frame
        table_frame=Frame(Right_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=5,y=82,width=754,height=472)

        #scrool bar 
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        self.student_table=ttk.Treeview(table_frame,columns=("dep","course","year","sem","id","name","div","roll","gender","dob","email","phone","address","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep",text="Depaertment")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="StudentId")
        self.student_table.heading("name",text="Name") 
        self.student_table.heading("roll",text="Roll No")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("div",text="Division")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone No")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("teacher",text="Teacher")
        self.student_table.heading("photo",text="PhotoSample Status")
        self.student_table["show"]="headings"
        
        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100) 
        self.student_table.column("roll",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("div",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("teacher",width=100)
        self.student_table.column("photo",width=120)
        self.student_table["show"]="headings"

        self.student_table.pack(fill=BOTH,expand=1) 
        self.student_table.bind("<ButtonRelease>",self.get_coursor)
        self.fetch_data()

         #=============== function declartion=======================
    
    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            start.say("All Field are required")
            start.runAndWait()
            messagebox.showerror("Error","All Field are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",user="root",password="MYSQL123",database="face_db")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                                  (self.var_dep.get(),self.var_course.get(),self.var_year.get(),self.var_semester.get(), 
                                   self.var_std_id.get(),  self.var_std_name.get(),self.var_div.get(),self.var_roll.get(),
                                   self.var_gender.get(),self.var_dob.get(),self.var_email.get(),self.var_phone.get(),
                                   self.var_address.get(),self.var_teacher.get(),self.var_radio1.get()))    
                conn.commit()
                self.fetch_data()
                conn.close()
                start.say("Student detail added successfully")
                start.runAndWait()
                messagebox.showinfo("Success","Student details, added successfully",parent=self.root)      
            except Exception as es:
                start.say("Error")
                start.runAndWait()
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)


    #================FETCH DATA ================
    
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",user="root",password="MYSQL123",database="face_db")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()
     
     #================ get cursor (get data in  stu info)================

    def get_coursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data1=content["values"]
        
        self.var_dep.set(data1[0]),
        self.var_course.set(data1[1]),
        self.var_year.set(data1[2]),
        self.var_semester.set(data1[3]),
        self.var_std_id.set(data1[4]),
        self.var_std_name.set(data1[5]),
        self.var_div.set(data1[6]),
        self.var_roll.set(data1[7]),
        self.var_gender.set(data1[8]),
        self.var_dob.set(data1[9]),
        self.var_email.set(data1[10]),
        self.var_phone.set(data1[11]),
        self.var_address.set(data1[12]),
        self.var_teacher.set(data1[13]),
        self.var_radio1.set(data1[14])

    #===============update function=====================

    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            start.say("All Field are required")
            start.runAndWait()
            messagebox.showerror("Error","All Field are required",parent=self.root)  
        else:
            try:
                update=messagebox.askyesno("Update","Do you want to update  this student detail",parent=self.root)
                if update>0:
                    conn=mysql.connector.connect(host="localhost",user="root",password="MYSQL123",database="face_db")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student set  Department=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,DOB=%s,Email=%s,Phone_no=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",(
                    self.var_dep.get(),self.var_course.get(),self.var_year.get(),self.var_semester.get(),  
                    self.var_std_name.get(),self.var_div.get(),self.var_roll.get(),self.var_gender.get(),self.var_dob.get(),
                    self.var_email.get(),self.var_phone.get(),self.var_address.get(),self.var_teacher.get(),self.var_radio1.get(),
                    self.var_std_id.get())) 
                else:
                    if  not update:
                        return
                start.say("Student detail updated ")
                start.runAndWait()
                messagebox.showinfo("Success","Student details ,updated successfully ",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as ex:
                start.say("Error")
                start.runAndWait()
                messagebox.showerror("Error",f"Due To: str{str(ex)}",parent=self.root)
              
        
        
#===============delete function==================
    def delete_data(self):
        if self.var_std_id.get()=="":
            start.say("Student id required")
            start.runAndWait()
            messagebox.showerror("warning","Student id required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Delete record","Do you want to delete this record",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",user="root",password="MYSQL123",database="face_db")
                    my_cursor=conn.cursor()
                    sql="delete from student where Student_id=%s"
                    val=(self.var_std_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                start.say("Student detail deleted")
                start.runAndWait()
                messagebox.showinfo("Delete","Student details deleted successfully",parent=self.root)
            except Exception as ex:
                messagebox.showerror("Error",f"Due To: str{str(ex)}",parent=self.root)   

    #=============reset function==================
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select semester")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_div.set("Select Division")
        self.var_roll.set("")
        self.var_gender.set("Male")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")


    #=====================generate data set or take photo sample =============================================

    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            start.say("All Field are required")
            start.runAndWait()
            messagebox.showerror("Error","All Field are required",parent=self.root) 
        else:
            try:
                conn=mysql.connector.connect(host="localhost",user="root",password="MYSQL123",database="face_db")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("update student set  Department=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,DOB=%s,Email=%s,Phone_no=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",(
                        self.var_dep.get(),self.var_course.get(),self.var_year.get(),self.var_semester.get(),  
                        self.var_std_name.get(),self.var_div.get(),self.var_roll.get(),self.var_gender.get(),self.var_dob.get(),
                        self.var_email.get(),self.var_phone.get(),self.var_address.get(),self.var_teacher.get(),self.var_radio1.get(),
                        self.var_std_id.get()==id+1)) 
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                #==========================load predefiend data on face frontals from opencv==========================================

                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    #scaling factor =1.3
                    #minimum neighbor=5
                    
                    for (x,y,w,h) in faces: # this for creating rectange on faces 
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped
                cap=cv2.VideoCapture(1)   #0 for web cam 
                img_id=0

                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame)is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450)) # w and h 
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="faces\\user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)   #fontScale: float, color: Any, thickness:
                        cv2.imshow("Crooped Face",face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:   #13 is for enter 
                        break
                cap.release()
                cv2.destroyAllWindows()
                start.say("data set generated")
                start.runAndWait()
                messagebox.showinfo("result","Generating data set completed!!! ",parent=self.root)
            except Exception as ex:
                    start.say("Error")
                    start.runAndWait()
                    messagebox.showerror("Error",f"Due To: str{str(ex)}",parent=self.root)


 



if __name__=="__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()
