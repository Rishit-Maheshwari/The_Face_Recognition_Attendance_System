from  tkinter import*
from  tkinter import ttk,messagebox
from PIL import Image,ImageTk 
import pyttsx3
import mysql.connector
import cv2 
import os
import numpy  as np
import pyttsx3

#============================variable for voice command ========================================
start=pyttsx3.init()


class Train:
    def __init__(self,root):
        self.root=root  
        self.root.geometry('1530x790+0+0')  
        self.root.title("Train Data") 

        
        #top heading 
        title_label=Label(self.root,text="TRAIN DATA SET",font =("times new roman",35,"bold"),justify="center",bg = "purple",fg="white")
        title_label.place(x=0,y=0,width=1410,height=70)
        
        #main frame
        main_frame=Frame(self.root,bd=5,bg="white")
        main_frame.place(x=0,y=75,width=1410,height=620)

      
        # 1st img 
        img_top=Image.open(r"img\\train.png")
        img_top=img_top.resize((900,650),Image.LANCZOS) 
        self.img_top=ImageTk.PhotoImage(img_top)

        first_label=Label(self.root,image=self.img_top)
        first_label.place(x=0,y=75,width=900,height=610)

        #button
        traindata_btn=Button(main_frame,text="TRAIN DATA",command=self.train_classifier,font=("times new roman",18,"bold"),bg="purple",fg="white")
        traindata_btn.place(x=1050,y=290,width=190,height=50)



    #=================================train classifier=============================================

    def train_classifier(self):
        data_directory=("faces") 
        path=[os.path.join(data_directory,file) for file in os.listdir(data_directory)]

        faces=[]
        id_s=[]
        
        for image in path:
            img=Image.open(image).convert("L")  # this line is for converting the images in gray scale
            imageNp=np.array(img,"uint8")  # uint8:it is a datatype in array 
            id=int(os.path.split(image)[1].split(".")[1])

            faces.append(imageNp)
            id_s.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        id_s=np.array(id_s)

        #=================================train the classifier and save =============================================

        classifier=cv2.face.LBPHFaceRecognizer_create()
        classifier.train(faces,id_s)
        classifier.write("classifier.xml")
        cv2.destroyAllWindows()
        start.say("Training Dataset completed!!")
        start.runAndWait()
        messagebox.showinfo("Result","Training Dataset completed!!",parent=self.root)

if __name__=="__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()