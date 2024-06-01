from tkinter import *  # for GUI
from tkinter import ttk  # for stylis
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox


class Chatbot:

    def __init__(self, root):
        self.root = root
        self.root.geometry("730x620+320+40")
        self.root.title("Eddie")
        self.root.bind('<Return>', self.enter_fun)

        # ================== MAIN FRAME =======================
        main_frame = Frame(self.root, bd=4, bg='white',width=610)
        main_frame.pack()
        # ================== IMAGE  =======================
        img = Image.open('img\\eddief.png')
        img = img.resize((150, 150), Image.Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)
        # ================= TITLE ==========================
        title_label = Label(main_frame, bd=3, relief=RAISED, anchor='nw', width=720, compound=LEFT,
                            image=self.photoimg, text="Eddie", font=('poppins', 40, 'bold'), fg='white', bg='purple')
        title_label.pack(side=TOP)

        # ================== SCROLL BAR ========================
        self.scroll_y = ttk.Scrollbar(main_frame, orient=VERTICAL)
        self.scroll_x = ttk.Scrollbar(main_frame, orient=HORIZONTAL)
        self.text = Text(main_frame, width=90, height=20, bd=3, relief=RAISED, font=(
            'poppins', 11), yscrollcommand=self.scroll_y.set,xscrollcommand= self.scroll_x.set)
        self.scroll_y.pack(side=RIGHT, fill=Y)
        self.scroll_x.pack(side=BOTTOM, fill=X)
        self.text.pack()

        # ================== BUTTON FRAME ======================
        btn_frame = Frame(self.root, bg="white",width=720)
        btn_frame.pack()
        # ================== LABEL ======================
        label_1 = Label(btn_frame, text="Type Something", font=(
            'poppins', 14, 'bold'), fg='purple', bg='white')
        label_1.grid(row=0, column=0, padx=5, pady=5, sticky=W)
        self.var_entry1 = StringVar()
        self.entry = ttk.Entry(btn_frame, textvariable=self.var_entry1, width=55, font=('poppins', 11))
        self.entry.grid(row=0, column=1, padx=5, pady=5, sticky=W)

        # ================== BUTTON ======================
        img_chat1 = Image.open('img\\send.png')
        img_chat1 = img_chat1.resize((40, 30), Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img_chat1)

        self.send = Button(btn_frame, command=self.send_message, image=self.photoimg1, width=35, font=(
            'poppins', 11, 'bold'), fg="white",  border=0, activebackground='white',
                           activeforeground='white')
        self.send.grid(row=0, column=2, padx=5, pady=5, sticky=W)

        self.clr = Button(btn_frame, command=self.clear, text="Clear Chat", width=12, font=(
            'poppins', 11, 'bold'), fg="white", bg='purple', border=0, activebackground='white',
                          activeforeground='purple')
        self.clr.grid(row=1, column=0, padx=5, pady=5, sticky=W)

        self.msg = ''
        self.label_11 = Label(btn_frame, text=self.msg, font=(
            'poppins', 14, 'bold'), fg='#fbec04', bg='white')
        self.label_11.grid(row=1, column=1, padx=5, pady=5, sticky=W)

        img_eddie = Image.open('img\\eddief.png')
        img_eddie = img_eddie.resize((40, 30), Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img_eddie)
       

        # ========================= FUNCTION DECLARATION ======================
    

    def enter_fun(self, event=""):
        self.send.invoke()
        self.var_entry1.set('')
        self.delete(0, tk.END)

    # =================== CLEAR FUNCTION ==================
    def clear(self):
        self.text.delete('1.0', END)
        self.var_entry1.set('')

    # =================== SEND FUNCTION ==================
    def send_message(self):
        send = '\t\t\t\t\t\t\t\t' + self.entry.get()+ ': You'
        self.text.insert(END, '\n' + send)
      
        if self.entry.get() == '':
            self.msg = "Please, enter some Input"
            self.label_11.config(text=self.msg, fg='red', bg='white')
        else:
            self.msg = ''
            self.label_11.config(text=self.msg, fg='red')
        if self.entry.get() == 'hello':
            self.text.insert(END, '\n\n' + 'Bot : Hi')

        elif self.entry.get() == 'hi':
            self.text.insert(END, '\n\n' + 'Bot : Hello')


        elif self.entry.get() == 'Fantastic':
            self.text.insert(END, '\n\n' + 'Bot : Nice to Hear')

        elif self.entry.get() == 'What is your name ?':
            self.text.insert(END, '\n\n' + 'Bot : My name is Eddie')

        elif self.entry.get() == 'How to use?':
            self.text.insert(END, '\n\n' + 'Bot : User Manual: Face Recognition Attendance System**\n\n**1. Installation and Launching:**\n1. Download the "Face Recognition Attendance System" application from the provided link.\n2. Install the application by following the installation prompts.\n3. Once installed, launch the application by double-clicking the app icon on your desktop.')


        elif self.entry.get() == 'help':
            self.text.insert(
                END,
                '\n\n' + 'Bot : yes, of course\n\n     1: What is Machine Learning?\n     2: What is Artifical Intelligence?\n     3: How does face Recongnition work?\n     4: Which algorithm did you used in your project?\n     5: What is meant by Haarsacde Open CV(Object Detection)?\n     6: What is meant by LBPH Opencv (Face Recognition)?\n     7: Link for reference.')

        elif self.entry.get() == '1':
            self.text.insert(
                END,
                '\n\n' + 'Bot : Machine learning is a subfield of artificial intelligence\n         which is broadly defined as the capability of a machine \n         to imitate intelligent human behavior.')

        elif self.entry.get() == '2':
            self.text.insert(
                END,
                '\n\n' + 'Bot : Artificial intelligence is the simulation\n         of human intelligence processes by machines,  \n         especially computer systems.')

        elif self.entry.get() == '3':
            self.text.insert(
                END,
                '\n\n' + 'Bot : Facial Recongnition is a way of recognizing\n         a human face through technology.A facial \n         recognition system uses biometrics to map\n         facial features from a photograph or video.\n         It compares the information with a database\n        of known faces to find a match.')
        elif self.entry.get() == '4':
            self.text.insert(
                END,
                '\n\n' + 'Bot : We have used two algorithms in our Project:\n\n         The first One is : Haarscade OpenCv (Object Detection) \n         The Second One is : LBPH OpenCv (Face Recognition)')
        elif self.entry.get() == '5':
            self.text.insert(
                END,
                '\n\n' + 'Bot : Haar cascade is an algorithm that can detect \n         objects in images, irrespective of their scale \n         in image and location.This algorithm is not \n         so complex and can run in real-time. As we\n         are using for face detection so we use frontal \n         face in our project.')
        elif self.entry.get() == '6':
            self.text.insert(
                END,
                '\n\n' + 'Bot : LBPH (Local Binary Pattern Histogram) is a Face-Recognition algorithm \n         it is used to recognize the face of a person.It is known for its performance \n         and how it is able to recognize the face of a person from both front face and\n         side face.')
        elif self.entry.get() == '7':
            self.url = "https://towardsdatascience.com/face-recognition-how-lbph-works-90ec258c3d6b"
            self.text.insert(
                END, '\n\n' + self.url)

        elif self.entry.get() == 'how to use?':
            self.text.insert(
                END,
                '\n\n' + 'Bot : User Manual: Face Recognition Attendance System**\n\n**1. Installation and Launching:**\n1. Download the "Face Recognition Attendance System" application from the provided link.\n2. Install the application by following the installation prompts.\n3. Once installed, launch the application by double-clicking the app icon on your desktop.\n**2. Login:**\n1. Upon launching the app, you will be directed to the login page.\n2. Enter your credentials (username and password) provided to you by the administrator.\n3. Click the "Login" button to access the main dashboard.\n\n**3. Student Registration:**\n1. In the main dashboard, navigate to the "Registration" section.\n2. Click on the "Register New Student" button.\n3. Fill in the required details of the student, including name, roll number, etc.\n4. Capture a photo of the student using the provided camera interface or by uploading a photo.\n5. Click the "Save" button to register the students information and photo.\n\n**4. Face Sample Capture:**\n1. After saving student details, click on the "Capture Face Sample" option\n2. The camera interface will open. Position the student in front of the camera and ensure good lighting.\n3. The system will automatically capture a sample of the students face.\n4. Once captured successfully, the system will save the face sample for future recognition.\n\n**5. Train Data Face Recognition and Attendance:**\n1. From the main dashboard, select the "Train Data" option.\n2. The Train Data interface will open click on "Train Data" option, and the system will train the data for  face recognition.\n\n**6. Face Recognition and Attendance:**\n1. From the main dashboard, select the Face Recognition option.\n2. The camera interface will open, and the system will start real-time face detection and recognition.\n3. As students come in front of the camera one by one, the system will attempt to recognize their faces.\n4. If a students face is recognized, their attendance will be marked as present\n\n.\n5. If a students face is not recognized or if theres an error, the system will prompt for manual attendance entry.\n\n**7. Photo Section:**\n1. In the main dashboard, navigate to the "Photo" to view saved student photos.\n2. Here, you can view and verify the photos captured during student registration.\n\n**8. Chat Bot Assistance:**\n1. If you have any doubts or need assistance, you can access the chatbot feature.\n2. Click on the "Chat Bot" option in the main dashboard.\n3. Type your question or concern, and the chatbot will provide relevant information and solutions.\n\n**9. Exit:**\n1. To get Exit from the application, click on the "Exit " button in the main dashboard.\n\nFor technical support or inquiries, contact rsupport team:\n\nEmail:rishitmaheshwari488@gmail.com\nEmail:pritampratipsingha@gmail.com')


if __name__ == "__main__":
    root = Tk()
    obj = Chatbot(root)
    root.mainloop()