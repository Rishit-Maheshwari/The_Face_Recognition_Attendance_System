from tkinter import*
from tkinter import ttk 
from PIL import Image , ImageTk
from tkinter import messagebox
from time import strftime
from datetime import datetime
import os
import csv
from tkinter import filedialog
import pyttsx3

#============================variable for voice command ========================================
start=pyttsx3.init()




#final

mydata=[]
class Attendance:
        def __init__(self,root):
            self.root=root
            self.root.geometry("1410x710+0+0")
            self.root.title("Attendance Management System")


        #-------varible
            self.var_atten_id=StringVar()
            self.var_atten_roll=StringVar()
            self.var_atten_name=StringVar()
            self.var_atten_dep=StringVar()
            self.var_atten_time=StringVar()
            self.var_atten_date=StringVar()
            self.var_atten_attendance=StringVar()

            title_lbl = Label(self.root,text="ATTENDANCE MANAGEMENT SYSTEM",font =("times new roman",35,"bold"),justify="center",bg = "purple",fg="white")
            title_lbl.place(x=0,y=0,width=1410,height=70)

            #main frame
            main_frame=Frame(self.root,bd=5,bg="white")
            main_frame.place(x=0,y=75,width=1410,height=620)

            #left label frame (STUDENT INFORMATION)
            Left_frame=LabelFrame(main_frame,border=5,bg="white",relief=RIDGE,text="Student Attendance Details",font=("times new roman",28,"bold"),fg="purple",bd=8)
            Left_frame.place(x=3,y=4,width=550,height=610)

            #img 
            bg_img=Image.open(r"img/attendance.png")
            bg_img=bg_img.resize((520,150),Image.LANCZOS)
            self.photoimg_bg=ImageTk.PhotoImage(bg_img)

            bg_img=Label(Left_frame,image=self.photoimg_bg,border=0)
            bg_img.place(x=5,y=5,width=520,height=150)

            #time button
            b7_1=Button(Left_frame,font =("times new roman",18,"bold"),command=self.present_time)
            b7_1.place(x=360,y=140,width=150,height=40)

            # Label for displaying time
            self.lbl = Label(Left_frame, font=("times new roman", 18, "bold"), bg="white", fg="purple")
            self.lbl.place(x=360, y=140, width=150, height=40)
            self.present_time()  

            #frame for details
            details_frame=LabelFrame(Left_frame,border=5,bg="white",relief=RIDGE,fg="purple",font=("times new roman",16,"bold"))
            details_frame.place(x=5,y=180,width=520,height=370)       

            #=======================================labal and entry===========================================
            #attendanceid
            ATT_ID_labal=Label(details_frame,text="AttendanceID:",font=("times new roman",12,"bold"),width=14,bg="white",anchor="w")
            ATT_ID_labal.grid(row=0,column=0,padx=6,pady=10,sticky=W)
            
            att_id_entry=ttk.Entry(details_frame,width=22,textvariable=self.var_atten_id,font=("times new roman",12,"bold"))
            att_id_entry.grid(row=0,column=1,padx=6,pady=10)

            #roll
            roll=Label(details_frame,text="Roll number:",font=("times new roman",12,"bold"),width=12,bg="white",anchor="w")
            roll.grid(row=1,column=0,padx=6,pady=10,sticky=W)
            
            roll_entry=ttk.Entry(details_frame,width=22,textvariable=self.var_atten_roll,font=("times new roman",12,"bold"))
            roll_entry.grid(row=1,column=1,padx=6,pady=10,sticky=W)   

            #name
            STU_name=Label(details_frame,text="Name:",font=("times new roman",12,"bold"),width=12,bg="white",anchor="w")
            STU_name.grid(row=3,column=0,padx=6,pady=10,sticky=W)
            
            stu_name_entry=ttk.Entry(details_frame,width=22,textvariable=self.var_atten_name,font=("times new roman",12,"bold"))
            stu_name_entry.grid(row=3,column=1,padx=6,pady=10,sticky=W) 

            #department 
            STU_department=Label(details_frame,text="department:",font=("times new roman",12,"bold"),width=12,bg="white",anchor="w")
            STU_department.grid(row=2,column=0,padx=6,pady=10,sticky=W)
            
            stu_department_entry=ttk.Entry(details_frame,width=22,textvariable=self.var_atten_dep,font=("times new roman",12,"bold"))
            stu_department_entry.grid(row=2,column=1,padx=6,pady=10,sticky=W)  


            #TIME
            STU_name=Label(details_frame,text="Time:",font=("times new roman",12,"bold"),width=12,bg="white",anchor="w")
            STU_name.grid(row=4,column=0,padx=6,pady=10,sticky=W)
            
            stu_name_entry=ttk.Entry(details_frame,width=22,textvariable=self.var_atten_time,font=("times new roman",12,"bold"))
            stu_name_entry.grid(row=4,column=1,padx=6,pady=10,sticky=W) 

            #DATE
            STU_name=Label(details_frame,text="Date:",font=("times new roman",12,"bold"),width=12,bg="white",anchor="w")
            STU_name.grid(row=5,column=0,padx=6,pady=10,sticky=W)
            
            stu_name_entry=ttk.Entry(details_frame,width=22,textvariable=self.var_atten_date,font=("times new roman",12,"bold"))
            stu_name_entry.grid(row=5,column=1,padx=6,pady=10,sticky=W) 

            #attendance status
            dep_labal=Label(details_frame,text="Attendance Status",font=("times new roman",12,"bold"),width=18,bg="white",anchor="w")
            dep_labal.grid(row=6,column=0,padx=10,sticky=W)

            dep_combo=ttk.Combobox(details_frame,font=("times new roman",12),textvariable=self.var_atten_attendance,width=20,state="readonly") #dropdown box create combobox
            dep_combo["values"]=("Status","Present","Absent")
            dep_combo.current(0)
            dep_combo.grid(row=6,column=1,padx=6,pady=10,sticky=W)

            
            #button frame  1
            btn_frame1=Frame(details_frame,bd=2,relief=RIDGE,bg="white")
            btn_frame1.place(x=0,y=320,width=510,height=36)

            #Import CSV BUTTON
            Import_CSV=Button(btn_frame1,text="Import CSV",command=self.importCsv,font=("times new roman",12,"bold"),width=13,bg="purple",fg="white")
            Import_CSV.grid(row=0,column=0)
            #Export CSV  BUTTON
            Export_CSV=Button(btn_frame1,text="Export CSV",command=self.exportCsv,font=("times new roman",12,"bold"),width=13,bg="purple",fg="white")
            Export_CSV.grid(row=0,column=1)
            #UPDATE  BUTTON
            update=Button(btn_frame1,text="UPDATE",command=self.Update_data,font=("times new roman",12,"bold"),width=13,bg="purple",fg="white")
            update.grid(row=0,column=2)
            #RESET BUTTON
            reset=Button(btn_frame1,text="RESET",command=self.reset_data,font=("times new roman",12,"bold"),width=13,bg="purple",fg="white")
            reset.grid(row=0,column=3)

            #Right label frame 
            Right_frame=LabelFrame(self.root,border=5,bg="white",relief=RIDGE,text="Attendance Detail",font=("times new roman",28,"bold"),fg="purple",bd=8)
            Right_frame.place(x=560,y=84,width=780,height=610)

            #table frame
            table_frame=Frame(Right_frame,bd=2,relief=RIDGE,bg="white")
            table_frame.place(x=5,y=15,width=754,height=540)      

            #----------scrollbar------------------
            scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
            scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
                        
            self.AttendanceReportTable=ttk.Treeview(table_frame,column=("id","roll","name","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

            scroll_x.pack(side=BOTTOM,fill=X)
            scroll_y.pack(side=RIGHT,fill=Y)

            scroll_x.config(command=self.AttendanceReportTable.xview)
            scroll_y.config(command=self.AttendanceReportTable.yview)


            self.AttendanceReportTable.heading("id",text="Attendance ID")
            self.AttendanceReportTable.heading("roll",text="Roll")
            self.AttendanceReportTable.heading("name",text="Name")
            self.AttendanceReportTable.heading("department",text="Department")
            self.AttendanceReportTable.heading("time",text="Time")
            self.AttendanceReportTable.heading("date",text="Date")
            self.AttendanceReportTable.heading("attendance",text="Attendance")

            self.AttendanceReportTable["show"]="headings"
            self.AttendanceReportTable.column("id",width=100)
            self.AttendanceReportTable.column("roll",width=100)
            self.AttendanceReportTable.column("name",width=150)
            self.AttendanceReportTable.column("department",width=100)
            self.AttendanceReportTable.column("time",width=100)
            self.AttendanceReportTable.column("date",width=100)
            self.AttendanceReportTable.column("attendance",width=100)
                        

            self.AttendanceReportTable.pack(fill=BOTH,expand=1)

            self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)
                             
        #=====================================fetch data=====================================

        def fecthData(self,rows):
                self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
                for i in rows:
                        self.AttendanceReportTable.insert("",END,values=i)

        #import csv
        def importCsv(self):
                global mydata
                mydata.clear()
                filename=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("*All File" ,"*.*")),parent=self.root)
                with open(filename) as myfile:
                        csvread=csv.reader(myfile,delimiter=",")
                        for i in csvread:
                                mydata.append(i)
                        self.fecthData(mydata)
        
        #export csv
        def exportCsv(self):
                try:
                        if len(mydata)<1:
                                start.say("No Data found to export")
                                start.runAndWait()
                                messagebox.showerror("No Data","No Data found to export",parent=self.root)
                                return False
                        filename=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("*All File" ,"*.*")),parent=self.root)
                        with open(filename,mode="w",newline="") as myfile:
                                exp_write=csv.writer(myfile,delimiter=",")
                                for i in mydata:
                                        exp_write.writerow(i)
                                start.say("Data exported")
                                start.runAndWait()
                                messagebox.showinfo("Data Export", "Data Exported to"+" " +os.path.basename(filename)+" "+"successfully")
                except Exception as es:
                        start.say("error")
                        start.runAndWait()
                        messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)
                
        def get_cursor(self,event=""):
                cursor_row=self.AttendanceReportTable.focus()
                content=self.AttendanceReportTable.item(cursor_row)
                rows=content["values"]
                self.var_atten_id.set(rows[0])
                self.var_atten_roll.set(rows[1])
                self.var_atten_name.set(rows[2])
                self.var_atten_dep.set(rows[3])
                self.var_atten_time.set(rows[4])
                self.var_atten_date.set(rows[5])
                self.var_atten_attendance.set(rows[6])

        def reset_data(self):
                self.var_atten_id.set("")
                self.var_atten_roll.set("")
                self.var_atten_name.set("")
                self.var_atten_dep.set("")
                self.var_atten_time.set("")
                self.var_atten_date.set("")
                self.var_atten_attendance.set("")
        
        def Update_data(self):
                try:
                        Update = messagebox.askyesno("Update","Do you want to update this student details",parent=self.root)
                        if Update==True:
                                self.var_atten_id.get()
                                self.var_atten_roll.get()
                                self.var_atten_name.get()
                                self.var_atten_dep.get()
                                self.var_atten_time.get()
                                self.var_atten_date.get()
                                self.var_atten_attendance.get()

                        else:
                                if  not Update:
                                        return

                        fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("*All File" ,"*.*")),parent=self.root)
                        with open(fln,mode="w",newline="") as myfile:
                                exp_write=csv.writer(myfile,delimiter=",")
                                for i in mydata:
                                        exp_write.writerow(i)
                        start.say("Student datails updated")
                        start.runAndWait()
                        messagebox.showinfo("Success","Student details succefully updated",parent=self.root)
       
                except Exception as es:
                        start.say("error")
                        start.runAndWait()
                        messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)


        
        #=============time function======================================================

        def present_time(self):
                string = strftime('%I:%M:%S %p')
                self.lbl.config(text=string)
                self.lbl.after(1000, self.present_time)
  

if __name__== "__main__":
        root=Tk()
        obj=Attendance(root)
        root.mainloop()