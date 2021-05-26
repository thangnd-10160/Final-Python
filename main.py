# first pip install in pycharm PyMySQL,pillow and tkinter
from ViewAds import ViewAds
from DelAds import deleteAds
from AddAds import addAds
from ViewNewsPaper import ViewNewPaper
from DelNewPaper import deleteNewPaper
from AddNewsPaper import addNewsPaper
from tkinter import *
from PIL import ImageTk,Image
import pymysql
from tkinter import messagebox

#We use MySQL Workbench 8.0 CE
# =>  create database dbNews;
#then
# =>  create table News(bid varchar(20) primary key, title varchar(30), author varchar(30), status varchar(30));
# =>  create table Ads(bid varchar(20) primary key, title varchar(30), author varchar(30), status varchar(30));

mypass = "root"
mydatabase="dbNews"

con = pymysql.connect(host="localhost",user="root",password=mypass,database=mydatabase)
cur = con.cursor()

root = Tk()
root.title("VNexpress")
root.minsize(width=600,height=600)
root.geometry("600x500")

same=True
n=0.25

# Adding a background image (source: Pinterest)

background_image =Image.open("readnew.jpg")
[imageSizeWidth, imageSizeHeight] = background_image.size

newImageSizeWidth = int(imageSizeWidth*n)
if same:
    newImageSizeHeight = int(imageSizeHeight*n) 
else:
    newImageSizeHeight = int(imageSizeHeight/n) 
    
background_image = background_image.resize((newImageSizeWidth,newImageSizeHeight),Image.ANTIALIAS)
img = ImageTk.PhotoImage(background_image)

Canvas1 = Canvas(root)

Canvas1.create_image(300,340,image = img)      
Canvas1.config(bg="white",width = newImageSizeWidth, height = newImageSizeHeight)
Canvas1.pack(expand=True,fill=BOTH)

headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)

headingLabel = Label(headingFrame1, text="Welcome to VNexpress", bg='black', fg='white', font=('Courier',15))
headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

btn1 = Button(root,text="Add News",bg='black', fg='white',command=addNewsPaper)
btn1.place(relx=0.28,rely=0.3, relwidth=0.45,relheight=0.1)
    
btn2 = Button(root,text="Delete News",bg='black', fg='white',command=deleteNewPaper)
btn2.place(relx=0.28,rely=0.4, relwidth=0.45,relheight=0.1)
    
btn3 = Button(root,text="View News",bg='black', fg='white',command=ViewNewPaper)
btn3.place(relx=0.28,rely=0.5, relwidth=0.45,relheight=0.1)
    
btn4 = Button(root,text="Add Ads",bg='black', fg='white',command= addAds)
btn4.place(relx=0.28,rely=0.6, relwidth=0.45,relheight=0.1)

btn5 = Button(root,text="Delete Ads",bg='black', fg='white',command=deleteAds)
btn5.place(relx=0.28,rely=0.7, relwidth=0.45,relheight=0.1)

btn6 = Button(root,text="View Ads",bg='black', fg='white',command=ViewAds)
btn6.place(relx=0.28,rely=0.8, relwidth=0.45,relheight=0.1)
root.mainloop()
