from tkinter import *
from PIL import ImageTk,Image
from matplotlib.pyplot import title #PIL -> Pillow
import pymysql
from tkinter import messagebox

def reportPage():
    
    root = Tk()
    root.title("Book Page")
    root.geometry("1500x900")
    
    #background color
    Canvas1 = Canvas(root)
    Canvas1.config(bg="pink")
    Canvas1.pack(expand=True, fill=BOTH)

    #yellow outside borders
    headingFrame1 = Frame(root, bg="white", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

    #inner borders
    headingLabel = Label(headingFrame1, text="Select one of the Option Below:", bg="black", fg="white", font=('Courier',15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)
    
    rpbtn1 = Button(root, text="11. Search", bg="white", fg="black", command=searchBook)
    rpbtn1.place(relx=0.28, rely=0.3, relwidth=0.45, relheight=0.1)
    
    rpbtn2 = Button(root, text="12. Books On Loan", bg="white", fg="black", command=bookOnLoan)
    rpbtn2.place(relx=0.28, rely=0.4, relwidth=0.45, relheight=0.1)
    
    rpbtn3 = Button(root, text="13. Books On Reservation", bg="white", fg="black", command=bookOnReservation)
    rpbtn3.place(relx=0.28, rely=0.5, relwidth=0.45, relheight=0.1)

    rpbtn4 = Button(root, text="14. Outstanding Fines", bg="white", fg="black", command=outstandingFine)
    rpbtn4.place(relx=0.28, rely=0.6, relwidth=0.45, relheight=0.1)

    rpbtn5 = Button(root, text="15. Books On Loan to Member", bg="white", fg="black",command=bookLoanMem)
    rpbtn5.place(relx=0.28, rely=0.7, relwidth=0.45, relheight=0.1)
    
    quitBtn = Button(root,text="Back to Main Menu",bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.28,rely=0.9, relwidth=0.45,relheight=0.1)

def searchBook():
    global titleInput, authoerInput, isbnInput, publisherInput,pubYearInput, con, cur, root, memIDInput

    root = Tk()
    root.title("Book Search Page")
    root.geometry("1500x900")
    
    Canvas1 = Canvas(root)
    Canvas1.config(bg="pink")
    Canvas1.pack(expand=True, fill=BOTH)

    #outer border
    headingFrame1 = Frame(root, bg="white", bd=5)
    headingFrame1.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.13)
    
    #add a leabel to heading Frame
    #inner border
    headingLabel = Label(headingFrame1, text="Search based on one of the categories below", bg="black", fg="white", font=('Courier',15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    #below outer background
    #add a label frame to canvas to give a lebl insite it to delete book
    LabelFrame = Frame(root, bg="black")
    LabelFrame.place(relx=0.1, rely=0.25, relwidth=0.8, relheight=0.6)

    #take in inputs
    title = Label(LabelFrame, text="Title ", bg="black", fg="white")
    title.place(relx=0.05, rely=0.3)

    titleInput = Entry(LabelFrame)
    titleInput.place(relx=0.3, rely=0.3, relwidth=0.62)
    
    author = Label(LabelFrame, text="Author ", bg="black", fg="white")
    author.place(relx=0.05, rely=0.4)

    authoerInput = Entry(LabelFrame)
    authoerInput.place(relx=0.3, rely=0.4, relwidth=0.62)
        
    isbn = Label(LabelFrame, text="ISBN ", bg="black", fg="white")
    isbn.place(relx=0.05, rely=0.5)

    isbnInput = Entry(LabelFrame)
    isbnInput.place(relx=0.3, rely=0.5, relwidth=0.62)
    
    publisher = Label(LabelFrame, text="Publisher ", bg="black", fg="white")
    publisher.place(relx=0.05, rely=0.6)

    publisherInput = Entry(LabelFrame)
    publisherInput.place(relx=0.3, rely=0.6, relwidth=0.62)
    
    pubYear = Label(LabelFrame, text="Publication Year ", bg="black", fg="white")
    pubYear.place(relx=0.05, rely=0.7)

    pubYearInput = Entry(LabelFrame)
    pubYearInput.place(relx=0.3, rely=0.7, relwidth=0.62)

    #submit button    
    submitBtn = Button(root, text="Search Book", bg="lightblue", fg="black", command = displayBooksSearched)
    submitBtn.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)

    quitBtn = Button(root, text="Back to Reports Menu", bg="lightblue", fg="black", command=root.destroy)
    quitBtn.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)

    root.mainloop()


def displayBooksSearched():
    root = Tk()
    root.title("Books displayed")
    root.minsize(width=400, height=400)
    root.geometry("1500x900")

    Canvas1 = Canvas(root)
    Canvas1.config(bg="#5F9EA0")
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root, bg="white", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)
    headingLabel = Label(headingFrame1, text="Books displayed", bg="black", fg="white", font=('Courier',15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    LabelFrame = Frame(root, bg="black")
    LabelFrame.place(relx=0.01, rely=0.25, relwidth=0.98, relheight=0.6)

    #add a text label to LabeFrame. "%s %s %s %s %s %s"%("{0:>10}".format(Accession No.),"{0:>40}".format('Title'),"{0:>60}".format('Author'),"{0:>70}".format('ISBN'),"{0:>60}".format('Publisher'),"{0:>20}".format('Year'))
    textLabel = Label(LabelFrame, text="%s %s %s %s %s %s"%("{0:>10}".format('Accession No.'),"{0:>40}".format('Title'),"{0:>60}".format('Author'),"{0:>70}".format('ISBN'),"{0:>60}".format('Publisher'),"{0:>20}".format('Year')),
                    bg="black", fg="white")
    textLabel.place(relx=0.07, rely=0.1)

    #addLine
    addline = Label(LabelFrame, text = "-"*500,bg="black", fg="white")
    addline.place(relx=0.05, rely=0.2)
    
    y = 0.25 #declare var to increase the height at y-axis to print details
    #query to retrieve details from books table
    
    title = titleInput.get() 
    authors = authoerInput.get() 
    isbn = isbnInput.get() 
    publisher = publisherInput.get() 
    pubyear = pubYearInput.get()

    if title == "" or authors == "" or isbn == "" or publisher == "" or pubyear == "": 
        messagebox.showinfo("Insufficient Info") 
        return

    con = pymysql.connect(host="localhost", user="root", password="yja9974533", database="library")
    cur = con.cursor()

    query = f'SELECT * FROM book WHERE title LIKE "%{title}%" AND authors LIKE "%{authors}%" AND isbn LIKE "%{isbn}%" AND publisher LIKE "%{publisher}%" AND year LIKE "%{pubyear}%"' 

    cur.execute(query)
    con.commit()
    
    for i in cur:
        Label(LabelFrame, text="%s %s %s %s %s %s"%("{0:>10}".format(i[0]),"{0:>40}".format(i[1]),"{0:>60}".format(i[2]),"{0:>70}".format(i[3]),"{0:>60}".format(i[4]),"{0:>20}".format(i[5])),
                bg="black", fg="white").place(relx=0.07, rely=y)
        y += 0.1

    quitBtn = Button(root, text="Back to Reports Menu", bg='lightblue', fg="black", command=root.destroy)
    quitBtn.place(relx=0.45, rely=0.7, relwidth=0.10, relheight=0.05)

    root.mainloop()

def bookOnLoan():  
    root = Tk()
    root.title("Book on Loan")
    root.minsize(width=400, height=400)
    root.geometry("1500x900")

    Canvas1 = Canvas(root)
    Canvas1.config(bg="#5F9EA0")
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root, bg="white", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)
    headingLabel = Label(headingFrame1, text="Books on Loan Report", bg="black", fg="white", font=('Courier',15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    LabelFrame = Frame(root, bg="black")
    LabelFrame.place(relx=0.01, rely=0.25, relwidth=0.98, relheight=0.6)

    #add a text label to LabeFrame
    textLabel = Label(LabelFrame, text="%10s %15s %20s %20s %30s %25s"%('Accession No.', 'Title', 'Author', 'ISBN', 'Publisher', 'Year'),
                    bg="black", fg="white")
    textLabel.place(relx=0.07, rely=0.1)

    #addLine
    addline = Label(LabelFrame, text = "-----------------------------------------------------------------------------------------------------------",bg="black", fg="white")
    addline.place(relx=0.05, rely=0.2)
    
    y = 0.25 #declare var to increase the height at y-axis to print details
    #query to retrieve details from books table
    getBooksOnLoan = "SELECT book.accessionNum, title, authors, isbn, publisher, year FROM book LEFT JOIN Loan USING(accessionNum)"
    try:
        con = pymysql.connect(host="localhost", user="root", password="yja9974533", database="library")
        cur = con.cursor()
        cur.execute(getBooksOnLoan)
        con.commit()
        for i in cur:
            Label(LabelFrame, text="%10s %40s %30s %20s %20s %30s"%(i[0],i[1],i[2],i[3],i[4],i[5]),
                    bg="black", fg="white").place(relx=0.07, rely=y)
            y += 0.1
            
    except:
         messagebox.showinfo("Error","Failed to Fetch files from database")

    quitBtn = Button(root, text="Back to Reports Menu", bg='lightblue', fg="black", command=root.destroy)
    quitBtn.place(relx=0.4, rely=0.9, relwidth=0.18, relheight=0.08)

    root.mainloop()

def bookOnReservation():
    root = Tk()
    root.title("Book on Reservation")
    root.minsize(width=400, height=400)
    root.geometry("1500x900")

    Canvas1 = Canvas(root)
    Canvas1.config(bg="#5F9EA0")
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root, bg="white", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)
    headingLabel = Label(headingFrame1, text="Books on Reservation Report", bg="black", fg="white", font=('Courier',15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    LabelFrame = Frame(root, bg="black")
    LabelFrame.place(relx=0.01, rely=0.25, relwidth=0.98, relheight=0.6)

    #add a text label to LabeFrame
    textLabel = Label(LabelFrame, text="%10s %20s %30s %20s"%('Accession No.','Title','Membership ID','Name'),
                    bg="black", fg="white")
    textLabel.place(relx=0.07, rely=0.1)

    #addLine
    addline = Label(LabelFrame, text = "-------------------------------------------------------------------------------------",bg="black", fg="white")
    addline.place(relx=0.05, rely=0.2)
    
    y = 0.25 #declare var to increase the height at y-axis to print details
    # #query to retrieve details from books table
    getBooksOnReservation = "SELECT accessionNum, book.title, memberID, member.name FROM reservation LEFT JOIN book USING (accessionNum) LEFT JOIN member USING (memberID)"
    try:
        con = pymysql.connect(host="localhost", user="root", password="yja9974533", database="library")
        cur = con.cursor()
        cur.execute(getBooksOnReservation)
        con.commit()
        for i in cur:
            Label(LabelFrame, text="%10s %40s %30s %20s"%(i[0],i[1],i[2],i[3]),
                    bg="black", fg="white").place(relx=0.07, rely=y)
            y += 0.1
            
    except:
         messagebox.showinfo("Error","Failed to Fetch files from database")

    quitBtn = Button(root, text="Back to Reports Menu", bg='lightblue', fg="black", command=root.destroy)
    quitBtn.place(relx=0.4, rely=0.9, relwidth=0.18, relheight=0.08)

    root.mainloop()

def outstandingFine():
    root = Tk()
    root.title("Outstanding Fines")
    root.minsize(width=400, height=400)
    root.geometry("1500x900")

    Canvas1 = Canvas(root)
    Canvas1.config(bg="#5F9EA0")
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root, bg="white", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)
    headingLabel = Label(headingFrame1, text="Members with Outstanding Fines", bg="black", fg="white", font=('Courier',15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    LabelFrame = Frame(root, bg="black")
    LabelFrame.place(relx=0.01, rely=0.25, relwidth=0.98, relheight=0.6)

    #add a text label to LabeFrame
    textLabel = Label(LabelFrame, text="%10s %15s %20s %20s %20s"%('Membership ID','Name','Faculty','Phone Number' , 'Email'),
                    bg="black", fg="white")
    textLabel.place(relx=0.07, rely=0.1)

    #addLine
    addline = Label(LabelFrame, text = "-------------------------------------------------------------------------------------",bg="black", fg="white")
    addline.place(relx=0.05, rely=0.2)
    
    y = 0.25 #declare var to increase the height at y-axis to print details
    # #query to retrieve details from books table
    getMembersWithFine = "SELECT member.memberID, name, faculty, phoneNumber, email FROM fine LEFT JOIN member USING (memberID)"
    try:
        con = pymysql.connect(host="localhost", user="root", password="yja9974533", database="library")
        cur = con.cursor()
        cur.execute(getMembersWithFine)
        con.commit()
        for i in cur:
            Label(LabelFrame, text="%10s %25s %20s %20s %20s"%(i[0],i[1],i[2],i[3], i[4]),
                    bg="black", fg="white").place(relx=0.07, rely=y)
            y += 0.1
            
    except:
         messagebox.showinfo("Error","Failed to Fetch files from database")

    quitBtn = Button(root, text="Back to Reports Menu", bg='lightblue', fg="black", command=root.destroy)
    quitBtn.place(relx=0.4, rely=0.9, relwidth=0.18, relheight=0.08)

    root.mainloop()

def bookLoanMem():

    global memIDInput, con, cur, root
    
    root = Tk()
    root.title("Book on Loan to Member Page")
    root.geometry("1500x900")
    
    Canvas1 = Canvas(root)
    Canvas1.config(bg="pink")
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root, bg="white", bd=5)
    headingFrame1.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.13)
    
    #add a leabel to heading Frame
    headingLabel = Label(headingFrame1, text="Search based on one of the categories below", bg="black", fg="white", font=('Courier',15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    #add a label frame to canvas to give a lebl insite it to delete book
    LabelFrame = Frame(root, bg="black")
    LabelFrame.place(relx=0.1, rely=0.25, relwidth=0.8, relheight=0.6)

    #take in inputs
    memID = Label(LabelFrame, text="Membership ID ", bg="black", fg="white")
    memID.place(relx=0.05, rely=0.3)

    memIDInput = Entry(LabelFrame)
    memIDInput.place(relx=0.3, rely=0.3, relwidth=0.62)
    
    #submit button    
    submitBtn = Button(root, text="Search Member", bg="lightblue", fg="black", command = displayBooksGivenID)
    submitBtn.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)

    quitBtn = Button(root, text="Back to Reports Menu", bg="lightblue", fg="black", command=root.destroy)
    quitBtn.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)

    root.mainloop()


def displayBooksGivenID():
    
    root = Tk()
    root.title("Book on Loan Given MemberID")
    root.minsize(width=400, height=400)
    root.geometry("1500x900")

    Canvas1 = Canvas(root)
    Canvas1.config(bg="#5F9EA0")
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root, bg="white", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)
    headingLabel = Label(headingFrame1, text="Books on Loan Report", bg="black", fg="white", font=('Courier',15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    LabelFrame = Frame(root, bg="black")
    LabelFrame.place(relx=0.01, rely=0.25, relwidth=0.98, relheight=0.6)

    #add a text label to LabeFrame
    textLabel = Label(LabelFrame, text="%10s %15s %20s %20s %30s %25s"%('Accession No.', 'Title', 'Author', 'ISBN', 'Publisher', 'Year'),
                    bg="black", fg="white")
    textLabel.place(relx=0.07, rely=0.1)

    #addLine
    addline = Label(LabelFrame, text = "-----------------------------------------------------------------------------------------------------------",bg="black", fg="white")
    addline.place(relx=0.05, rely=0.2)
    
    y = 0.25 #declare var to increase the height at y-axis to print details
    #query to retrieve details from books table
    member_id = memIDInput.get() 
    getBooksOnLoanGivenMem = "SELECT book.accessionNum, title, authors, isbn, publisher, year FROM book LEFT JOIN Loan USING(accessionNum) WHERE Loan.memberID = '%s'" %(member_id)

    try:
        con = pymysql.connect(host="localhost", user="root", password="yja9974533", database="library")
        cur = con.cursor()
        cur.execute(getBooksOnLoanGivenMem)
        con.commit()
        for i in cur:
            Label(LabelFrame, text="%10s %40s %30s %20s %20s %30s"%(i[0],i[1],i[2],i[3],i[4],i[5]),
                    bg="black", fg="white").place(relx=0.07, rely=y)
            y += 0.1
            
    except:
         messagebox.showinfo("Error","Failed to Fetch files from database")

    quitBtn = Button(root, text="Back to Reports Menu", bg='lightblue', fg="black", command=root.destroy)
    quitBtn.place(relx=0.4, rely=0.9, relwidth=0.18, relheight=0.08)

    root.mainloop()

    

    
        