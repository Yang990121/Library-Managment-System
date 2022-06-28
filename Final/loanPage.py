from tkinter import *
from PIL import ImageTk,Image
from matplotlib.pyplot import title #PIL -> Pillow
import pymysql
from tkinter import messagebox
import datetime

def loanPage():
    root = Tk()
    root.title("Book Page")
    root.geometry("1500x900")
    
    Canvas1 = Canvas(root)
    Canvas1.config(bg="#5F9EA0")
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root, bg="white", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

    headingLabel = Label(headingFrame1, text="Select one of the Option Below:", bg="black", fg="white", font=('Courier',15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)
    
    lbtn1 = Button(root, text="6. Borrow: Book Borrowing", bg="white", fg="black" , command=borrowBook)
    lbtn1.place(relx=0.28, rely=0.3, relwidth=0.45, relheight=0.1)
    
    lbtn2 = Button(root, text="7. Return: Book Returning", bg="white", fg="black", command=returnBook)
    lbtn2.place(relx=0.28, rely=0.4, relwidth=0.45, relheight=0.1)
    

    quitBtn = Button(root,text="Back to Main Menu",bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.28,rely=0.9, relwidth=0.45,relheight=0.1)


def borrowBook():
    global accessNumInput, memIDInput, returnDateInput, con, cur, root, input
    root = Tk()
    root.title("Borrow Page")
    root.geometry("1500x900")
    
    Canvas1 = Canvas(root)
    Canvas1.config(bg="#5F9EA0")
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root, bg="white", bd=5)
    headingFrame1.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.13)
    
    #add a leabel to heading Frame
    headingLabel = Label(headingFrame1, text="To Borrow a Book \n Please Enter Information Below:", bg="black", fg="white", font=('Courier',15))
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

    #submit button    
    submitBtn = Button(root, text="Borrow Book", bg="lightblue", fg="black", command= borrow_book)
    submitBtn.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)

    quitBtn = Button(root, text="Back to Loan Menu", bg="lightblue", fg="black", command=root.destroy)
    quitBtn.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)

    root.mainloop()




def borrow_book():
    con = pymysql.connect(host = 'localhost', user = 'root', password = "yja9974533", db = "library") 
    cur = con.cursor() 
    query = "SELECT * FROM book WHERE accessionNum = '%s'" %(accessNumInput.get())
    cur.execute(query)
    book_exists = cur.fetchall()

    query = "SELECT COUNT(*) FROM member WHERE memberID = '%s'" %(memIDInput.get())
    cur.execute(query)
    member_exist = cur.fetchall()[0][0]

    query = "SELECT COUNT(*) FROM loan WHERE memberID =  '%s'" %(memIDInput.get())
    cur.execute(query)
    has_loan = cur.fetchall()[0][0]


    query = "SELECT COUNT(*) FROM fine WHERE memberID =  '%s'" %(memIDInput.get())
    cur.execute(query)
    has_fine = cur.fetchall()[0][0]

    query = "SELECT COUNT(*) FROM reservation WHERE accessionNum = '%s'" %(accessNumInput.get())
    cur.execute(query)
    has_reservation = cur.fetchall()[0][0]
    
    query = "SELECT (loanDate) FROM loan WHERE accessionNum =  '%s'" %(accessNumInput.get())
    cur.execute(query)
    book_loaned = cur.fetchall()
    
    if not member_exist:
        messagebox.showinfo("Error", "Member does not exist!")
        return
    elif not (book_exists):
        messagebox.showinfo("Error!", "Book does not exist!")
        return 

    elif (has_loan >= 2):
        messagebox.showinfo("Error!", "Member has existing loans!")
        return
    
    elif (has_fine):
        messagebox.showinfo("Error!", "Member has existing fines!")
        return

    elif (book_loaned):
        messagebox.showinfo("Error!", "Book currently on Loan until " + str(book_loaned[0][0]) + " for " + str(datetime.timedelta(days=14)))
        return False

    elif (has_reservation):
        messagebox.showinfo("Error!", "Book is reserved by others!")
        return

    else:
        root = Tk()
        root.title("Loan Book Page")
        root.geometry("1500x900")
        
        Canvas1 = Canvas(root)
        Canvas1.config(bg="#5F9EA0")
        Canvas1.pack(expand=True, fill=BOTH)

        LabelFrame = Frame(root, bg="black")
        LabelFrame.place(relx=0.1, rely=0.25, relwidth=0.8, relheight=0.6)

        headingFrame1 = Frame(root, bg="white", bd=5)
        headingFrame1.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.13)
        
        #add a leabel to heading Frame
        headingLabel = Label(headingFrame1, text="Please Confirm Loan Details \n Details to Be Correct:", bg="black", fg="white", font=('Courier',15))
        headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)


        query = "SELECT * FROM book WHERE accessionNum = '%s'" %(accessNumInput.get())
        cur.execute(query)
        book_details = cur.fetchall()[0]
        title = book_details[1]

        query = "SELECT * FROM member WHERE memberID = '%s'" %(memIDInput.get())
        cur.execute(query)
        member_details = cur.fetchall()[0]
        member_name = member_details[1]

        borrow_date = datetime.datetime.today().strftime('%Y-%m-%d')
        borrow_date = datetime.datetime.strptime(borrow_date, '%Y-%m-%d')
        return_date = borrow_date + datetime.timedelta(days=14)

        output1 = Label(LabelFrame, text="Accession Number ", bg="black", fg="white")
        output1.place(relx=0.15, rely=0.2)

        output1DOuput = Label(LabelFrame, text= accessNumInput.get(), bg="white", fg="black")
        output1DOuput.place(relx=0.3, rely=0.2, relwidth=0.62)
        
        output2 = Label(LabelFrame, text="Book Title ", bg="black", fg="white")
        output2.place(relx=0.15, rely=0.3)

        output2Output = Label(LabelFrame, text= title, bg="white", fg="black")
        output2Output.place(relx=0.3, rely=0.3, relwidth=0.62)
        
        output3 = Label(LabelFrame, text="Borrow Date ", bg="black", fg="white")
        output3.place(relx=0.15, rely=0.4)

        output3Output = Label(LabelFrame, text= str(borrow_date), bg="white", fg="black")
        output3Output.place(relx=0.3, rely=0.4, relwidth=0.62)
        
        output4 = Label(LabelFrame, text="Membership ID ", bg="black", fg="white")
        output4.place(relx=0.15, rely=0.5)

        output4Output = Label(LabelFrame, text= memIDInput.get(), bg="white", fg="black")
        output4Output.place(relx=0.3, rely=0.5, relwidth=0.62)
        
        output5 = Label(LabelFrame, text="Member Name ", bg="black", fg="white")
        output5.place(relx=0.15, rely=0.6)

        output5Output = Label(LabelFrame, text= member_name, bg="white", fg="black")
        output5Output.place(relx=0.3, rely=0.6, relwidth=0.62)

        output6 = Label(LabelFrame, text="Due Date ", bg="black", fg="white")
        output6.place(relx=0.15, rely=0.7)

        output6Output = Label(LabelFrame, text= str(return_date), bg="white", fg="black")
        output6Output.place(relx=0.3, rely=0.7, relwidth=0.62)
   

        submitBtn = Button(root, text="Confirm Loan", bg="lightblue", fg="black", command=confirm_loan)
        submitBtn.place(relx=0.28, rely=0.8, relwidth=0.18, relheight=0.08)

        quitBtn = Button(root, text="Back to Loan Page", bg="lightblue", fg="black", command=root.destroy)
        quitBtn.place(relx=0.53, rely=0.8, relwidth=0.18, relheight=0.08)
        root.mainloop()
        root.mainloop()
        return book_exists[0]


def confirm_loan():
    con = pymysql.connect(host = 'localhost', user = 'root', password = "yja9974533", db = "library")
    cur = con.cursor()

    access_num = accessNumInput.get()
    member_id = memIDInput.get()


    date_today = str(datetime.datetime.date(datetime.datetime.now()))
    query = "INSERT INTO loan(accessionNum, memberID, loandate) VALUES('%s', '%s', '%s')" %(access_num, member_id, date_today)
    cur.execute(query)
    con.commit()

    query = "SELECT COUNT(*) FROM reservation WHERE memberID = '%s'" %(member_id)
    cur.execute(query)
    has_reservation = cur.fetchall()[0][0]
    if (has_reservation):
        query = "DELETE FROM reservation WHERE memberID = '%s'" %(member_id)
        cur.execute(query)
        con.commit()
    messagebox.showinfo("Success!", "Book has been borrowed!")

def returnBook():
    global accessNumInput, returnDateInput, con, cur, root
    root = Tk()
    root.title("Return Page")
    root.geometry("1500x900")
    
    Canvas1 = Canvas(root)
    Canvas1.config(bg="#5F9EA0")
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root, bg="white", bd=5)
    headingFrame1.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.13)
    
    #add a leabel to heading Frame
    headingLabel = Label(headingFrame1, text="To Return a Book \n Please Enter Information Below:", bg="black", fg="white", font=('Courier',15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    #add a label frame to canvas to give a lebl insite it to delete book
    LabelFrame = Frame(root, bg="black")
    LabelFrame.place(relx=0.1, rely=0.25, relwidth=0.8, relheight=0.6)

    #take in inputs
    accessNum = Label(LabelFrame, text="Accession Number ", bg="black", fg="white")
    accessNum.place(relx=0.05, rely=0.3)

    accessNumInput = Entry(LabelFrame)
    accessNumInput.place(relx=0.3, rely=0.3, relwidth=0.62)
    
    returnDate = Label(LabelFrame, text="Return Date ", bg="black", fg="white")
    returnDate.place(relx=0.05, rely=0.4)

    returnDateInput = Entry(LabelFrame)
    returnDateInput.place(relx=0.3, rely=0.4, relwidth=0.62)

    #submit button    
    submitBtn = Button(root, text="Return Book", bg="lightblue", fg="black", command = return_book )
    submitBtn.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)

    quitBtn = Button(root, text="Back to Loan Menu", bg="lightblue", fg="black", command=root.destroy)
    quitBtn.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)

    root.mainloop()


def return_book():
    global con, cur, root, accessNumInput, member_id, returnDateInput
    con = pymysql.connect(host = 'localhost', user = 'root', password = "Jiajie98108967", db = "library")
    cur = con.cursor()

    access_num = accessNumInput.get()
    return_date = returnDateInput.get()

    query = f'SELECT COUNT(*) FROM loan WHERE accessionNum = "{access_num}"'
    cur.execute(query)
    num_books = cur.fetchall()[0][0]

    format = '%Y-%m-%d'
    if not (num_books):
        messagebox.showinfo("Error!", "Book is not loaned!")
        return
    try:
        datetime.datetime.strptime(return_date, format)
    except ValueError:
        messagebox.showinfo("Error!", "Please input in YYYY-MM-DD Format")

    query = "SELECT (loanDate) FROM loan WHERE accessionNum = '%s'" %(access_num)
    cur.execute(query)
    loan_date = cur.fetchall()[0][0] + datetime.timedelta(days=14)
    loan_date = datetime.datetime.combine(loan_date, datetime.datetime.min.time())

    query = "SELECT memberID, loanID FROM loan WHERE accessionNum = '%s'" %(access_num)
    cur.execute(query)
    member_id = cur.fetchall()[0][0]
    cur.execute(query)
    loan_id = cur.fetchall()[0][1]


    return_date = datetime.datetime.strptime(return_date, format)

    fine_amount = 0

    if (loan_date < return_date):
        seconds_difference = (return_date - loan_date).total_seconds()
        fine_amount = seconds_difference / 86400
        
    query = 'SELECT title FROM loan LEFT JOIN book USING (accessionNum)'
    cur.execute(query)
    book_title = cur.fetchall()[0][0]

    query = 'SELECT name FROM loan LEFT JOIN member USING (memberID) '
    cur.execute(query)
    member_name = cur.fetchall()[0][0]


    root = Tk()
    root.title("Return Page")
    root.geometry("1500x900")
    
    Canvas1 = Canvas(root)
    Canvas1.config(bg="#5F9EA0")
    Canvas1.pack(expand=True, fill=BOTH)

    LabelFrame = Frame(root, bg="black")
    LabelFrame.place(relx=0.1, rely=0.25, relwidth=0.8, relheight=0.6)

    headingFrame1 = Frame(root, bg="white", bd=5)
    headingFrame1.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.13)
    
    #add a leabel to heading Frame
    headingLabel = Label(headingFrame1, text="Confirm Details \n To be correct:", bg="black", fg="white", font=('Courier',15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    accessionNum = Label(LabelFrame, text="Accession Number ", bg="black", fg="white")
    accessionNum.place(relx=0.15, rely=0.2)

    accessionNumOuput = Label(LabelFrame, text= access_num, bg="white", fg="black")
    accessionNumOuput.place(relx=0.3, rely=0.2, relwidth=0.62)

    bookTitle = Label(LabelFrame, text="Book Title ", bg="black", fg="white")
    bookTitle.place(relx=0.15, rely=0.3)

    bookTitleOuput = Label(LabelFrame, text= book_title, bg="white", fg="black")
    bookTitleOuput.place(relx=0.3, rely=0.3, relwidth=0.62)
#
    memberID = Label(LabelFrame, text="Membership ID ", bg="black", fg="white")
    memberID.place(relx=0.15, rely=0.4)

    memberIDOuput = Label(LabelFrame, text= member_id, bg="white", fg="black")
    memberIDOuput.place(relx=0.3, rely=0.4, relwidth=0.62)

    memberName = Label(LabelFrame, text="Member Name ", bg="black", fg="white")
    memberName.place(relx=0.15, rely=0.5)

    memberNameOuput = Label(LabelFrame, text= member_name, bg="white", fg="black")
    memberNameOuput.place(relx=0.3, rely=0.5, relwidth=0.62)

    returnDate = Label(LabelFrame, text="Return Date ", bg="black", fg="white")
    returnDate.place(relx=0.15, rely=0.6)

    returnDateOuput = Label(LabelFrame, text= return_date.strftime('%Y-%m-%d'), bg="white", fg="black")
    returnDateOuput.place(relx=0.3, rely=0.6, relwidth=0.62)

    fineAmount = Label(LabelFrame, text="Fine Amount ", bg="black", fg="white")
    fineAmount.place(relx=0.15, rely=0.7)

    fineAmountOuput = Label(LabelFrame, text= fine_amount, bg="white", fg="black")
    fineAmountOuput.place(relx=0.3, rely=0.7, relwidth=0.62)


    submitBtn = Button(root, text="Confirm Payment", bg="lightblue", fg="black", command=confirm)
    submitBtn.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)

    quitBtn = Button(root, text="Back to Payment Menu", bg="lightblue", fg="black", command=root.destroy)
    quitBtn.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)
    root.mainloop()
    

def confirm():
    access_num = accessNumInput.get()
    return_date = returnDateInput.get()

    query = f'SELECT COUNT(*) FROM loan WHERE accessionNum = "{access_num}"'
    cur.execute(query)
    num_books = cur.fetchall()[0][0]

    format = '%Y-%m-%d'
    if not (num_books):
        messagebox.showinfo("Error!", "Book is not loaned!")
        return
    try:
        datetime.datetime.strptime(return_date, format)
    except ValueError:
        messagebox.showinfo("Error!", "Please input in YYYY-MM-DD Format")

    query = "SELECT (loanDate) FROM loan WHERE accessionNum = '%s'" %(access_num)
    cur.execute(query)
    loan_date = cur.fetchall()[0][0] + datetime.timedelta(days=14)
    loan_date = datetime.datetime.combine(loan_date, datetime.datetime.min.time())

    query = "SELECT memberID, loanID FROM loan WHERE accessionNum = '%s'" %(access_num)
    cur.execute(query)
    member_id = cur.fetchall()[0][0]
    cur.execute(query)
    loan_id = cur.fetchall()[0][1]


    return_date = datetime.datetime.strptime(return_date, format)

    fine_amount = 0

    if (loan_date < return_date):
        seconds_difference = (return_date - loan_date).total_seconds()
        fine_amount = seconds_difference / 86400
        query = 'SELECT (fineAmount) FROM fine WHERE memberID = "%s"' %(member_id)
        cur.execute(query)
        

        member_fine = cur.fetchall()
        if (member_fine):
            fine_amount += member_fine[0][0]
            query = "UPDATE fine SET fineAmount = '%d' WHERE memberID = '%s'" %(fine_amount, member_id)
            cur.execute(query)
            con.commit()
        else:
            query = "INSERT INTO Fine(memberID, fineAmount) VALUES('%s', '%d')" %(member_id, fine_amount)
            cur.execute(query)
            con.commit()

    query = "DELETE from loan WHERE accessionNum = '%s'" %(accessNumInput.get())
    cur.execute(query)
    con.commit()

    if fine_amount:
        messagebox.showinfo("Error!", "Book returned successfully but has fines.")
        return
    messagebox.showinfo("Success!", "Book has been returned.")
    root.withdraw()
