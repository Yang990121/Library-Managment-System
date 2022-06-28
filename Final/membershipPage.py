from sqlite3 import Cursor
from tkinter import *
from PIL import ImageTk,Image
from numpy import number #PIL -> Pillow
import pymysql
from tkinter import messagebox

from sqlalchemy import null

# Main membership page
def membershipPage():
    root = Tk()
    root.title("Membership Page")
    root.geometry("1500x900")
    
    Canvas1 = Canvas(root)
    Canvas1.config(bg="goldenrod")
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root, bg="white", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)
    
    #add a leabel to heading Frame
    headingLabel = Label(headingFrame1, text="Select one of the Option Below:", bg="black", fg="white", font=('Courier',15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    mbtn1 = Button(root, text="1. Creation: Membership creation", bg="white", fg="black", command=createMem)
    mbtn1.place(relx=0.28, rely=0.3, relwidth=0.45, relheight=0.1)
    
    mbtn2 = Button(root, text="2. Deletion: Membership deletion", bg="white", fg="black", command=deleteMem)
    mbtn2.place(relx=0.28, rely=0.4, relwidth=0.45, relheight=0.1)
    
    mbtn3 = Button(root, text="3. Update Membership update", bg="white", fg="black", command=updateMem)
    mbtn3.place(relx=0.28, rely=0.5, relwidth=0.45, relheight=0.1)

    quitBtn = Button(root,text="Back to Main Menu",bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.28,rely=0.9, relwidth=0.45,relheight=0.1)

# Create Membership Page
def createMem():
    global memberIDinput, nameInput, facultyInput, phoneInput, emailInput, con, cur, root
    root = Tk()
    root.title("Creation Page")
    root.geometry("1500x900")
    
    Canvas1 = Canvas(root)
    Canvas1.config(bg="goldenrod")
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root, bg="white", bd=5)
    headingFrame1.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.13)
    
    #add a leabel to heading Frame
    headingLabel = Label(headingFrame1, text="To Create Member \n Please Enter Requested Information Below:", bg="black", fg="white", font=('Courier',15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    #add a label frame to canvas to give a lebl insite it to delete book
    LabelFrame = Frame(root, bg="black")
    LabelFrame.place(relx=0.1, rely=0.25, relwidth=0.8, relheight=0.6)

    #take in inputs
    memberID = Label(LabelFrame, text="Membership ID ", bg="black", fg="white")
    memberID.place(relx=0.05, rely=0.3)

    memberIDinput = Entry(LabelFrame)
    memberIDinput.place(relx=0.3, rely=0.3, relwidth=0.62)
    
    name = Label(LabelFrame, text="Name ", bg="black", fg="white")
    name.place(relx=0.05, rely=0.4)

    nameInput = Entry(LabelFrame)
    nameInput.place(relx=0.3, rely=0.4, relwidth=0.62)
    
    faculty = Label(LabelFrame, text="Faculty ", bg="black", fg="white")
    faculty.place(relx=0.05, rely=0.5)

    facultyInput = Entry(LabelFrame)
    facultyInput.place(relx=0.3, rely=0.5, relwidth=0.62)
    
    phone = Label(LabelFrame, text="Phone Number ", bg="black", fg="white")
    phone.place(relx=0.05, rely=0.6)

    phoneInput = Entry(LabelFrame)
    phoneInput.place(relx=0.3, rely=0.6, relwidth=0.62)
    
    email = Label(LabelFrame, text="Email ", bg="black", fg="white")
    email.place(relx=0.05, rely=0.7)

    emailInput = Entry(LabelFrame)
    emailInput.place(relx=0.3, rely=0.7, relwidth=0.62)

    #submit button    
    submitBtn = Button(root, text="Create Member", bg="lightblue", fg="black", command=signup)
    submitBtn.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)

    quitBtn = Button(root, text="Back to \n Membership Menu", bg="lightblue", fg="black", command=root.destroy)
    quitBtn.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)

    root.mainloop()

# Create deletion page
def deleteMem():
    global memberIDinput, nameInput, facultyInput, phoneInput, emailInput, con, cur, root
    root = Tk()
    root.title("Delete Page")
    root.geometry("1500x900")
    
    Canvas1 = Canvas(root)
    Canvas1.config(bg="goldenrod")
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root, bg="white", bd=5)
    headingFrame1.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.13)
    
    #add a leabel to heading Frame
    headingLabel = Label(headingFrame1, text="To Delete Member \n Please Enter Membership ID:", bg="black", fg="white", font=('Courier',15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    #add a label frame to canvas to give a lebl insite it to delete book
    LabelFrame = Frame(root, bg="black")
    LabelFrame.place(relx=0.1, rely=0.25, relwidth=0.8, relheight=0.6)

    #take in inputs
    memberID = Label(LabelFrame, text="Membership ID ", bg="black", fg="white")
    memberID.place(relx=0.05, rely=0.3)

    memberIDinput = Entry(LabelFrame)
    memberIDinput.place(relx=0.3, rely=0.3, relwidth=0.62)

    #submit button    
    submitBtn = Button(root, text="Delete Member", bg="lightblue", fg="black", command=remove_member)
    submitBtn.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)

    quitBtn = Button(root, text="Back to \n Membership Menu", bg="lightblue", fg="black", command=root.destroy)
    quitBtn.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)

    root.mainloop()

# Create Update page
def updateMem():
    global memberIDinput, nameInput, facultyInput, phoneInput, emailInput
    root = Tk()
    root.title("Update Membership Page")
    root.geometry("1500x900")
    
    Canvas1 = Canvas(root)
    Canvas1.config(bg="goldenrod")
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root, bg="white", bd=5)
    headingFrame1.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.13)
    
    #add a leabel to heading Frame
    headingLabel = Label(headingFrame1, text="To Update Member \n Please Enter Membership ID:", bg="black", fg="white", font=('Courier',15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    #add a label frame to canvas to give a lebl insite it to delete book
    LabelFrame = Frame(root, bg="black")
    LabelFrame.place(relx=0.1, rely=0.25, relwidth=0.8, relheight=0.6)

    #take in inputs
    memberID = Label(LabelFrame, text="Membership ID ", bg="black", fg="white")
    memberID.place(relx=0.05, rely=0.3)

    memberIDinput = Entry(LabelFrame)
    memberIDinput.place(relx=0.3, rely=0.3, relwidth=0.62)


    #submit button    
    submitBtn = Button(root, text="Update Member", bg="lightblue", fg="black", command=updateInfo)
    submitBtn.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)

    quitBtn = Button(root, text="Back to \n Membership Menu", bg="lightblue", fg="black", command=root.destroy)
    quitBtn.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)

    root.mainloop()


def updateInfo():
    global memberIDinput, nameInput, facultyInput, phoneInput, emailInput
    root = Tk()
    root.title("Member information")
    root.geometry("1500x900")
    
    Canvas1 = Canvas(root)
    Canvas1.config(bg="goldenrod")
    Canvas1.pack(expand=True, fill=BOTH)

    con = pymysql.connect(host = 'localhost', user = 'root', password = "yja9974533", db = "library")
    cur = con.cursor()

    query = "SELECT * FROM member WHERE memberID = '%s'" %(memberIDinput.get())
    cur.execute(query)
    member_exist = cur.fetchall()

    if not (member_exist):
        messagebox.showinfo("Error!", "Member does not exist!")
        root.destroy()

    headingFrame1 = Frame(root, bg="white", bd=5)
    headingFrame1.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.13)
    
    #add a leabel to heading Frame
    headingLabel = Label(headingFrame1, text="Please Enter Requested Information Below", bg="black", fg="white", font=('Courier',15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    #add a label frame to canvas to give a lebl insite it to delete book
    LabelFrame = Frame(root, bg="black")
    LabelFrame.place(relx=0.1, rely=0.25, relwidth=0.8, relheight=0.6)

    #take in inputs
    memberID = Label(LabelFrame, text="Membership ID ", bg="black", fg="white")
    memberID.place(relx=0.05, rely=0.3)

    memberIDoutput = Label(LabelFrame, text= memberIDinput.get(), bg="white", fg="black")
    memberIDoutput.place(relx=0.3, rely=0.3, relwidth=0.62)

    # memberIDinput = Entry(LabelFrame)
    # memberIDinput.place(relx=0.3, rely=0.3, relwidth=0.62)
    
    name = Label(LabelFrame, text="Name ", bg="black", fg="white")
    name.place(relx=0.05, rely=0.4)

    nameInput = Entry(LabelFrame)
    nameInput.place(relx=0.3, rely=0.4, relwidth=0.62)
    
    faculty = Label(LabelFrame, text="Faculty ", bg="black", fg="white")
    faculty.place(relx=0.05, rely=0.5)

    facultyInput = Entry(LabelFrame)
    facultyInput.place(relx=0.3, rely=0.5, relwidth=0.62)
    
    phone = Label(LabelFrame, text="Phone Number ", bg="black", fg="white")
    phone.place(relx=0.05, rely=0.6)

    phoneInput = Entry(LabelFrame)
    phoneInput.place(relx=0.3, rely=0.6, relwidth=0.62)
    
    email = Label(LabelFrame, text="Email ", bg="black", fg="white")
    email.place(relx=0.05, rely=0.7)

    emailInput = Entry(LabelFrame)
    emailInput.place(relx=0.3, rely=0.7, relwidth=0.62)

    #submit button    
    submitBtn = Button(root, text="Update Member", bg="lightblue", fg="black", command=update_member)
    submitBtn.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)

    quitBtn = Button(root, text="Back to \n Update Menu", bg="lightblue", fg="black", command=root.destroy)
    quitBtn.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)

    
def signup():
    member_id = memberIDinput.get()
    name = nameInput.get()
    faculty = facultyInput.get()
    phone_number = phoneInput.get()
    email = emailInput.get()

    if (member_id == "" or name == "" or faculty == "" or phone_number == "" or email == ""):
        messagebox.showinfo("Error!", "Missing or incomplete fields!")
        return

    con = pymysql.connect(host = 'localhost', user = 'root', password = "yja9974533", db = "library")
    cur = con.cursor()

    query = "SELECT COUNT(*) FROM member WHERE memberID = '%s'" %(member_id)
    cur.execute(query)

    member_exist = cur.fetchall()[0][0]
    if (member_exist):
        messagebox.showinfo("Error", "Member already exists!")
        return

    query ="INSERT INTO member VALUES ('%s', '%s', '%s', '%s', '%s')" %(member_id, name, faculty, phone_number, email)
    cur.execute(query)
    con.commit()
    messagebox.showinfo("Success", "Member added successfully!")
    root.destroy

def remove_member():
    global con, cur, root
    con = pymysql.connect(host = 'localhost', user = 'root', password = "yja9974533", db = "library")
    cur = con.cursor()

    member_id = memberIDinput.get()

    query = "SELECT COUNT(*) FROM member WHERE memberID = '%s'" %(member_id)
    cur.execute(query)
    member_exist = cur.fetchall()[0][0]

    query2 = "SELECT COUNT(*) FROM reservation WHERE memberID = '%s'" %(member_id)
    cur.execute(query2)
    has_reservation = cur.fetchall()[0][0]

    query3 = "SELECT COUNT(*) FROM fine WHERE memberID =  '%s'" %(member_id)
    cur.execute(query3)
    has_fine = cur.fetchall()[0][0]

    query4 = "SELECT COUNT(*) FROM loan WHERE memberID = '%s'" %(member_id)
    cur.execute(query4)
    has_loan = cur.fetchall()[0][0]

    if not member_exist:
        messagebox.showinfo("Error", "Member does not exist!")
        return
    elif (has_reservation):
        messagebox.showinfo("Error", "Member has reservations!")
        return
    elif (has_fine):
        messagebox.showinfo("Error", "Member has fines!")
        return
    elif (has_loan):
        messagebox.showinfo("Error", "Member has loans!")
        return
    else:
        root = Tk()
        root.title("Remove Page")
        root.geometry("1000x900")
        
        Canvas1 = Canvas(root)
        Canvas1.config(bg="#5F9EA0")
        Canvas1.pack(expand=True, fill=BOTH)

        LabelFrame = Frame(root, bg="black")
        LabelFrame.place(relx=0.1, rely=0.25, relwidth=0.8, relheight=0.6)

        headingFrame1 = Frame(root, bg="white", bd=5)
        headingFrame1.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.13)
        
        #add a leabel to heading Frame
        headingLabel = Label(headingFrame1, text="Please Confirm Delete \n Details to Be Correct:", bg="black", fg="white", font=('Courier',15))
        headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

        memberID = Label(LabelFrame, text="Member ID ", bg="black", fg="white")
        memberID.place(relx=0.15, rely=0.2)

        memberIDOuput = Label(LabelFrame, text= member_id, bg="white", fg="black")
        memberIDOuput.place(relx=0.3, rely=0.2, relwidth=0.62)
        
        output2 = Label(LabelFrame, text="Name ", bg="black", fg="white")
        output2.place(relx=0.15, rely=0.3)

        query = "SELECT * FROM member WHERE memberID = '%s'" %(memberIDinput.get())
        cur.execute(query)
        member_details = cur.fetchall()[0]
        name = member_details[1]
        faculty = member_details[2]
        phone_number = member_details[3]
        email = member_details[4]

        output2Output = Label(LabelFrame, text= name, bg="white", fg="black")
        output2Output.place(relx=0.3, rely=0.3, relwidth=0.62)
        
        output3 = Label(LabelFrame, text="Faculty ", bg="black", fg="white")
        output3.place(relx=0.15, rely=0.4)

        output3Output = Label(LabelFrame, text= faculty, bg="white", fg="black")
        output3Output.place(relx=0.3, rely=0.4, relwidth=0.62)
        
        output4 = Label(LabelFrame, text="Phone Number ", bg="black", fg="white")
        output4.place(relx=0.15, rely=0.5)

        output4Output = Label(LabelFrame, text= str(phone_number), bg="white", fg="black")
        output4Output.place(relx=0.3, rely=0.5, relwidth=0.62)
        
        output5 = Label(LabelFrame, text="Email Address ", bg="black", fg="white")
        output5.place(relx=0.15, rely=0.6)

        output5Output = Label(LabelFrame, text= email, bg="white", fg="black")
        output5Output.place(relx=0.3, rely=0.6, relwidth=0.62)
   

        submitBtn = Button(root, text="Delete Member", bg="lightblue", fg="black", command=confirm_delete)
        submitBtn.place(relx=0.28, rely=0.7, relwidth=0.18, relheight=0.08)

        quitBtn = Button(root, text="Back to Membership Menu", bg="lightblue", fg="black", command=root.destroy)
        quitBtn.place(relx=0.53, rely=0.7, relwidth=0.18, relheight=0.08)
        root.mainloop()

    

def confirm_delete():
    root = Tk()
    query = "DELETE from member WHERE memberID = '%s'" %(memberIDinput.get())
    cur.execute(query)
    con.commit()
    messagebox.showinfo("Success", "Member has been deleted!")
    root.withdraw()
    return True



def update_member():
    con = pymysql.connect(host = 'localhost', user = 'root', password = "yja9974533", db = "library")
    cur = con.cursor()
    member_id = memberIDinput.get()
    name = nameInput.get()
    faculty = facultyInput.get()
    phone_number = phoneInput.get()
    email = emailInput.get()

    if (member_id == "" or name == "" or faculty == "" or phone_number == "" or email == ""):
        messagebox.showinfo("Error", "Missing/Incomplete Details")
        return False
    query = "SELECT * FROM member WHERE memberID = '%s'" %(member_id)
    cur.execute(query)
    member_exist = cur.fetchall()
    if not (member_exist):
        messagebox.showinfo("Error!", "Member does not exist!")
        return False
    else:
        root = Tk()
        root.title("Update Page")
        root.geometry("1000x900")
        
        Canvas1 = Canvas(root)
        Canvas1.config(bg="#5F9EA0")
        Canvas1.pack(expand=True, fill=BOTH)

        LabelFrame = Frame(root, bg="black")
        LabelFrame.place(relx=0.1, rely=0.25, relwidth=0.8, relheight=0.6)

        headingFrame1 = Frame(root, bg="white", bd=5)
        headingFrame1.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.13)
        
        #add a leabel to heading Frame
        headingLabel = Label(headingFrame1, text="Please Confirm Update \n Details to Be Correct:", bg="black", fg="white", font=('Courier',15))
        headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

        memberID = Label(LabelFrame, text="Member ID ", bg="black", fg="white")
        memberID.place(relx=0.15, rely=0.2)

        memberIDOuput = Label(LabelFrame, text= member_id, bg="white", fg="black")
        memberIDOuput.place(relx=0.3, rely=0.2, relwidth=0.62)
        
        output2 = Label(LabelFrame, text="Name ", bg="black", fg="white")
        output2.place(relx=0.15, rely=0.3)

        output2Output = Label(LabelFrame, text= name, bg="white", fg="black")
        output2Output.place(relx=0.3, rely=0.3, relwidth=0.62)
        
        output3 = Label(LabelFrame, text="Faculty ", bg="black", fg="white")
        output3.place(relx=0.15, rely=0.4)

        output3Output = Label(LabelFrame, text= faculty, bg="white", fg="black")
        output3Output.place(relx=0.3, rely=0.4, relwidth=0.62)
        
        output4 = Label(LabelFrame, text="Phone Number ", bg="black", fg="white")
        output4.place(relx=0.15, rely=0.5)

        output4Output = Label(LabelFrame, text= str(phone_number), bg="white", fg="black")
        output4Output.place(relx=0.3, rely=0.5, relwidth=0.62)
        
        output5 = Label(LabelFrame, text="Email Address ", bg="black", fg="white")
        output5.place(relx=0.15, rely=0.6)

        output5Output = Label(LabelFrame, text= email, bg="white", fg="black")
        output5Output.place(relx=0.3, rely=0.6, relwidth=0.62)
   

        submitBtn = Button(root, text="Update Member", bg="lightblue", fg="black", command=confirm_update)
        submitBtn.place(relx=0.28, rely=0.7, relwidth=0.18, relheight=0.08)

        quitBtn = Button(root, text="Back to Membership Menu", bg="lightblue", fg="black", command=root.destroy)
        quitBtn.place(relx=0.53, rely=0.7, relwidth=0.18, relheight=0.08)
        root.mainloop()

def confirm_update():
    root = Tk()
    con = pymysql.connect(host = 'localhost', user = 'root', password = "yja9974533", db = "library")
    cur = con.cursor()
    member_id = memberIDinput.get()
    name = nameInput.get()
    faculty = facultyInput.get()
    phone_number = phoneInput.get()
    email = emailInput.get()
    query = "UPDATE member SET memberID = '%s', name = '%s', faculty = '%s', phoneNumber = '%s', email = '%s' WHERE memberID = '%s'" %(member_id, name, faculty, phone_number, email, member_id)
    cur.execute(query)
    con.commit()
    messagebox.showinfo("Successful", "Details Updated")
    root.withdraw()
    return True