from tkinter import *
from PIL import ImageTk,Image
from matplotlib.pyplot import title #PIL -> Pillow
import pymysql
from tkinter import messagebox
from datetime import datetime

# Main membership page
def bookPage():
    root = Tk()
    root.title("Book Page")
    root.geometry("1500x900")
    
    Canvas1 = Canvas(root)
    Canvas1.config(bg="PeachPuff2")
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root, bg="white", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)
    
    #add a leabel to heading Frame
    headingLabel = Label(headingFrame1, text="Select one of the Option Below:", bg="black", fg="white", font=('Courier',15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    bbtn1 = Button(root, text="4. Acquisition: Book Acquisition", bg="white", fg="black", command=acquisition)
    bbtn1.place(relx=0.28, rely=0.3, relwidth=0.45, relheight=0.1)
    
    bbtn2 = Button(root, text="5. Withdrawal: Book Withdrawal", bg="white", fg="black", command=withdraw)
    bbtn2.place(relx=0.28, rely=0.4, relwidth=0.45, relheight=0.1)
    

    quitBtn = Button(root,text="Back to Main Menu",bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.28,rely=0.9, relwidth=0.45,relheight=0.1)


# Create acquistion page
def acquisition():
    global accessNumInput, titleInput, authorInput, isbnInput, publisherInput, pubYearInput, con, cur, root
    root = Tk()
    root.title("Aquisition Page")
    root.geometry("1500x900")
    
    Canvas1 = Canvas(root)
    Canvas1.config(bg="PeachPuff2")
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root, bg="white", bd=5)
    headingFrame1.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.13)
    
    #add a leabel to heading Frame
    headingLabel = Label(headingFrame1, text="For New Book Acquisition \n Please Enter Required Information Below:", bg="black", fg="white", font=('Courier',15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    #add a label frame to canvas to give a lebl insite it to delete book
    LabelFrame = Frame(root, bg="black")
    LabelFrame.place(relx=0.1, rely=0.25, relwidth=0.8, relheight=0.6)

    #take in inputs
    accessNum = Label(LabelFrame, text="Accession Number ", bg="black", fg="white")
    accessNum.place(relx=0.05, rely=0.3)

    accessNumInput = Entry(LabelFrame)
    accessNumInput.place(relx=0.3, rely=0.3, relwidth=0.62)
    
    title = Label(LabelFrame, text="Title ", bg="black", fg="white")
    title.place(relx=0.05, rely=0.4)

    titleInput = Entry(LabelFrame)
    titleInput.place(relx=0.3, rely=0.4, relwidth=0.62)
    
    author = Label(LabelFrame, text="Author ", bg="black", fg="white")
    author.place(relx=0.05, rely=0.5)

    authorInput = Entry(LabelFrame)
    authorInput.place(relx=0.3, rely=0.5, relwidth=0.62)
        
    isbn = Label(LabelFrame, text="ISBN ", bg="black", fg="white")
    isbn.place(relx=0.05, rely=0.6)

    isbnInput = Entry(LabelFrame)
    isbnInput.place(relx=0.3, rely=0.6, relwidth=0.62)
    
    publisher = Label(LabelFrame, text="Publisher ", bg="black", fg="white")
    publisher.place(relx=0.05, rely=0.7)

    publisherInput = Entry(LabelFrame)
    publisherInput.place(relx=0.3, rely=0.7, relwidth=0.62)
    
    pubYear = Label(LabelFrame, text="Publication Year ", bg="black", fg="white")
    pubYear.place(relx=0.05, rely=0.8)

    pubYearInput = Entry(LabelFrame)
    pubYearInput.place(relx=0.3, rely=0.8, relwidth=0.62)

    #submit button    
    submitBtn = Button(root, text="Add New Book", bg="lightblue", fg="black", command=add_book)
    submitBtn.place(relx=0.28, rely=0.86, relwidth=0.15, relheight=0.08)

    quitBtn = Button(root, text="Back to Books Menu", bg="lightblue", fg="black", command=root.destroy)
    quitBtn.place(relx=0.53, rely=0.86, relwidth=0.15, relheight=0.08)

    root.mainloop()

# Create withdraw page
def withdraw():
    global accessNuminput, con, cur, root
    root = Tk()
    root.title("Withdraw Book Page")
    root.geometry("1500x900")
    
    Canvas1 = Canvas(root)
    Canvas1.config(bg="PeachPuff2")
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root, bg="white", bd=5)
    headingFrame1.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.13)
    
    #add a leabel to heading Frame
    headingLabel = Label(headingFrame1, text="To Remove Outdated Books From System \n Please Enter Required Information Below:", bg="black", fg="white", font=('Courier',15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    #add a label frame to canvas to give a lebl insite it to delete book
    LabelFrame = Frame(root, bg="black")
    LabelFrame.place(relx=0.1, rely=0.25, relwidth=0.8, relheight=0.6)

    #take in inputs
    accessNum = Label(LabelFrame, text="Accession Number  ", bg="black", fg="white")
    accessNum.place(relx=0.05, rely=0.3)

    accessNuminput = Entry(LabelFrame)
    accessNuminput.place(relx=0.3, rely=0.3, relwidth=0.62)

    #submit button    
    submitBtn = Button(root, text="Withdraw Book", bg="lightblue", fg="black", command=withdraw_book)
    submitBtn.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.06)

    quitBtn = Button(root, text="Back to Books Menu", bg="lightblue", fg="black", command=root.destroy)
    quitBtn.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.06)

    root.mainloop()

def add_book(): 
    accessionNum = accessNumInput.get() 
    title = titleInput.get() 
    authors = authorInput.get() 
    isbn = isbnInput.get() 
    publisher = publisherInput.get() 
    pubyear = pubYearInput.get() 
 
    con = pymysql.connect(host = 'localhost', user = 'root', password = "yja9974533", db = "library") 
    cur = con.cursor() 

    if (accessionNum == "" or title == "" or authors == "" or isbn == "" or publisher == "" or pubyear == ""):
        messagebox.showinfo("Error!", "Missing or incomplete fields.")
        return

    query = "SELECT COUNT(*) FROM book WHERE accessionNum = '%s'" %(accessionNum)
    cur.execute(query)
    num_books = cur.fetchall()[0][0]

    if (num_books):
        messagebox.showinfo("Error!", "Book already in Library!")
        return
    
    query = "INSERT INTO book(accessionNum, title, authors, isbn, publisher, year) VALUES('%s', '%s', '%s', '%s', '%s', '%s')" %(accessionNum, title, authors, isbn, publisher, pubyear)
    cur.execute(query)
    con.commit()
    messagebox.showinfo("Success!", "Book successfully added into Library!")
    root.destroy()
    return
    


def withdraw_book(): 
    accessionNum = accessNumInput.get() 
 
    con = pymysql.connect(host = 'localhost', user = 'root', password = "yja9974533", db = "library") 
    cur = con.cursor() 
 
    reservations = f'SELECT COUNT(*) FROM reservation WHERE accessionNum = "{accessionNum}"' 
    cur.execute(reservations) 
    reservation_number = cur.fetchall()[0][0] 
 
    loans = f'SELECT COUNT(*) FROM loan WHERE accessionNum = "{accessionNum}"' 
    cur.execute(loans) 
    loan_number = cur.fetchall()[0][0] 
 
    search = f'SELECT COUNT(*) FROM book WHERE accessionNum = "{accessionNum}"' 
    cur.execute(search) 
    book_exists = cur.fetchall()[0][0] 
 
    if not book_exists: 
        messagebox.showinfo("Error", "Book is not in libary") 
        return
    
    if reservation_number == 0 and loan_number == 0: 
        deletion = f'DELETE FROM book WHERE accessionNum = "{accessionNum}"' 
        cur.execute(deletion) 
        messagebox.showinfo("Success", "Book has been withdrawn from circulation") 
        return True 
 
    elif reservation_number != 0: 
        messagebox.showinfo("Error", "Book currently has active reservation") 
        return False 
    else: 
        messagebox.showinfo("Error", "Book is currently loaned out") 
        return False

