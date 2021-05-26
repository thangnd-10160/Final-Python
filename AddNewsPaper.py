from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import pymysql

def newsRegister():
    
    bid = Info1.get()
    title = Info2.get()
    author = Info3.get()
    status = Info4.get()
    status = status.lower()
    
    insertNews = "insert into "+NewsTable+" values('"+bid+"','"+title+"','"+author+"','"+status+"')"
    try:
        cur.execute(insertNews)
        con.commit()
        messagebox.showinfo('Success',"News added successfully")
    except:
        messagebox.showinfo("Error","Can't add data into VNexpress Database")
    
    


    root.destroy()
    
def addNewsPaper():
    
    global Info1,Info2,Info3,Info4,Canvas1,con,cur,NewsTable,root
    
    root = Tk()
    root.title("Add Newspaper")
    root.minsize(width=400,height=400)
    root.geometry("600x500")

    # Add database and password
    mypass = "root"
    mydatabase="dbNews"

    con = pymysql.connect(host="localhost",user="root",password=mypass,database=mydatabase)
    cur = con.cursor()

    # Enter Table Names
    NewsTable = "news"

    Canvas1 = Canvas(root)
    
    Canvas1.config(bg="#ff6e40")
    Canvas1.pack(expand=True,fill=BOTH)
        
    headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)

    headingLabel = Label(headingFrame1, text="Add News", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)


    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.4,relwidth=0.8,relheight=0.4)
        
   
    lb1 = Label(labelFrame,text=" News ID : ", bg='black', fg='white')
    lb1.place(relx=0.05,rely=0.15, relheight=0.12)
        
    Info1 = Entry(labelFrame)
    Info1.place(relx=0.3,rely=0.15, relwidth=0.62, relheight=0.12)
        
    # Title
    lb2 = Label(labelFrame,text="Author : ", bg='black', fg='white')
    lb2.place(relx=0.05,rely=0.35, relheight=0.12)
        
    Info2 = Entry(labelFrame)
    Info2.place(relx=0.3,rely=0.35, relwidth=0.62, relheight=0.12)
        

    lb3 = Label(labelFrame,text="Title : ", bg='black', fg='white')
    lb3.place(relx=0.05,rely=0.55, relheight=0.12)
        
    Info3 = Entry(labelFrame)
    Info3.place(relx=0.3,rely=0.55, relwidth=0.62, relheight=0.12)
        

    lb4 = Label(labelFrame,text="Content : ", bg='black', fg='white')
    lb4.place(relx=0.05,rely=0.75, relheight=0.12)
        
    Info4 = Entry(labelFrame)
    Info4.place(relx=0.3,rely=0.75, relwidth=0.62, relheight=0.12)
        
  
    SubmitBtn = Button(root,text="SUBMIT",bg='#d1ccc0', fg='black',command=newsRegister)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()