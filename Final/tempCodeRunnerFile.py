def display_books_on_loan(): 
    query = "SELECT book.accessionNum, title, authors, isbn, publisher, year FROM book INNER JOIN Loan USING(accessionNum)" 
    cursor.execute(query) 
    print(cursor.fetchall())