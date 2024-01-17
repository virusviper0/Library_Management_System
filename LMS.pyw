from datetime import datetime , timedelta
from sqlite3 import Cursor
from tkinter import *
from tkinter import filedialog
import mysql.connector
from tkinter.ttk import Combobox, Treeview
import tkinter.messagebox as msg
class library_man():
    def __init__(self,root):

        ################### Library Management System ##################### 
        self.root=root
        self.root.title("LIBRARY MANAGEMENT SYSTEM")
        self.root.geometry("1000x1000")
        self.root.minsize(1000,1000)
        self.root.maxsize(1000,1000)
        self.root.wm_iconbitmap('icon.ico')
        # datetime.now().strftime("%d/%m/%y")
        
        ######################## Variable Data ###############3
        self.member_var=StringVar()
        self.prn_var=StringVar()
        self.MemberID_var=StringVar()
        self.First_Name_var=StringVar()
        self.Surname_var=StringVar()
        self.Course_var=StringVar()
        self.PhoneNumber_var=StringVar()
        self.Address_var=StringVar()
        self.Bookid_var=StringVar()
        self.BookName_var=StringVar()
        self.AuthorName_var=StringVar()
        self.Current_date_var=StringVar()
        self.IssueDate_var=StringVar()
        self.Due_Date_var=StringVar()
        self.FneOnDue_var=StringVar()
        self.BookPrice_var=StringVar()
        # self.PhoneNumber_var.set("")
        # self.Course_var.set("Bsc")

        self.member_var.set("Student")
        self.Current_date_var.set(datetime.now().strftime("%d %B"))
        due=self.IssueDate_var.set(datetime.now().strftime("%d %B"))
        self.Due_Date_var.set((datetime.now()+timedelta(days=14)).strftime("%d %B"))

        #############################################################################
        issue_time=datetime.strptime(self.IssueDate_var.get(),"%d %B")
        Due_time=datetime.strptime(self.Due_Date_var.get(),"%d %B")
        gape=Due_time-issue_time
        if int(gape.days)>15:
            self.FneOnDue_var.set(gape.days)
        print(gape.days)
        print(type(gape))
############################################################################################   

        ######################## Top label #################
        titlelabel=Label(self.root,text="LIBRARY MANAGEMENT SYSTEM",bg="BLUE",fg="WHITE",bd=10,relief="ridge",font=("times",23,"bold"),padx=3,pady=5)
        titlelabel.pack(side=TOP,fill=X)

        ######################## Frame of Data Input ###########
        frame=Frame(self.root,bd=9,relief="ridge",padx=3,pady=3,bg="GREEN")
        frame.place(x=0,y=65,width=1000,height=400)

        ########################### data frame left #############3
        InputFrameLeft=LabelFrame(frame,text="LIBRARY MEMBER INFO",bg="BLUE",fg="WHITE",bd=9,relief="ridge",font=("times",13,"bold"),padx=0,pady=5)
        InputFrameLeft.place(x=0,y=0,width=500,height=377)

                    #### Label  #3
        Membertype=Label(InputFrameLeft,bg="BLUE",text="Member Info",font=("reguler",11,"bold"),padx=2,pady=8)
        PRN=Label(InputFrameLeft,bg="BLUE",text="PRN",font=("reguler",11,"bold"),padx=2,pady=8)
        MemberID=Label(InputFrameLeft,bg="BLUE",text="ID",font=("reguler",11,"bold"),padx=2,pady=8)        
        First_NameOfMember=Label(InputFrameLeft,bg="BLUE",text="Name",font=("reguler",11,"bold"),padx=2,pady=8)
        SurnameOfMember=Label(InputFrameLeft,text="SurName",font=("reguler",11,"bold"),bg="BLUE",padx=2,pady=8)
        PhoneNumber=Label(InputFrameLeft,bg="BLUE",text="Phone Number",font=("reguler",11,"bold"),padx=2,pady=8)
        Address=Label(InputFrameLeft,bg="BLUE",text="Address",font=("reguler",11,"bold"),padx=2,pady=8)
        Course=Label(InputFrameLeft,bg="BLUE",text="Course",font=("reguler",11,"bold"),padx=2,pady=8)        


        Membertype.grid(row=0,column=0,sticky=W)
        PRN.grid(row=1,column=0,sticky=W)
        MemberID.grid(row=2,column=0,sticky=W)
        First_NameOfMember.grid(row=3,column=0,sticky=W)
        SurnameOfMember.grid(row=4,column=0,sticky=W)
        Course.grid(row=5,column=0,sticky=W)
        PhoneNumber.grid(row=6,column=0,sticky=W)
        Address.grid(row=7,column=0,sticky=W)

                #########  Entry #######3
        Membertypecombo=Combobox(InputFrameLeft,textvariable=self.member_var,font=("regular",10,"bold"),width=15,value=("Student","Teacher"))
        PRNentry=Entry(InputFrameLeft,textvariable=self.prn_var,font=("reguler",10,"bold"),width=17)
        MemberIDentry=Entry(InputFrameLeft,textvariable=self.MemberID_var,font=("reguler",10,"bold"),width=17)
        First_Nameentry=Entry(InputFrameLeft,textvariable=self.First_Name_var,font=("reguler",10,"bold"),width=17)
        Surnameentry=Entry(InputFrameLeft,textvariable=self.Surname_var,font=("reguler",10,"bold"),width=17)
        Courseentry=Combobox(InputFrameLeft,textvariable=self.Course_var,font=("regular",10,"bold"),width=15,value=("B.Sc","B.Com","B.A","PGDCA","M.Com","M.A"))
        PhoneNumberentry=Entry(InputFrameLeft,textvariable=self.PhoneNumber_var,font=("reguler",10,"bold"),width=17)
        Addressentry=Entry(InputFrameLeft,textvariable=self.Address_var,font=("reguler",10,"bold"),width=17)
        
        Membertypecombo.grid(row=0,column=1)
        PRNentry.grid(row=1,column=1)
        MemberIDentry.grid(row=2,column=1)
        First_Nameentry.grid(row=3,column=1)
        Surnameentry.grid(row=4,column=1)
        Courseentry.grid(row=5,column=1)
        PhoneNumberentry.grid(row=6,column=1)
        Addressentry.grid(row=7,column=1)

                        #######3 Book Label #$$#######
        Bookid=Label(InputFrameLeft,text="Book Id",font=("reguler",11,"bold"),bg="BLUE",padx=2,pady=8)
        BookName=Label(InputFrameLeft,text="Book Name",font=("reguler",11,"bold"),bg="BLUE",padx=2,pady=8)
        AuthorName=Label(InputFrameLeft,text="Author Name",font=("reguler",11,"bold"),bg="BLUE",padx=2,pady=8)
        Current_date=Label(InputFrameLeft,text="Today Date",font=("reguler",11,"bold"),bg="BLUE",padx=2,pady=8)
        IssueDate=Label(InputFrameLeft,text="Issue Date",font=("reguler",11,"bold"),bg="BLUE",padx=2,pady=8)
        Due_Date=Label(InputFrameLeft,text="Due Date",font=("reguler",11,"bold"),bg="BLUE",padx=2,pady=8)
        FineOnDue=Label(InputFrameLeft,text="Fine",font=("reguler",11,"bold"),bg="BLUE",padx=2,pady=8)
        BookPrice=Label(InputFrameLeft,text="Book Price",font=("reguler",11,"bold"),bg="BLUE",padx=2,pady=8)

        Bookid.grid(row=0,column=2,sticky=W)
        BookName.grid(row=1,column=2,sticky=W)
        AuthorName.grid(row=2,column=2,sticky=W)
        Current_date.grid(row=3,column=2,sticky=W)
        IssueDate.grid(row=4,column=2,sticky=W)
        Due_Date.grid(row=5,column=2,sticky=W)
        FineOnDue.grid(row=6,column=2,sticky=W)
        BookPrice.grid(row=7,column=2,sticky=W)

                        ############ Book Entry ##########333
        Bookid_entry=Entry(InputFrameLeft,textvariable=self.Bookid_var,font=("reguler",10,"bold"),width=17)
        BookName_entry=Entry(InputFrameLeft,textvariable=self.BookName_var,font=("reguler",10,"bold"),width=17)
        AuthorName_entry=Entry(InputFrameLeft,textvariable=self.AuthorName_var,font=("reguler",10,"bold"),width=17)
        Current_date_Entry=Entry(InputFrameLeft,textvariable=self.Current_date_var,font=("reguler",10,"bold"),width=17)
        IssueDate_entry=Entry(InputFrameLeft,textvariable=self.IssueDate_var,font=("reguler",10,"bold"),width=17)
        Due_Date_Entry=Entry(InputFrameLeft,textvariable=self.Due_Date_var,font=("reguler",10,"bold"),width=17)
        FneOnDue_Entry=Entry(InputFrameLeft,textvariable=self.FneOnDue_var,font=("reguler",10,"bold"),width=17)
        BookPrice_entry=Entry(InputFrameLeft,textvariable=self.BookPrice_var,font=("reguler",10,"bold"),width=17)

        Bookid_entry.grid(row=0,column=3)
        BookName_entry.grid(row=1,column=3)
        AuthorName_entry.grid(row=2,column=3)
        Current_date_Entry.grid(row=3,column=3)
        IssueDate_entry.grid(row=4,column=3)
        Due_Date_Entry.grid(row=5,column=3)
        FneOnDue_Entry.grid(row=6,column=3)
        BookPrice_entry.grid(row=7,column=3)

        ####################### data frame right ###################3333
        DataFrameRight=LabelFrame(frame,text="BOOK DETAIL",bg="BLUE",fg="WHITE",bd=9,relief="ridge",font=("times",13,"bold"),padx=3,pady=5)
        DataFrameRight.place(x=505,y=0,width=470,height=377)

        self.TxtBox=Text(DataFrameRight,font=("regulr",10,"bold"),width=38,height=19,padx=3,pady=4)
        listscroll=Scrollbar(DataFrameRight,)
        ListBoxBook=Listbox(DataFrameRight,font=("regulr",10,"bold"),width=21,height=18)

        self.TxtBox.grid(row=0,column=2)
        listscroll.grid(row=0,column=1,sticky="ns")
        ListBoxBook.grid(row=0,column=0,padx=2)

        listscroll.config(command=ListBoxBook.yview)

        Book=self.LibraryBookList()
        for item in Book:
            ListBoxBook.insert(END,item)
        
        AddBook=Button(DataFrameRight,command=self.AddBookInLibrary,text="Add Book",font=("times",10,"bold"),width=20,bg="Blue",fg="WHITE")
        AddBook.grid(column=0,row=1)

        PrintButton=Button(DataFrameRight,text="Print",command=self.printData,bg="Blue",fg="WHITE",font=("times",10,"bold"),width=20)
        PrintButton.grid(row=1,column=2)

        ############## Frame for button ###############3
        framebutton=Frame(self.root,bd=9,relief="ridge",padx=1,pady=7,bg="GREEN")
        framebutton.place(x=0,y=465,width=1000,height=70)

        #############3 Button selcttion ###################
        AddButton=Button(framebutton,command=self.AddData,text="Add Data",font=("times",11,"bold"),width=17,padx=0,relief="raised",pady=3,bg="BLUE",fg="WHITE")
        ResetButton=Button(framebutton,command=self.reset,text="Reset",font=("times",11,"bold"),width=17,bg="BLUE",padx=0,relief="raised",pady=3,fg="WHITE")
        DeleteButton=Button(framebutton,command=self.delete,text="Delete",font=("times",11,"bold"),width=17,bg="BLUE",padx=0,relief="raised",pady=3,fg="WHITE")
        UpdateButton=Button(framebutton,command=self.update,text="Update",font=("times",11,"bold"),width=17,bg="BLUE",padx=0,relief="raised",pady=3,fg="WHITE")
        ExitButton=Button(framebutton,command=self.LmsExit,text="Exit",font=("times",11,"bold"),width=17,bg="BLUE",padx=0,relief="raised",pady=3,fg="WHITE")
        ShowButton=Button(framebutton,command=self.show_data,text="Show",font=("times",11,"bold"),width=17,bg="BLUE",padx=0,relief="raised",pady=3,fg="WHITE")

        AddButton.grid(row=0,column=0,padx=1)
        ResetButton.grid(row=0,column=1,padx=1)
        DeleteButton.grid(row=0,column=2,padx=1)
        UpdateButton.grid(row=0,column=3,padx=1)
        ExitButton.grid(row=0,column=5,padx=1)
        ShowButton.grid(row=0,column=4,padx=1)
        
        #################### Frame for data base info #################
        DataBaseInfo=Frame(self.root,bd=9,relief="ridge",padx=2,bg="GREEN")
        DataBaseInfo.place(x=0,y=535,width=1000,height=130)
        
        tableframe=Frame(DataBaseInfo,bd=6,relief="raised",bg="BLUE")
        tableframe.place(x=0,y=1,width=979,height=107)

        xscrollbar_heading=Scrollbar(tableframe,orient="horizontal")
        yscrollbar_heading=Scrollbar(tableframe,orient="vertical")

        xscrollbar_heading.pack(side=BOTTOM,fill=X)
        yscrollbar_heading.pack(side=RIGHT,fill=Y)

        self.library_table=Treeview(tableframe,column=("Member Type","Prn","ID","Name","Surname","Course","Phone Number","Address","Book id","Book Name","Author Name","Issue","Due","Fine","Book Price"),xscrollcommand=xscrollbar_heading.set,yscrollcommand=yscrollbar_heading.set)

        xscrollbar_heading.config(command=self.library_table.xview)
        yscrollbar_heading.config(command=self.library_table.yview)

        ############### to Show ON DATABASE ON TKINTER ###############
        self.library_table.heading("Member Type",text="MEMBER TYPE"),       
        self.library_table.heading("Prn",text="PRN")        
        self.library_table.heading("ID",text="ID")       
        self.library_table.heading("Name",text="NAME") 
        self.library_table.heading("Surname",text="SURNAME")       
        self.library_table.heading("Course",text="COURSE")       
        self.library_table.heading("Phone Number",text="PHONE NUMBER")        
        self.library_table.heading("Address",text="ADDRESS")        
        self.library_table.heading("Book id",text="BOOK ID")        
        self.library_table.heading("Book Name",text="BOOK NAME")        
        self.library_table.heading("Author Name",text="AUTHOR NAME")
        # self.library_table.heading("Today",text="TODAY")        
        self.library_table.heading("Issue",text="ISSUE")        
        self.library_table.heading("Due",text="DUE")        
        self.library_table.heading("Fine",text="FINE")        
        self.library_table.heading("Book Price",text="BOOK PRICE")        

        self.library_table["show"]="headings"
        self.library_table.pack(fill=BOTH,expand=1)

        ###########################width to column to show data ############
        self.library_table.column("Member Type",width=100), 
        self.library_table.column("Prn",width=100), 
        self.library_table.column("ID",width=100),
        self.library_table.column("Name",width=100),
        self.library_table.column("Surname",width=100), 
        self.library_table.column("Course",width=100), 
        self.library_table.column("Phone Number",width=100), 
        self.library_table.column("Address",width=100),
        self.library_table.column("Book id",width=100),
        self.library_table.column("Book Name",width=100),
        self.library_table.column("Author Name",width=100),
        # self.library_table.column("Today",width=100),
        self.library_table.column("Issue",width=100),
        self.library_table.column("Due",width=100),
        self.library_table.column("Fine",width=100),
        self.library_table.column("Book Price",width=100),


        def SelectBook(event):
            value=ListBoxBook.get(ListBoxBook.curselection())
            ConnectionDatabase=mysql.connector.connect(host="localhost",username="root",password="eninja-library",database="lms")
            my_cursor=ConnectionDatabase.cursor()
            my_cursor.execute("select * from Book_Data where Book_Id=%s",(value[0],))
            Book=my_cursor.fetchall()
            self.Bookid_var.set(Book[0][0])
            self.BookName_var.set(Book[0][1])
            self.AuthorName_var.set(Book[0][2])
            self.BookPrice_var.set(Book[0][3])
            ConnectionDatabase.commit()
            ConnectionDatabase.close()

        def BookScanBarcode(event):
            value=self.Bookid_var.get()
            ConnectionDatabase=mysql.connector.connect(host="localhost",username="root",password="eninja-library",database="lms")
            my_cursor=ConnectionDatabase.cursor()
            my_cursor.execute("select * from Book_Data where Book_Id=%s",(value,))
            Book=my_cursor.fetchall()
            ConnectionDatabase.commit()
            ConnectionDatabase.close()
            if value != Book[0][0]:
                msg.showerror("ERROR","BOOK IS NOT PRESENT IN DATA BASE")
            else:
                self.Bookid_var.set(Book[0][0])
                self.BookName_var.set(Book[0][1])
                self.AuthorName_var.set(Book[0][2])
                self.BookPrice_var.set(Book[0][3])

        self.root.bind('<Return>',BookScanBarcode)
        self.library_table.bind("<ButtonRelease-1>",self.get_cursor)
        ListBoxBook.bind('<<ListboxSelect>>',SelectBook)
        self.fetch_data()

    def printData(self):
        open_file=filedialog.asksaveasfile(mode="w",defaultextension=".txt")
        text=str(self.TxtBox.get(1.0,END))
        open_file.write(text)
        open_file.close()

    def AddBookInLibrary(self):
        # import AddBookTemp 
        pass

    def LibraryBookList(self):
        ConnectionDatabase=mysql.connector.connect(host="localhost",username="root",password="eninja-library",database="lms")
        my_cursor=ConnectionDatabase.cursor()
        my_cursor.execute("select Book_Id,Book_Name from Book_Data")
        row=my_cursor.fetchall()
        ConnectionDatabase.commit()
        ConnectionDatabase.close()
        return row

    def AddData(self):
        ConnectionDatabase=mysql.connector.connect(host="localhost",username="root",password="eninja-library",database="lms")
        my_cursor=ConnectionDatabase.cursor()
        if self.MemberID_var.get()!="" and self.Bookid_var.get()!="":
            my_cursor.execute("select * from Issue_Book where Book_Id=%s",(self.Bookid_var.get(),))
            FindResult=my_cursor.fetchall()
            if FindResult == []:
                        my_cursor.execute("insert into Issue_Book values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                        (self.member_var.get(),
                        self.prn_var.get(),
                        self.MemberID_var.get(),
                        self.First_Name_var.get(),
                        self.Surname_var.get(),
                        self.Course_var.get(),
                        self.PhoneNumber_var.get(),
                        self.Address_var.get(),
                        self.Bookid_var.get(),
                        self.BookName_var.get(),
                        self.AuthorName_var.get(),
                        self.Current_date_var.get(),
                        self.Due_Date_var.get(),
                        self.FneOnDue_var.get(),
                        self.BookPrice_var.get()
                        ))
                        msg.showinfo("SUCCESS","DATA ADDED")
            else:
                msg.showerror("ERROR","Book Id is Not Present")   
    
            ConnectionDatabase.commit()
            ConnectionDatabase.close()
            self.fetch_data()
        else:
            msg.showerror("ERROR","Please Enter Data")

    def fetch_data(self):
        ConnectionDatabase=mysql.connector.connect(host="localhost",username="root",password="eninja-library",database="lms")
        my_cursor=ConnectionDatabase.cursor()
        my_cursor.execute("select * from Issue_Book")
        row=my_cursor.fetchall()
        if len(row)!=0:
            self.library_table.delete(*self.library_table.get_children())
            for i in row:
                self.library_table.insert("",END,values=i)
            ConnectionDatabase.commit()
        ConnectionDatabase.close()

    def get_cursor(self,event=""):
        cursor_row=self.library_table.focus()
        content=self.library_table.item(cursor_row)
        row=content['values']
        self.member_var.set(row[0])
        self.prn_var.set(row[1])
        self.MemberID_var.set(row[2])
        self.First_Name_var.set(row[3])
        self.Surname_var.set(row[4])
        self.Course_var.set(row[5])
        self.PhoneNumber_var.set(row[6])
        self.Address_var.set(row[7])
        self.Bookid_var.set(row[8])
        self.BookName_var.set(row[9])
        self.AuthorName_var.set(row[10])
        self.IssueDate_var.set(row[11])
        self.Due_Date_var.set(row[12])
        self.FneOnDue_var.set(row[13])
        self.BookPrice_var.set(row[14])

    def show_data(self):
        if (self.MemberID_var.get()=="" or self.Bookid_var.get()==""):
            msg.showerror("ERROR","Please Select A Member")
        else:
            self.TxtBox.delete("1.0","end")
            self.TxtBox.insert(END,"\t   LIBRARY INFO.\n")
            self.TxtBox.insert(END,"Member Type\t\t"+self.member_var.get()+"\n")
            self.TxtBox.insert(END,"PRN No.\t\t"+self.prn_var.get()+"\n")
            self.TxtBox.insert(END,"ID\t\t"+self.MemberID_var.get()+"\n")
            self.TxtBox.insert(END,"First Name\t\t"+self.First_Name_var.get()+"\n")
            self.TxtBox.insert(END,"Last Name\t\t"+self.Surname_var.get()+"\n")
            self.TxtBox.insert(END,"Course\t\t"+self.Course_var.get()+"\n")
            self.TxtBox.insert(END,"Phone Number\t\t"+self.PhoneNumber_var.get()+"\n")
            self.TxtBox.insert(END,"Address\t\t"+self.Address_var.get()+"\n")
            self.TxtBox.insert(END,"Book Id\t\t"+self.Bookid_var.get()+"\n")
            self.TxtBox.insert(END,"Book\t\t"+self.BookName_var.get()+"\n")
            self.TxtBox.insert(END,"Author\t\t"+self.AuthorName_var.get()+"\n")
            self.TxtBox.insert(END,"Issue On:\t\t"+self.IssueDate_var.get()+"\n")
            self.TxtBox.insert(END,"Due On:\t\t"+self.Due_Date_var.get()+"\n")
            self.TxtBox.insert(END,"Fine On Due:\t\t"+self.FneOnDue_var.get()+"\n")

    def reset(self):
        reset=msg.askyesno("RESET","Are You Sure ?")
        if reset == True:
            self.member_var.set("")
            self.prn_var.set("")
            self.MemberID_var.set("")
            self.First_Name_var.set("")
            self.Surname_var.set("")
            self.Course_var.set("")
            self.PhoneNumber_var.set("")
            self.Address_var.set("")
            self.Bookid_var.set("")
            self.BookName_var.set("")
            self.AuthorName_var.set("")
            # self.IssueDate_var.set("")
            # self.Due_Date_var.set("")
            self.FneOnDue_var.set("")
            self.BookPrice_var.set("")

    def LmsExit(self):
        iexit=msg.askyesno("LMS","Do you want to exit")
        if iexit == True:
            exit()
        else:
            pass

    def update(self):
        if self.MemberID_var.get()=="" or self.Bookid_var.get()=="":
            msg.showerror("ERROR","Please Enter Student Id")
        else:
            ConnectionDatabase=mysql.connector.connect(host="localhost",username="root",password="eninja-library",database="lms")
            my_cursor=ConnectionDatabase.cursor()
            
            my_cursor.execute("update Issue_Book set Prn=%s",self.prn_var.get())
            ConnectionDatabase.commit()
            self.fetch_data()
            self.reset()
            ConnectionDatabase.close()
            msg.showinfo("Success","Updated")
        
    def delete(self):
        if self.MemberID_var.get()=="" or self.Bookid_var.get()=="":
            msg.showerror("ERROE","Select the member")
        else:
            ConnectionDatabase=mysql.connector.connect(host="localhost",username="root",password="eninja-library",database="lms")
            my_cursor=ConnectionDatabase.cursor()
            my_cursor.execute("Select * from Issue_Book where ID=%s and Book_Id=%s",(self.MemberID_var.get(),self.Bookid_var.get()))
            DataPresent=my_cursor.fetchall()
            print(DataPresent)
            if DataPresent !="":
                my_cursor.execute("delete from Issue_Book where ID=%s and Book_Id=%s",(self.MemberID_var.get(),self.Bookid_var.get()))
                ConnectionDatabase.commit()
                ConnectionDatabase.close()
                msg.showinfo("Succedd","Data is deleted")
            else:
                msg.showerror("ERROR","Data Not Present In DataBase")
            self.fetch_data()
            # self.reset()
         
root=Tk()
obj=library_man(root)
root.mainloop()