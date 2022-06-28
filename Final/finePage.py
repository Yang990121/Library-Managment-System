from tkinter import *
from PIL import ImageTk,Image
from matplotlib.pyplot import text, title #PIL -> Pillow
import pymysql
from tkinter import messagebox

def finePage():
    root = Tk()
    root.title("Book Page")
    new_var = ("1800x900")
    root.geometry(new_var)
    
    Canvas1 = Canvas(root)
    Canvas1.config(bg="Slateblue1")
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root, bg="white", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

    headingLabel = Label(headingFrame1, text="Select one of the Option Below:", bg="black", fg="white", font=('Courier',15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)
    
    fbtn1 = Button(root, text="10. Payment: Fine Payment", bg="white", fg="black", command=finePayment)
    fbtn1.place(relx=0.28, rely=0.3, relwidth=0.45, relheight=0.1)

    quitBtn = Button(root,text="Back to Main Menu",bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.28,rely=0.9, relwidth=0.45,relheight=0.1)

def finePayment():
    global memIDInput, paymentDateInput, paymentAmountInput, con, cur, root
    root = Tk()
    root.title("Reservation Page")
    root.geometry("1500x900")
    
    Canvas1 = Canvas(root)
    Canvas1.config(bg="Slateblue1")
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root, bg="white", bd=5)
    headingFrame1.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.13)
    
    #add a leabel to heading Frame
    headingLabel = Label(headingFrame1, text="To Pay a Fine \n Please Enter Information Below:", bg="black", fg="white", font=('Courier',15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    #add a label frame to canvas to give a lebl insite it to delete book
    LabelFrame = Frame(root, bg="black")
    LabelFrame.place(relx=0.1, rely=0.25, relwidth=0.8, relheight=0.6)

    #take in inputs
    memID = Label(LabelFrame, text="Membership ID ", bg="black", fg="white")
    memID.place(relx=0.05, rely=0.4)

    memIDInput = Entry(LabelFrame)
    memIDInput.place(relx=0.3, rely=0.4, relwidth=0.62)
    
    paymentDate = Label(LabelFrame, text="Payment Date ", bg="black", fg="white")
    paymentDate.place(relx=0.05, rely=0.5)

    paymentDateInput = Entry(LabelFrame)
    paymentDateInput.place(relx=0.3, rely=0.5, relwidth=0.62)
    
    paymentAmount = Label(LabelFrame, text="Payment Amount ", bg="black", fg="white")
    paymentAmount.place(relx=0.05, rely=0.6)

    paymentAmountInput = Entry(LabelFrame)
    paymentAmountInput.place(relx=0.3, rely=0.6, relwidth=0.62)

    #submit button    
    submitBtn = Button(root, text="Pay Fine", bg="lightblue", fg="black", command=pay_fine)
    submitBtn.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)

    quitBtn = Button(root, text="Back to Fine Menu", bg="lightblue", fg="black", command=root.destroy)
    quitBtn.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)

    root.mainloop()

def pay_fine():
    memberID = memIDInput.get()
    amount = paymentAmountInput.get()
    payment_date = paymentDateInput.get()

    try:
        int(amount)
    except:
        messagebox.showinfo("Error", "Invalid Amount")

    amount = int(amount)

    con = pymysql.connect(host = 'localhost', user = 'root', password = "yja9974533", db = "library")
    cur = con.cursor()

    memberQuery = f'SELECT COUNT(*) FROM member WHERE memberID = "{memberID}"'
    cur.execute(memberQuery)
    if cur.fetchall()[0][0] == 0:
        messagebox.showinfo("Error", "Invalid member ID")
        return
    
    fineQuery = f'SELECT fineAmount FROM fine WHERE memberID = "{memberID}"'
    cur.execute(fineQuery)
    try:
        fine = cur.fetchall()[0][0]
    except IndexError:
        messagebox.showinfo("Error", "Member has no outstanding fines")
        return
    if amount != fine:
        messagebox.showinfo("Error", "Payment is not equal to fine amount")
        return
    else:
        
        root = Tk()
        root.title("Borrow Page")
        root.geometry("1000x900")
        
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

        paymentdue = Label(LabelFrame, text="Payment Due ", bg="black", fg="white")
        paymentdue.place(relx=0.15, rely=0.2)

        paymentdueOuput = Label(LabelFrame, text= str(amount), bg="white", fg="black")
        paymentdueOuput.place(relx=0.3, rely=0.2, relwidth=0.62)
        
        memID = Label(LabelFrame, text="Member ID ", bg="black", fg="white")
        memID.place(relx=0.15, rely=0.3)

        memIDOutput = Label(LabelFrame, text= memberID, bg="white", fg="black")
        memIDOutput.place(relx=0.3, rely=0.3, relwidth=0.62)
        
        paymentDate = Label(LabelFrame, text="Payment Date ", bg="black", fg="white")
        paymentDate.place(relx=0.15, rely=0.4)

        paymentDateOutput = Label(LabelFrame, text= payment_date, bg="white", fg="black")
        paymentDateOutput.place(relx=0.3, rely=0.4, relwidth=0.62)
        
        Exact = Label(LabelFrame, text="Exact Fee Only", bg="black", fg="white")
        Exact.place(relx=0.45, rely=0.5)

        submitBtn = Button(root, text="Confirm Payment", bg="lightblue", fg="black", command=confirm)
        submitBtn.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)

        quitBtn = Button(root, text="Back to Payment Menu", bg="lightblue", fg="black", command=root.destroy)
        quitBtn.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)
        root.mainloop()

def confirm():
    root = Tk()
    con = pymysql.connect(host = 'localhost', user = 'root', password = "yja9974533", db = "library")
    cur = con.cursor()
    query = f'DELETE FROM fine WHERE memberID = "{memIDInput.get()}"'
    cur.execute(query)
    con.commit()
    messagebox.showinfo("Successful", "Fine payment paid")
    root.destroy()




    