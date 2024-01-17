from tkinter import *
import mysql.connector
import tkinter.messagebox as msg
class BookData():
    def __init__(self,root):
        self.root=root
        self.root.minsize(300,300)
        self.root.maxsize(300,300)
        self.root.title("Add Books")
        self.root.wm_iconbitmap('icon.ico')

        titlelabel=Label(root,text="Add Books",bg="BLUE",fg="WHITE",bd=8,relief="ridge",font=("times",20,"bold"),padx=3,pady=5)
        titlelabel.pack(side=TOP,fill=X)

        self.Bookid_var=StringVar()
        self.BookName_var=StringVar()
        self.AuthorName_var=StringVar()
        self.BookPrice_var=StringVar()

        frame=Frame(root,bd=9,relief="ridge",padx=9,pady=10,bg="GREEN")
        frame.place(x=0,y=57,width=300,height=243)

        Bookid=Label(frame,text="Book Id",font=("Regular",13,"bold"),fg="BLACK",bg="GREEN",padx=2,pady=7)
        Bookid.grid(row=0,column=0,sticky=W)
        BookName=Label(frame,text="Book Name",font=("Regular",13,"bold"),fg="BLACK",bg="GREEN",padx=2,pady=7)
        BookName.grid(row=1,column=0,sticky=W)
        AuthorName=Label(frame,text="Author Name",font=("Regular",13,"bold"),fg="BLACK",bg="GREEN",padx=2,pady=7)
        AuthorName.grid(row=2,column=0,sticky=W)
        BookPrice=Label(frame,text="Book Price",font=("Regular",13,"bold"),fg="BLACK",bg="GREEN",padx=2,pady=7)
        BookPrice.grid(row=3,column=0,sticky=W)

        Bookid_entry=Entry(frame,textvariable=self.Bookid_var,width=22)
        Bookid_entry.grid(row=0,column=1)
        BookName_entry=Entry(frame,textvariable=self.BookName_var,width=22)
        BookName_entry.grid(row=1,column=1)
        AuthorName_entry=Entry(frame,textvariable=self.AuthorName_var,width=22)
        AuthorName_entry.grid(row=2,column=1)
        BookPrice_entry=Entry(frame,textvariable=self.BookPrice_var,width=22)
        BookPrice_entry.grid(row=3,column=1)

        AddButton=Button(frame,text="Add Book",fg="WHITE",command=self.AddBookFunction,bg="BLUE",padx=3,pady=5)
        AddButton.grid(row=4,column=0,columnspan=2,pady=10)
        self.root.bind('<Return>',self.AddBookFunction)
    def AddBookFunction(self,event):
        result=self.AddBookData()
        if result == 0:
            exit()
        else:
            pass

    def AddBookData(self):
        try:
            int(self.BookPrice_var.get())
            conn=mysql.connector.connect(host="localhost",username="root",password="eninja-library",database="lms")
            my_cursor=conn.cursor()
            my_cursor.execute("Select * from Book_Data where Book_Id=%s",(self.Bookid_var.get(),))
            BookCheck=my_cursor.fetchall()
            if BookCheck == []:
                my_cursor.execute("insert into Book_Data values(%s,%s,%s,%s)",(self.Bookid_var.get(),self.BookName_var.get(),self.AuthorName_var.get(),self.BookPrice_var.get()))
                msg.showinfo("SUCCESS","Book Successfully Added")
            else:
                msg.showerror("ERROR","Book ID Already Exist")
            Ans=msg.askretrycancel("LMS","Add Book Again")
            if Ans == True:
                self.Bookid_var.set("")
                self.AuthorName_var.set("")
                self.BookName_var.set("")
                self.BookPrice_var.set("")
            else:
                conn.commit()
                conn.close()
                return 0
        except:
            msg.showerror("ERROR","Enter A Valid Price")
            self.BookPrice_var.set("")

root=Toplevel()
obj=BookData(root)
root.mainloop()