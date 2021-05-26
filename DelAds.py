from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import pymysql

# Add database and password
mypass = "root"
mydatabase="dbNews"

con = pymysql.connect(host="localhost",user="root",password=mypass,database=mydatabase)
cur = con.cursor()

# Enter Table Names

AdsTable = "ads"


def DeleteAds():
    
    bid = Info1.get()
    
    deleteSql = "delete from "+AdsTable+" where bid = '"+bid+"'"

    try:
        cur.execute(deleteSql)
        con.commit()
        
        messagebox.showinfo('Success',"Ads Deleted Successfully")
    except:
        messagebox.showinfo("Please check Ads ID")
    

    print(bid)

    Info1.delete(0, END)
    root.destroy()
    
def deleteAds(): 
    
    global Info1,Info2,Info3,Info4,Canvas1,con,cur,AdsTable,root
    
    root = Tk()
    root.title("Delete Ads")
    root.minsize(width=400,height=400)
    root.geometry("600x500")

    
    Canvas1 = Canvas(root)
    
    Canvas1.config(bg="#006B38")
    Canvas1.pack(expand=True,fill=BOTH)
        
    headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        
    headingLabel = Label(headingFrame1, text="Delete Ads", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)   
        
    # Ads ID to Delete
    lb2 = Label(labelFrame,text="Ads ID : ", bg='black', fg='white')
    lb2.place(relx=0.05,rely=0.5)
        
    Info1 = Entry(labelFrame)
    Info1.place(relx=0.3,rely=0.5, relwidth=0.62,relheight=0.12)
    
    #Submit Button
    SubmitBtn = Button(root,text="SUBMIT",bg='#d1ccc0', fg='black',command=DeleteAds)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()