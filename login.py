from cProfile import label
from logging import root
from re import I
from sqlite3 import Cursor
from tkinter import *
from tkinter import ttk
from tkinter import font
from turtle import update
from PIL import Image, ImageTk  # pip install pillow
import mysql.connector
from tkinter import messagebox



def main():
    win=Tk()
    app=login_window(win)
    win.mainloop()






class login_window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")
        
        self.bg=ImageTk.PhotoImage(file=r"C:\Users\ASUS\Desktop\VS Code project\Login\Images\3.2.jpg")
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)
        
        frame=Frame(self.root,bg="light yellow")
        frame.place(x=580,y=170,width=380,height=480)
        
        img1=Image.open(r"C:\Users\ASUS\Desktop\VS Code project\Login\Images\image1.jpg")
        img1=img1.resize((175,120),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lblimg1=Label(image=self.photoimage1,bg="black",borderwidth=0)
        lblimg1.place(x=680,y=172,width=175,height=120)
        
        get_str=Label(frame,text="Get Started",font=("times new roman",20,"bold"),fg="black",bg="light yellow")
        get_str.place(x=123,y=122)
        
        # label
        username=Label(frame,text="UserName",font=("times new roman",15,"bold"),fg="black",bg="light yellow")
        username.place(x=70,y=155)
        self.txtuser=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtuser.place(x=40,y=180,width=280)
        
        password=Label(frame,text="Password",font=("times new roman",15,"bold"),fg="black",bg="light yellow")
        password.place(x=70,y=225)
        self.txtpass=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtpass.place(x=40,y=250,width=280)
        
        
        img2=Image.open(r"C:\Users\ASUS\Desktop\VS Code project\Login\Images\user.png")
        img2=img2.resize((25,23),Image.ANTIALIAS)
        self.photoimage2=ImageTk.PhotoImage(img2)
        lblimg1=Label(image=self.photoimage2,bg="black",borderwidth=0)
        lblimg1.place(x=625,y=322,width=25,height=23)
        
        img3=Image.open(r"C:\Users\ASUS\Desktop\VS Code project\Login\Images\pass.png")
        img3=img3.resize((25,25),Image.ANTIALIAS)
        self.photoimage3=ImageTk.PhotoImage(img3)
        lblimg1=Label(image=self.photoimage3,bg="black",borderwidth=0)
        lblimg1.place(x=625,y=395,width=25,height=25)
        
        
        loginbtn=Button(frame,text="Login",command=self.login,font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="gold",bg="black",activebackground="black",activeforeground="gold")
        loginbtn.place(x=130,y=300,width=120,height=35)
        
        
        registerbtn=Button(frame,text="New User",command=self.register_window,borderwidth=0,font=("times new roman",10,"bold"),fg="black",bg="light yellow",activebackground="light yellow",activeforeground="black")
        registerbtn.place(x=5,y=370,width=120)
        
        forgetpassbtn=Button(frame,text="Forget Password",command=self.forgot_password_window,font=("times new roman",10,"bold"),borderwidth=0,fg="black",bg="light yellow",activebackground="light yellow",activeforeground="black")
        forgetpassbtn.place(x=15,y=390,width=140)
        
    
    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)
    
    
    
    
    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get=="":
            messagebox.showerror("Error","All Fiels Are Required")
        elif self.txtuser.get()=="Mohit_Sinha" and self.txtpass.get()=="Mohitsinha80@":
            messagebox.showinfo("Success","Welcome To System")
        else:
            try:
                
                conn=mysql.connector.connect(host="localhost",user="root",password="Mohitsinha80@",database="mydata")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from register where email=%s and password=%s",(
                            self.txtuser.get(),
                            self.txtpass.get()
                    
                             ))
                row=my_cursor.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Username And Password")
                else:
                    open_main=messagebox.askyesno("YesNo","Access Only Admin")
                    if open_main>0:
                        self.new_window=Toplevel(self.root)
                        self.app=student(self.new_window)
                    else:
                        if not open_main:
                            return
                conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error", f"Due To:{str(es)}", parent=self.root)
    
    
    def reset_pass(self):
        if self.combo_security_Q.get()=="Select":
            messagebox.showerror("Error","Show Security Question",parent=self.root2)
        elif self.txt_security.get=="":
            messagebox.showerror("Error","Please Enter Valid Answer",parent=self.root2)
        elif self.txt_newpass.get=="":
            messagebox.showerror("Error","Please Enter New Password",parent=self.root2)
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="Mohitsinha80@",database="mydata")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s and securityQ=%s and securityA=%s")
            value=(self.txtuser.get(),self.combo_security_Q.get(),self.txt_security.get())
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Please Enter Correct Answer",parent=self.root2)
            else:
                query=("update register set password=%s where email=%s")
                value=(self.txt_newpass.get(),self.txtuser.get())
                my_cursor.execute(query,value)
                conn.commit()
                conn.close()
                messagebox.showinfo("Info","Your Password Has Been Reset, Please Login with New Password",parent=self.root2)
                self.root2.destroy()
                
                
            
    
    
    
    
    
    
    
    
    def forgot_password_window(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Please Enter The Email Id To Reset Password")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="Mohitsinha80@",database="mydata")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.txtuser.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Please Enter Valid User Name")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forgot Password")
                self.root2.geometry("450x550+580+170")
                
                l=Label(self.root2,text="Forgot Password",font=("times new roman",20,"bold"),fg="red",bg="white")
                l.place(x=0,y=10,relwidth=1)
                
                Security_Q=Label(self.root2,text="Select Security Question",font=("times new roman",15,"bold"),fg="black",bg="white")
                Security_Q.place(x=50,y=80)
                
                self.combo_security_Q=ttk.Combobox(self.root2,font=("times new roman",15,"bold"),state="readonly")
                self.combo_security_Q["values"]=("Select","Your Birth Place","Your GirlFriend/Boyfriend Name","Your Pet Name")
                self.combo_security_Q.place(x=50,y=110,width=250)
                self.combo_security_Q.current(0)
                Security_A=Label(self.root2,text="Security Answer",font=("times new roman",15,"bold"),fg="black",bg="white")
                Security_A.place(x=50,y=150)
                self.txt_security=ttk.Entry(self.root2,font=("times new roman",15,"bold"))
                self.txt_security.place(x=50,y=180,width=250)
        
                new_password=Label(self.root2,text="New Password",font=("times new roman",15,"bold"),fg="black",bg="white")
                new_password.place(x=50,y=220)
                self.txt_newpass=ttk.Entry(self.root2,font=("times new roman",15,"bold"))
                self.txt_newpass.place(x=50,y=250,width=250)
                
                btn=Button(self.root2,text="Reset",command=self.reset_pass,font=("times new roman",15,"bold"),fg="white",bg="green")
                btn.place(x=150,y=290)
        
            
                
                
            
            

class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1550x800+0+0")
        
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()
        
        
        
        
        self.bg=ImageTk.PhotoImage(file=r"C:\Users\ASUS\Desktop\VS Code project\Login\Images\13.2.jpg")
        bg_lbl=Label(self.root,image=self.bg)
        bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)
        
        self.bg1=ImageTk.PhotoImage(file=r"C:\Users\ASUS\Desktop\VS Code project\Login\Images\12.2.jpg")
        left_lbl=Label(self.root,image=self.bg1)
        left_lbl.place(x=120,y=100,width=470,height=550)
        
        frame=Frame(self.root,bg="light green")
        frame.place(x=580,y=100,width=750,height=550)
        
        register_lbl=Label(frame,text="Register Here",font=("times new roman",25,"bold"),fg="red",bg="light green")
        register_lbl.place(x=250,y=17)
        
        
        fname=Label(frame,text="First Name",font=("times new roman",15,"bold"),fg="red",bg="light green")
        fname.place(x=50,y=100)
        fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",15,"bold"))
        fname_entry.place(x=50,y=130,width=250)
        
        l_name=Label(frame,text="Last Name",font=("times new roman",15,"bold"),fg="red",bg="light green")
        l_name.place(x=370,y=100)
        self.txt_lname=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",15,"bold"))
        self.txt_lname.place(x=370,y=130,width=250)
        
        contact=Label(frame,text="Contact No.",font=("times new roman",15,"bold"),fg="red",bg="light green")
        contact.place(x=50,y=170)
        self.txt_contact=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",15,"bold"))
        self.txt_contact.place(x=50,y=200,width=250)
        
        email=Label(frame,text="Email Id.",font=("times new roman",15,"bold"),fg="red",bg="light green")
        email.place(x=370,y=170)
        self.txt_email=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",15,"bold"))
        self.txt_email.place(x=370,y=200,width=250)
        
        Security_Q=Label(frame,text="Select Security Question",font=("times new roman",15,"bold"),fg="red",bg="light green")
        Security_Q.place(x=50,y=240)
        
        self.combo_security_Q=ttk.Combobox(frame,textvariable=self.var_securityQ,font=("times new roman",15,"bold"),state="readonly")
        self.combo_security_Q["values"]=("Select","Your Birth Place","Your GirlFriend/Boyfriend Name","Your Pet Name")
        self.combo_security_Q.place(x=50,y=270,width=250)
        self.combo_security_Q.current(0)
        Security_A=Label(frame,text="Security Answer",font=("times new roman",15,"bold"),fg="red",bg="light green")
        Security_A.place(x=370,y=240)
        self.txt_security=ttk.Entry(frame,textvariable=self.var_securityA,font=("times new roman",15,"bold"))
        self.txt_security.place(x=370,y=270,width=250)
        
        pswd=Label(frame,text="New Password",font=("times new roman",15,"bold"),fg="red",bg="light green")
        pswd.place(x=50,y=310)
        self.txt_pswd=ttk.Entry(frame,textvariable=self.var_pass,font=("times new roman",15,"bold"))
        self.txt_pswd.place(x=50,y=340,width=250)
        
        confirm_pswd=Label(frame,text="Confirm Password",font=("times new roman",15,"bold"),fg="red",bg="light green")
        confirm_pswd.place(x=370,y=310)
        self.txt_confirm_pswd=ttk.Entry(frame,textvariable=self.var_confpass,font=("times new roman",15,"bold"))
        self.txt_confirm_pswd.place(x=370,y=340,width=250)
        
        self.var_check=IntVar()
        checkbtn=Checkbutton(frame,variable=self.var_check,text="I Agree the Terms And Conditions",font=("times new roman",13,"bold"),onvalue=1,offvalue=0)
        checkbtn.place(x=50,y=390)
        
        img=Image.open(r"C:\Users\ASUS\Desktop\VS Code project\Login\Images\b.jpg")
        img=img.resize((190,60),Image.ANTIALIAS)
        self.photoimage=ImageTk.PhotoImage(img)
        b1=Button(frame,image=self.photoimage,command=self.register_data,borderwidth=0,cursor="hand2",font=("times new roman",13,"bold"))
        b1.place(x=70,y=430,width=190)
        
        img1=Image.open(r"C:\Users\ASUS\Desktop\VS Code project\Login\Images\l.jpg")
        img1=img1.resize((190,60),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        b1=Button(frame,image=self.photoimage1,command=self.return_login,borderwidth=0,cursor="hand2",font=("times new roman",13,"bold"))
        b1.place(x=390,y=430,width=190)
        
        
        
    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get=="Select":
            messagebox.showerror("Error","All Fields Are Required")
        elif self.var_pass.get()!=self.var_confpass.get():
            messagebox.showerror("Error","Password And Confirm Password Must Be Same")
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please Agree Our Terms And Conditions")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="Mohitsinha80@",database="mydata")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","User Allready Exist Please Try Some Another Email_Id")
            else:
                try:
                    
                    
                    
                    my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                        self.var_fname.get(),
                        self.var_lname.get(),
                        self.var_contact.get(),
                        self.var_email.get(),
                        self.var_securityQ.get(),
                        self.var_securityA.get(),
                        self.var_pass.get()
                        
                            ))
                    conn.commit()
                    conn.close()
                    messagebox.showinfo("Success","Registered Successfully")
                except Exception as es:
                    messagebox.showerror("Error", f"Due To:{str(es)}", parent=self.root)
    
     
    def return_login(self):
         self.root.destroy()
     
     
     
     
     
                
            

class student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x800+0+0")
        self.root.title("STUDENT MANAGMENT SYSTEM")

        # variables
        self.var_cou = StringVar()
        self.var_dep = StringVar()
        self.var_year = StringVar()
        self.var_sem = StringVar()
        self.var_stu_id = StringVar()
        self.var_univ_id = StringVar()
        self.var_name = StringVar()
        self.var_dob = StringVar()
        self.var_father = StringVar()
        self.var_mobile = StringVar()
        self.var_sess = StringVar()
        self.var_quota = StringVar()
        self.var_email = StringVar()
        self.var_address = StringVar()
        self.gender_var=StringVar()
        
        
        
        img = Image.open(r"C:\Users\ASUS\Desktop\VS Code project\Login\Student managment system -Mohit(2013187)\photos\akgec.png")
        img = img.resize((1525, 130), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        self.btn_1 = Button(self.root, image=self.photoimg)
        self.btn_1.place(x=0, y=0, width=1525, height=130)

        
        bg_lbl = Label(self.root, bd=2, relief=RIDGE,bg="yellow")
        bg_lbl.place(x=0, y=130, width=1525, height=700)

        lbl_title = Label(bg_lbl, text="STUDENT MANAGMENT SYSTEM", font=("times new roman", 32, "bold"), fg="black",
                          bg="yellow")
        lbl_title.place(x=0, y=0, width=1525, height=40)

        # manage frame
        Manage_frame = Frame(bg_lbl, bd=2, relief=RIDGE, bg="green")
        Manage_frame.place(x=15, y=50, width=1500, height=600)

        # left frame
        DataLeftFrame = LabelFrame(Manage_frame, bd=4, relief=RIDGE, padx=2, text="Student Information",
                                   font=("times new roman", 14, "bold"), fg="brown", bg="white")
        DataLeftFrame.place(x=20, y=10, width=650, height=580)

        # current course label frame
        std_lbl_info_frame = LabelFrame(DataLeftFrame, bd=4, relief=RIDGE, padx=2, text="Current Course Information",
                                        font=("times new roman", 13, "italic"), fg="red", bg="white")
        std_lbl_info_frame.place(x=10, y=5, width=625, height=155)

        # labels course
        lbl_cou = Label(std_lbl_info_frame, text="Course:", font=("times new roman", 15, "bold"), bg="white")
        lbl_cou.grid(row=0, column=0, padx=25, sticky=W)

        comb_cour = ttk.Combobox(std_lbl_info_frame, textvariable=self.var_cou, font=("times new roman", 12, "normal"),
                                 width=17, state="readonly")
        comb_cour["value"] = ("Select Course", "B.Tech", "BCA", "BBA", "MBA", "M.Tech")
        comb_cour.current(0)
        comb_cour.grid(row=0, column=1, padx=1, pady=20, sticky=W)

        # labels deparment
        lbl_dep = Label(std_lbl_info_frame, text="Deparment:", font=("times new roman", 15, "bold"), bg="white")
        lbl_dep.grid(row=0, column=2, padx=20, sticky=W)

        comb_dep = ttk.Combobox(std_lbl_info_frame, textvariable=self.var_dep, font=("times new roman", 12, "normal"),
                                width=17, state="readonly")
        comb_dep["value"] = ("Select Department", "CIVIL", "CSE", "IT", "ECE", "EN", "ME")
        comb_dep.current(0)
        comb_dep.grid(row=0, column=3, padx=1, pady=20, sticky=W)

        # labels Year
        lbl_yer = Label(std_lbl_info_frame, text="Year:", font=("Times new roman", 15, "bold"), bg="white")
        lbl_yer.grid(row=1, column=0, padx=25, sticky=W)

        comb_yer = ttk.Combobox(std_lbl_info_frame, textvariable=self.var_year, font=("times new roman", 12, "normal"),
                                width=17, state="readonly")
        comb_yer["value"] = ("Select Year", "First", "Second", "Third", "Fourth")
        comb_yer.current(0)
        comb_yer.grid(row=1, column=1, padx=1, pady=10, sticky=W)

        # labels Semester
        lbl_sem = Label(std_lbl_info_frame, text="Semester:", font=("Times new roman", 15, "bold"), bg="white")
        lbl_sem.grid(row=1, column=2, padx=20, sticky=W)

        comb_sem = ttk.Combobox(std_lbl_info_frame, textvariable=self.var_sem, font=("times new roman", 12, "normal"),
                                width=17, state="readonly")
        comb_sem["value"] = ("Select Semester", "I sem", "II sem")
        comb_sem.current(0)
        comb_sem.grid(row=1, column=3, padx=1, pady=10, sticky=W)

        # student class label frame
        std_lbl_class_frame = LabelFrame(DataLeftFrame, bd=4, relief=RIDGE, padx=2, text="Student Information",
                                         font=("times new roman", 12, "italic"), fg="red", bg="white")
        std_lbl_class_frame.place(x=10, y=168, width=625, height=328)

        # labels
        # Student id
        lbl_collid = Label(std_lbl_class_frame, text="Student Id:", font=("Times new roman", 14, "bold"), bg="white")
        lbl_collid.grid(row=0, column=0, padx=10,pady=10, sticky=W)

        id_entry = ttk.Entry(std_lbl_class_frame, textvariable=self.var_stu_id, font=("Times new roman", 12, "normal"),
                             width=17)
        id_entry.grid(row=0, column=1, sticky=W, padx=5,pady=10)

        # university roll
        lbl_uniid = Label(std_lbl_class_frame, text="University Roll No.:", font=("Times new roman", 14, "bold"), bg="white")
        lbl_uniid.grid(row=0, column=2, padx=10,pady=10, sticky=W)

        uni_roll = ttk.Entry(std_lbl_class_frame, textvariable=self.var_univ_id, font=("Times new roman", 12, "normal"),
                             width=15)
        uni_roll.grid(row=0, column=3, sticky=W, padx=0, pady=10)

        # Name
        lbl_name = Label(std_lbl_class_frame, text="Name:", font=("Times new roman", 14, "bold"), bg="white")
        lbl_name.grid(row=1, column=0, padx=10,pady=10, sticky=W)

        name_entry = ttk.Entry(std_lbl_class_frame, textvariable=self.var_name, font=("Times new roman", 12, "normal"),
                               width=17)
        name_entry.grid(row=1, column=1, sticky=W, padx=5, pady=10)

        # Date of birth
        lbl_dob = Label(std_lbl_class_frame, text="D.O.B:", font=("Times new roman", 14, "bold"), bg="white")
        lbl_dob.grid(row=1, column=2, padx=10,pady=10, sticky=W)

        dob_entry = ttk.Entry(std_lbl_class_frame, textvariable=self.var_dob, font=("Times new roman", 12, "normal"),
                              width=15)
        dob_entry.grid(row=1, column=3, sticky=W, padx=0, pady=10)
        
        
        
        
        gender=Label(std_lbl_class_frame,text="Gender:",font=('times new roman',14,'bold'),bg="white")
        gender.grid(row=2,column=0,padx=10,pady=8,sticky=W)

        
        male=Radiobutton(std_lbl_class_frame,variable=self.gender_var,text='Male',value='Male',font=('times new roman',14,'bold'),bg="white")
        male.grid(row=2,column=1,sticky=W)
        self.gender_var.set('Male')
        female=Radiobutton(std_lbl_class_frame,variable=self.gender_var,text='Female',value='Female',font=('times new roman',14,'bold'),bg="white")
        female.grid(row=2,column=2,padx=10,pady=8,sticky=W)


        # fathers name
        lbl_fatnm = Label(std_lbl_class_frame, text="Father Name:", font=("Times new roman", 14, "bold"), bg="white")
        lbl_fatnm.grid(row=3, column=0, padx=10,pady=10, sticky=W)

        fatnm_entry = ttk.Entry(std_lbl_class_frame, textvariable=self.var_father,
                                font=("Times new roman", 12, "normal"), width=17)
        fatnm_entry.grid(row=3, column=1, sticky=W, padx=10, pady=10)

        # mobile no
        lbl_mobno = Label(std_lbl_class_frame, text="Mobile No.:", font=("Times new roman", 14, "bold"), bg="white")
        lbl_mobno.grid(row=3, column=2, padx=10,pady=10, sticky=W)

        mobno_en = ttk.Entry(std_lbl_class_frame, textvariable=self.var_mobile, font=("Times new roman", 12, "normal"),
                             width=15)
        mobno_en.grid(row=3, column=3, sticky=W, padx=0, pady=10)

        # session yr
        lbl_sesyr = Label(std_lbl_class_frame, text="Session yr:", font=("Times new roman", 14, "bold"), bg="white")
        lbl_sesyr.grid(row=4, column=0, padx=10,pady=10, sticky=W)

        ses_entry = ttk.Entry(std_lbl_class_frame, textvariable=self.var_sess, font=("Times new roman", 12, "normal"),
                              width=17)
        ses_entry.grid(row=4, column=1, sticky=W, padx=10, pady=10)

        # Quota
        lbl_quota = Label(std_lbl_class_frame, text="Quota:", font=("Times new roman", 14, "bold"), bg="white")
        lbl_quota.grid(row=4, column=2, padx=10,pady=10, sticky=W)

        comb_quota = ttk.Combobox(std_lbl_class_frame, textvariable=self.var_quota,
                                  font=("Times new roman", 12, "normal"), width=13, state="readonly")
        comb_quota["value"] = ("Select Quota", "General", "OBC", "SC", "ST")
        comb_quota.current(0)
        comb_quota.grid(row=4, column=3, padx=0, pady=10, sticky=W)

        # Email id
        lbl_email = Label(std_lbl_class_frame, text="Email Id:", font=("Times new roman", 14, "bold"), bg="white")
        lbl_email.grid(row=5, column=0, padx=10,pady=10, sticky=W)

        email_entry = ttk.Entry(std_lbl_class_frame, textvariable=self.var_email,
                                font=("Times new roman", 12, "normal"), width=17)
        email_entry.grid(row=5, column=1, sticky=W, padx=10, pady=10)

        # Address
        lbl_addr = Label(std_lbl_class_frame, text="Address:", font=("Times new roman", 14, "bold"), bg="white")
        lbl_addr.grid(row=5, column=2, padx=10,pady=10, sticky=W)

        add_entry = ttk.Entry(std_lbl_class_frame, textvariable=self.var_address,
                              font=("Times new roman", 12, "normal"), width=15)
        add_entry.grid(row=5, column=3, sticky=W, padx=0, pady=10)

        # button frame
        btn_frame = Frame(DataLeftFrame, bd=4, relief=RIDGE, bg="white")
        btn_frame.place(x=10, y=500, width=625, height=40)

        btn_add = Button(btn_frame, text="Save", command=self.add_data, font=("Cooper Black", 12,), width=13, bg="blue",
                         fg="white", borderwidth=0)
        btn_add.grid(row=0, column=1, padx=3, pady=2)

        btn_update = Button(btn_frame, text="Update",command=self.update_data, font=("Cooper Black", 12,), width=13, bg="blue", fg="white",
                            borderwidth=0)
        btn_update.grid(row=0, column=2, padx=4, pady=2)

        btn_Remove = Button(btn_frame, text="Delete",command=self.delete_data, font=("Cooper Black", 12,), width=13, bg="blue", fg="white",
                            borderwidth=0)
        btn_Remove.grid(row=0, column=3, padx=4, pady=2)

        btn_reset = Button(btn_frame, text="Reset",command=self.reset_data, font=("Cooper Black", 12,), width=12, bg="blue", fg="white",
                           borderwidth=0)
        btn_reset.grid(row=0, column=4, padx=4, pady=2)

        # right frame
        DataRightFrame = LabelFrame(Manage_frame, bd=4, relief=RIDGE, padx=2, text="Student Database",
                                    font=("times new roman", 14, "bold"), fg="brown", bg="white")
        DataRightFrame.place(x=670, y=10, width=810, height=580)

        # image
        img_right = Image.open(r"C:\Users\ASUS\Desktop\VS Code project\Login\Student managment system -Mohit(2013187)\photos\akkm5.png")
        img_right.resize((785, 150), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img_right)

        my_img = Label(DataRightFrame, image=self.photoimg3, bd=3, relief=RIDGE)
        my_img.place(x=2, y=3, width=785, height=200)

        # search
        searchFrame = LabelFrame(DataRightFrame, bd=4, relief=RIDGE, padx=2, text="Search Student Information",
                                 font=("times new roman", 12, "bold"), fg="brown", bg="white")
        searchFrame.place(x=0, y=195, width=785, height=65)
        
        
        Seach_by = Label(searchFrame, font=("arial", 12, "bold"), text="Search By:", bg="red", fg="white")
        Seach_by.grid(row=0, column=0, sticky=W, padx=5)
        
        
        
        self.var_com_search=StringVar()
        search_by = ttk.Combobox(searchFrame,textvariable=self.var_com_search, font=("Times new roman", 12, "normal"), width=13, state="readonly")
        search_by["value"] = ("Select Option", "Student_Id", "University_Id", "Mobile_no")
        search_by.current(0)
        search_by.grid(row=0, column=1, padx=5, sticky=W)
        self.var_search=StringVar()
        txt_search = ttk.Entry(searchFrame,textvariable=self.var_search, font=("Times new roman", 12, "normal"), width=20)
        txt_search.grid(row=0, column=2, sticky=W, padx=5, pady=10)

        btn_Search = Button(searchFrame,command=self.search_data, text="Search", font=("Cooper Black", 12,), width=15, bg="blue", fg="white",
                            borderwidth=0)
        btn_Search.grid(row=0, column=3, padx=5)

        btn_ShowAll = Button(searchFrame,command=self.fetch_data, text="Show All", font=("Cooper Black", 12), width=15, bg="blue", fg="white",
                             borderwidth=0)
        btn_ShowAll.grid(row=0, column=4, padx=5)

        # ***********************Student Table and scroll bar ****************************
        table_frame = Frame(DataRightFrame, bd=4, relief=RIDGE, bg="white")
        table_frame.place(x=0, y=260, width=785, height=290)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)
        self.student_table = ttk.Treeview(table_frame, columns=(
        "Course", "Dep","Year" ,"Sem", "Stud_id", "Univ_id", "Name", "DoB","Gender", "Father", "Mobile", "Ses" ,"Quota",
        "Email", "Address"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("Course", text="Course")
        self.student_table.heading("Dep", text="Deparment")
        self.student_table.heading("Year", text="Year")
        
        self.student_table.heading("Sem", text="Semester")
        self.student_table.heading("Stud_id", text="Student_Id")
        self.student_table.heading("Univ_id", text="University_Id")
        
        
        self.student_table.heading("Name", text="Name")
        self.student_table.heading("DoB", text="D.O.B")
        self.student_table.heading("Gender", text="Gender")
        self.student_table.heading("Father", text="Father_Nm")
        self.student_table.heading("Mobile", text="Mobile_No.")
        self.student_table.heading("Ses", text="Session yr")
        self.student_table.heading("Quota", text="Quota")
        self.student_table.heading("Email", text="Email_Id")
        self.student_table.heading("Address", text="Address")

        self.student_table["show"] = "headings"

        self.student_table.column("Course", width=100)
        self.student_table.column("Dep", width=100)
        self.student_table.column("Year", width=100)
        self.student_table.column("Sem", width=100)
        self.student_table.column("Stud_id", width=100)
        self.student_table.column("Univ_id", width=100)
        
        
        self.student_table.column("Name", width=100)
        self.student_table.column("DoB", width=100)
        self.student_table.column("Gender", width=100)
        self.student_table.column("Father", width=100)
        self.student_table.column("Mobile", width=100)
        self.student_table.column("Ses", width=100)
        self.student_table.column("Quota", width=100)
        self.student_table.column("Email", width=100)
        self.student_table.column("Address", width=150)

        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
        

    def add_data(self):
        if (self.var_cou.get() == "" or self.var_dep.get() == "" or self.var_name.get() == ""):
            messagebox.showerror("Error", "All Fields Are required")
        else:
            try:
                conn = mysql.connector.connect(host="localhost", user="root", password="Mohitsinha80@",
                                               database="student")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
                    self.var_cou.get(),
                    self.var_dep.get(),
                    self.var_year.get(),
                    self.var_sem.get(),
                    self.var_stu_id.get(),
                    self.var_univ_id.get(),
                    self.var_name.get(),
                    self.var_dob.get(),
                    self.gender_var.get(),
                    self.var_father.get(),
                    self.var_mobile.get(),
                    self.var_sess.get(),
                    self.var_quota.get(),
                    self.var_email.get(),
                    self.var_address.get()
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Student has been added!", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due To:{str(es)}", parent=self.root)
    
    
    #fetch Function
    def fetch_data(self):
        
        conn = mysql.connector.connect(host="localhost", user="root", password="Mohitsinha80@",
                                               database="student")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()
        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
                conn.commit()
        conn.close()
            
                
    #Get Cursor
    def get_cursor(self,event=""):
        cursor_row=self.student_table.focus()
        content=self.student_table.item(cursor_row)
        data=content["values"]
        self.var_cou.set(data[0])
        self.var_dep.set(data[1])
        self.var_year.set(data[2])
        self.var_sem.set(data[3])
        self.var_stu_id.set(data[4])
        self.var_univ_id.set(data[5])
        self.var_name.set(data[6])
        self.var_dob.set(data[7])
        self.gender_var.set(data[8])
        self.var_father.set(data[9])
        self.var_mobile.set(data[10])
        self.var_sess.set(data[11])
        self.var_quota.set(data[12])
        self.var_email.set(data[13])
        self.var_address.set(data[14])

    # update
    def update_data(self):
        if(self.var_dep.get()=="" or self.var_email.get=="" or self.var_stu_id.get()==""):
            messagebox.showerror("Error","All Fields Are Required",parent=self.root)
        else:
            try:
                update=messagebox.askyesno("Update","Aye You Sure To Update Student Data",parent=self.root)
                if update>0:
                    conn = mysql.connector.connect(host="localhost", user="root", password="Mohitsinha80@",
                                               database="student")
                    my_cursor = conn.cursor()
                    my_cursor.execute("update student set coarse=%s,dep=%s,year=%s,semester=%s,university_id=%s,name=%s,dob=%s,Gender=%s,father=%s,mobile_no=%s,session=%s,quota=%s,email=%s,address=%s where student_id=%s",(
                                                                                                                                                                                            self.var_cou.get(),
                                                                                                                                                                                            self.var_dep.get(),
                                                                                                                                                                                            self.var_year.get(),
                                                                                                                                                                                            self.var_sem.get(),
                                                                                                                                                                                            
                                                                                                                                                                                            self.var_univ_id.get(),
                                                                                                                                                                                            self.var_name.get(),
                                                                                                                                                                                            self.var_dob.get(),
                                                                                                                                                                                            self.gender_var.get(),
                                                                                                                                                                                            self.var_father.get(),
                                                                                                                                                                                            self.var_mobile.get(),
                                                                                                                                                                                            self.var_sess.get(),
                                                                                                                                                                                            self.var_quota.get(),
                                                                                                                                                                                            self.var_email.get(),
                                                                                                                                                                                            self.var_address.get(),
                                                                                                                                                                                            self.var_stu_id.get()
                                                                                                                                                                                            ))
                else:
                    if not update:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Sdudent Data Successfully Updated",parent=self.root)      
            except Exception as es:
                messagebox.showerror("Error", f"Due To:{str(es)}", parent=self.root)
                
                
                
    # Delete
    def delete_data(self):
        if self.var_stu_id.get=="":
            messagebox.showerror("Error","All Fields Are Required",parent=self.root)
        else:
            try:
                Delete=messagebox.askyesno("Delete","Are You Sure You Want To Delete Data",parent=self.root)
                if Delete>0:
                    conn = mysql.connector.connect(host="localhost", user="root", password="Mohitsinha80@",
                                                   database="student")
                    my_cursor = conn.cursor()
                    sql="delete from student where student_id=%s"
                    value=(self.var_stu_id.get(),)
                    my_cursor.execute(sql,value)
                else:
                    if not Delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Student Data Has Been Deleted Successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due To:{str(es)}", parent=self.root)
            
            
    # Reset
    def reset_data(self):
        self.var_cou.set("Select Course")
        self.var_dep.set("Select Department")
        self.var_year.set("Select Year")
        self.var_sem.set("Select Semester")
        self.var_stu_id.set("")
        self.var_univ_id.set("")
        self.var_name.set("")
        self.var_dob.set("")
        self.gender_var.set("")
        self.var_father.set("")
        self.var_mobile.set("")
        self.var_sess.set("")
        self.var_quota.set("Select Quota")
        self.var_email.set("")
        self.var_address.set("")

               
    # Search Data 
    def search_data(self):
        if self.var_com_search.get()=="" or self.var_search.get=="":
            messagebox.showerror("Error","Please Select Option", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", user="root", password="Mohitsinha80@",
                                                   database="student")
                my_cursor = conn.cursor()
                my_cursor.execute("select * from student where "+str(self.var_com_search.get())+" LIKE '%"+str(self.var_search.get())+"%'")
                rows=my_cursor.fetchall()
                if len(rows)!=0:
                    self.student_table.delete(*self.student_table.get_children())
                    for i in rows:
                        self.student_table.insert("",END,values=i)
                conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error", f"Due To:{str(es)}", parent=self.root)
               
                
      

       
        
        
        
                
        
        
        
        
        
        
        
if __name__=="__main__":
    main()
