from tkinter import *
from PIL import ImageTk,Image #PIL -> Pillow
import pymysql
from tkinter import messagebox
from membershipPage import *
from bookPage import *
from loanPage import *
from reservationPage import *
from finePage import *
from reportPage import *



con = pymysql.connect(host="localhost", user="root", password="yja9974533", database="library")

cur = con.cursor()

#enter table names here
bookTable = "books"

root = Tk()
root.title("BT2102 Group 7")
root.minsize(width=400, height=400)
root.geometry("1500x900")


#Add the background Image
same = True
n = 0.55

background_image = Image.open("/Users/jianyang/Documents/Y1S2/BT2102 Data Management and Visualisation/Assignment 1/Code/lib3.jpeg")
[imageSizeWidth, imageSizeHeight] = background_image.size

#set the new image width and height
newImageSizeWidth = int(imageSizeWidth * n)

if same:
    newImageSizeHeight = int(imageSizeHeight * n)
else:
    newImageSizeHeight = int(imageSizeHeight / n)

background_image = background_image.resize((newImageSizeWidth, newImageSizeHeight), Image.ANTIALIAS)

#add an image to canva
img = ImageTk.PhotoImage(background_image)
canvas1 = Canvas(root)
canvas1.create_image(300, 340, image=img)
canvas1.config(bg="white", width=newImageSizeWidth, height=newImageSizeHeight)
canvas1.pack(expand=True, fill=BOTH)

#adding a heading Frame to library
headingFrame1 = Frame(root, bg="white", bd=5)
headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

headingLabel = Label(headingFrame1, text="ALS", bg="black", fg="white", font=('Courier',15))
headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

#Add the buttons
btn1 = Button(root, text="Membership", bg="white", fg="black" , command=membershipPage)
btn1.place(relx=0.15, rely=0.3, relwidth=0.3, relheight=0.15)

btn2 = Button(root, text="Books", bg="white", fg="black" , command=bookPage)
btn2.place(relx=0.55, rely=0.3, relwidth=0.3, relheight=0.15)

btn3 = Button(root, text="Loans",bg="white", fg="black", command= loanPage)
btn3.place(relx=0.15, rely=0.5, relwidth=0.3, relheight=0.15)

btn4 = Button(root, text="Reservation", bg="white", fg="black", command=reservationPage)
btn4.place(relx=0.55, rely=0.5, relwidth=0.3, relheight=0.15)

btn5 = Button(root, text="Fines", bg="white", fg="black", command= finePage)
btn5.place(relx=0.15, rely=0.7, relwidth=0.3, relheight=0.15)

btn6 = Button(root, text="Reports", bg="white", fg="black", command= reportPage)
btn6.place(relx=0.55, rely=0.7, relwidth=0.3, relheight=0.15)

quitBtn = Button(root, text="Quit", bg="white", fg="black", command=root.destroy)
quitBtn.place(relx=0.415, rely=0.9, relwidth=0.18, relheight=0.08)

root.mainloop() #call the mainloop to run the application


