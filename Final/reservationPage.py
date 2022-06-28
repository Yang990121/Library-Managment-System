from tkinter import *
from PIL import ImageTk,Image
from matplotlib.pyplot import title #PIL -> Pillow
import pymysql
from tkinter import messagebox
from datetime import datetime

def reservationPage():
    root = Tk()
    root.title("Book Page")
    root.geometry("1500x900")
    
    Canvas1 = Canvas(root)
    Canvas1.config(bg="lightblue")
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root, bg="white", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

    headingLabel = Label(headingFrame1, text="Select one of the Option Below:", bg="black", fg="white", font=('Courier',15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    rvbtn1 = Button(root, text="8. Reserve a Book: Book Reservation", bg="white", fg="black", command=reserveBook)
    rvbtn1.place(relx=0.2, rely=0.3, relwidth=0.6, relheight=0.1)
    
    rvbtn2 = Button(root, text="9. Cancel Reservation: Reservation Canellation", bg="white", fg="black", command=cancelReserve)
    rvbtn2.place(relx=0.2, rely=0.4, relwidth=0.6, relheight=0.1)
    

    quitBtn = Button(root,text="Back to Main Menu",bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.28,rely=0.9, relwidth=0.45,relheight=0.1)

def reserveBook():
    global accessNumInput, memIDInput, reserveDateInput, con, cur, root
    root = Tk()
    root.title("Reservation Page")
    root.geometry("1500x900")
    
    Canvas1 = Canvas(root)
    Canvas1.config(bg="lightblue")
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root, bg="white", bd=5)
    headingFrame1.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.13)
    
    #add a leabel to heading Frame
    headingLabel = Label(headingFrame1, text="To Reserve a Book \n Please Enter Information Below:", bg="black", fg="white", font=('Courier',15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    #add a label frame to canvas to give a lebl insite it to delete book
    LabelFrame = Frame(root, bg="black")
    LabelFrame.place(relx=0.1, rely=0.25, relwidth=0.8, relheight=0.6)

    #take in inputs
    accessNum = Label(LabelFrame, text="Accession Number ", bg="black", fg="white")
    accessNum.place(relx=0.05, rely=0.3)

    accessNumInput = Entry(LabelFrame)
    accessNumInput.place(relx=0.3, rely=0.3, relwidth=0.62)
    
    memID = Label(LabelFrame, text="Membership ID ", bg="black", fg="white")
    memID.place(relx=0.05, rely=0.4)

    memIDInput = Entry(LabelFrame)
    memIDInput.place(relx=0.3, rely=0.4, relwidth=0.62)
    
    reserveDate = Label(LabelFrame, text="Reserve Date ", bg="black", fg="white")
    reserveDate.place(relx=0.05, rely=0.5)

    reserveDateInput = Entry(LabelFrame)
    reserveDateInput.place(relx=0.3, rely=0.5, relwidth=0.62)

    #submit button    
    submitBtn = Button(root, text="Reserve Book", bg="lightblue", fg="black", command=reserve)
    submitBtn.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)

    quitBtn = Button(root, text="Back to \n Reservations Menu", bg="lightblue", fg="black", command=root.destroy)
    quitBtn.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)

    root.mainloop()

def cancelReserve():
    global accessNumInput, memIDInput, reserveDateInput
    root = Tk()
    root.title("Cancellation Page")
    root.geometry("1500x900")
    
    Canvas1 = Canvas(root)
    Canvas1.config(bg="lightblue")
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root, bg="white", bd=5)
    headingFrame1.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.13)
    
    #add a leabel to heading Frame
    headingLabel = Label(headingFrame1, text="To Cancel a Reservation \n Please Enter Information Below:", bg="black", fg="white", font=('Courier',15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    #add a label frame to canvas to give a lebl insite it to delete book
    LabelFrame = Frame(root, bg="black")
    LabelFrame.place(relx=0.1, rely=0.25, relwidth=0.8, relheight=0.6)

    #take in inputs
    accessNum = Label(LabelFrame, text="Accession Number ", bg="black", fg="white")
    accessNum.place(relx=0.05, rely=0.3)

    accessNumInput = Entry(LabelFrame)
    accessNumInput.place(relx=0.3, rely=0.3, relwidth=0.62)
    
    memID = Label(LabelFrame, text="Membership ID ", bg="black", fg="white")
    memID.place(relx=0.05, rely=0.4)

    memIDInput = Entry(LabelFrame)
    memIDInput.place(relx=0.3, rely=0.4, relwidth=0.62)
    
    reserveDate = Label(LabelFrame, text="Cancel Date ", bg="black", fg="white")
    reserveDate.place(relx=0.05, rely=0.5)

    reserveDateInput = Entry(LabelFrame)
    reserveDateInput.place(relx=0.3, rely=0.5, relwidth=0.62)

    #submit button    
    submitBtn = Button(root, text="Cancel Reservation", bg="lightblue", fg="black", command=cancel_reservation)
    submitBtn.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)

    quitBtn = Button(root, text="Back to \n Reservations Menu", bg="lightblue", fg="black", command=root.destroy)
    quitBtn.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)

    root.mainloop()

def reserve(): 
    accessionNum = accessNumInput.get() 
    memberID = memIDInput.get() 
    reserveDate = reserveDateInput.get()
 
    con = pymysql.connect(host = 'localhost', user = 'root', password = "yja9974533", db = "library") 
    cur = con.cursor() 
 
    checkfines = f'SELECT COUNT(*) FROM fine WHERE memberID = "{memberID}"' 
    cur.execute(checkfines) 
    fines = cur.fetchall()[0][0] 
     
    reserved = f'SELECT COUNT(*) FROM reservation WHERE memberID != "{memberID}" AND accessionNum = "{accessionNum}"' 
    cur.execute(reserved) 
    reservedNum = cur.fetchall()[0][0] 
 
    myReserved = f'SELECT COUNT(*) FROM reservation WHERE memberID = "{memberID}"' 
    cur.execute(myReserved) 
    myReservedNum = cur.fetchall()[0][0] 
 
    currentID = f'SELECT MAX(reservationID) FROM reservation' 
    cur.execute(currentID) 
    currentID = cur.fetchall()[0][0]

    validID = f'SELECT COUNT(*) FROM member WHERE memberID = "{memberID}"'
    cur.execute(validID)
    validID = cur.fetchall()[0][0]

    validAccess = f'SELECT COUNT(*) FROM book WHERE accessionNum = "{accessionNum}"'
    cur.execute(validAccess)
    validAccess = cur.fetchall()[0][0]

    if accessionNum == "" or memberID == "" or reserveDate == "":
        messagebox.showinfo("Error", "Missing inputs")
        return
    
    if not validID:
        messagebox.showinfo("Error", "Invalid Member ID")
        return
    elif not validAccess:
        messagebox.showinfo("Error", "Invalid Accession Number")
        return

    elif fines > 0: 
        messagebox.showinfo("Error", "Member has outstanding fines") 
        return 
    elif reservedNum > 0:
        print(reservedNum)
        messagebox.showinfo("Error", "Book is already reserved") 
        return 
    elif myReservedNum == 2: 
        messagebox.showinfo("Error", "User already has reserved 2 books") 
        return 
    else: 
        query = f"INSERT INTO reservation (reservationID, accessionNum, memberID, ReservationDate) Values ({currentID + 1}, {accessionNum},{memberID} ,{datetime.today})" 
        cur.execute(query) 
        con.commit() 
        messagebox.showinfo("Success", "Book is reserved") 
        return True

def cancel_reservation(): 
    accessionNum = accessNumInput.get() 
    memberID = memIDInput.get() 
    
 
    con = pymysql.connect(host = 'localhost', user = 'root', password = "yja9974533", db = "library") 
    cur = con.cursor() 
 
    memberquery = f'SELECT COUNT(*) FROM reservation WHERE memberID = "{memberID}" AND accessionNum = "{accessionNum}"' 
    cur.execute(memberquery) 
    exists = cur.fetchall()[0][0] 
     
    if exists: 
        deletion = f'DELETE FROM reservation WHERE memberID = "{memberID}"' 
        cur.execute(deletion) 
        con.commit() 
        messagebox.showinfo("Successful", "Reservation deleted") 
        return 
    else: 
        messagebox.showinfo("Error", "Reservation does not exist") 
        return