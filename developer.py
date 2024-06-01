from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
import webbrowser

#==============class developer======================================================================

class Developer:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Developer")
        # top heading
        title_label = Label(self.root, text="DEVELOPER", font=("times new roman", 35, "bold"), justify="center",
                            bg="purple", fg="white")
        title_label.place(x=0, y=0, width=1420, height=90)

        def open_url(event):
            webbrowser.open("https://www.linkedin.com/in/rishitmaheshwari02")

        def open_url2(event):
            webbrowser.open("rishitmaheshwari488@gmail.com")

        def open_url3(event):
            webbrowser.open("https://www.linkedin.com/in/pritam-pratip-singha")

        def open_url4(event):
            webbrowser.open("pritampratipsingha@gmail.com")


        # main frame
        main_frame = Frame(self.root, bd=0, relief=RIDGE, bg="white")
        main_frame.place(x=0, y=70, width=1540, height=650)


        # inner frame
        inner_frame = Frame(main_frame, bd=0, relief=RIDGE, bg="white", border=8)
        inner_frame.place(x=35, y=30, width=1300, height=580)

        #===================================== upper text ===================================================================

        dev_label = Label(inner_frame,text="The Face Recognition Attendance System has been developed by Rishit Maheshwari and Pritam Pratip Singha.\n Their combined expertise in software development and AI technology has led to the creation of \n this efficient(Face Recognition Attendance System).\n\n\n",font=("times new roman", 15, "bold"), width=100, height=8, bg="white", fg="purple")
        dev_label.place(x=35, y=10)

        #============================================== rishit =============================================================


        #rishit frame for email and linkedin
        email_frame = Frame(main_frame, bd=0, relief=RIDGE, bg="white", border=0)
        email_frame.place(x=200, y=170, width=1000, height=150)
        
        #name
        label1_name =Label(email_frame, text="Rishit Maheshwari", fg="purple",font=('times new roman', 15, 'bold underline'), width=28, height=2,bg='white')
        label1_name.place(x=290, y=0)

        #email
        label1_email =Label(email_frame, text="Email :", fg="purple",font=('times new roman', 15, 'bold'), width=28, height=2,bg='white')
        label1_email.place(x=150, y=40)

        label1_email_link =Label(email_frame, text="rishitmaheshwari488@gmail.com",cursor="hand2", fg="purple",font=('times new roman', 15, 'bold'), width=24, height=2,bg='white')
        label1_email_link.place(x=350, y=40)
        label1_email_link.bind("<Button-1>", open_url2)

        #linkedin
        label_linked = Label(email_frame, text="Linkedin :", fg="purple",font=('times new roman', 15, 'bold'), width=28, height=2,bg='white')
        label_linked.place(x=100, y=80)

        label_linkedin_link =Label(email_frame, text="https://www.linkedin.com/in/rishitmaheshwari02",cursor="hand2", fg="purple",font=('times new roman', 15, 'bold'), width=35, height=2,bg='white')
        label_linkedin_link.place(x=312, y=80)
        label_linkedin_link.bind("<Button-1>", open_url)

        #============================================== pritam =============================================================

         #rishit frame for email and linkedin
        email1_frame = Frame(main_frame, bd=0, relief=RIDGE, bg="white", border=0)
        email1_frame.place(x=200, y=310, width=1000, height=150)
        
        #name
        label1_name =Label(email1_frame, text="Pritam Pratip Singha", fg="purple",font=('times new roman', 15, 'bold underline'), width=28, height=2,bg='white')
        label1_name.place(x=290, y=0)

        #email
        label1_email =Label(email1_frame, text="Email :", fg="purple",font=('times new roman', 15, 'bold'), width=28, height=2,bg='white')
        label1_email.place(x=190, y=40)

        label1_email_link =Label(email1_frame, text="pritampratipsingha.com",cursor="hand2", fg="purple",font=('times new roman', 15, 'bold'), width=18, height=2,bg='white')
        label1_email_link.place(x=390, y=40)
        label1_email_link.bind("<Button-1>", open_url2)

        #linkedin
        label_linked = Label(email1_frame, text="Linkedin :", fg="purple",font=('times new roman', 15, 'bold'), width=28, height=2,bg='white')
        label_linked.place(x=100, y=80)

        label_linkedin_link =Label(email1_frame, text="https://www.linkedin.com/in/pritam-pratip-singha",cursor="hand2", fg="purple",font=('times new roman', 15, 'bold'), width=35, height=2,bg='white')
        label_linkedin_link.place(x=312, y=80)
        label_linkedin_link.bind("<Button-1>", open_url)

        #================================= Last text ==============================================================
        label_lower_text =Label(inner_frame, text="For any inquiries, suggestions, or collaboration opportunities, feel free to reach out to us via the provided ""email addresses or LinkedIn profiles.\n Your feedback is valuable and contributes to the ongoing improvement of ""the Face \n Recognition Attendance System. \n", font=("times new roman", 15, "bold"),width=100, height=4, bg="white",fg="purple")
        label_lower_text.place(x=35, y=430)


if __name__ == "__main__":
    root = Tk()
    obj = Developer(root)
    root.mainloop()
