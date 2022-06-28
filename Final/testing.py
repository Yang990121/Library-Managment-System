create schema library;
use library;
CREATE TABLE member (
  memberID varchar(255) NOT NULL UNIQUE,
  name varchar(255) NOT NULL,
  faculty varchar(255) NOT NULL,
  phoneNumber int NOT NULL UNIQUE,
  email varchar(255) NOT NULL UNIQUE,
  PRIMARY KEY (memberID)
) ;

INSERT INTO member(memberID, name, faculty, phoneNumber, email) VALUES
('A101A', 'Hermione Granger', 'Science' , 33336663, 'flying@als.edu'),
('A201B', 'Sherlock Holmes', 'Law', 44327676, 'elementarydrw@als.edu'),
('A301C', 'Tintin', 'Engineering', 14358788, 'luvmilu@als.edu'),
('A401D', 'Prinche Hamlet', 'FASS', 16091609, 'tobeornot@als.edu');

CREATE TABLE book (
 accessionNum varchar(255) NOT NULL UNIQUE,
    title varchar(255) NOT NULL,
    authors varchar(255) NOT NULL,
    isbn bigint NOT NULL,
    publisher varchar(255) NOT NULL,
    year int NOT NULL,
    PRIMARY KEY (accessionNum)
);

INSERT INTO book(accessionNum, title, authors, isbn, publisher, year) VALUES
('A01', 'A 1984 Story', 'George Orwell,,', 9790000000001, 'Intra S.r.l.s.', 2021),
('A02', '100 anos de soledad', 'Gabriel Garcia Marquez,,', 9790000000002, 'Vintage Espanol', 2017),
('A03', 'Brave New World', 'Aldous Huxley,,', 9790000000003, 'Harper Perennial', 2006);
INSERT INTO book(accessionNum, title, authors, isbn, publisher, year) VALUES
('A04', 'mygod', 'fuck', 9790000000004, 'Harping', 2009);

CREATE TABLE reservation (
 reservationID int NOT NULL UNIQUE AUTO_INCREMENT,
	accessionNum varchar(255) NOT NULL UNIQUE,
    memberID varchar(255) NOT NULL,
    ReservationDate date NOT NULL,
    PRIMARY KEY (reservationID),
	FOREIGN KEY (accessionNum) REFERENCES book(accessionNum),
    FOREIGN KEY (memberID) REFERENCES member(memberID)
);

CREATE TABLE loan (
 loanID int NOT NULL UNIQUE AUTO_INCREMENT,
	accessionNum varchar(255) NOT NULL UNIQUE,
    memberID varchar(255) NOT NULL,
    loanDate date NOT NULL,
    PRIMARY KEY (loanID),
    FOREIGN KEY (memberID) REFERENCES member(memberID),
    FOREIGN KEY (accessionNum) REFERENCES book(accessionNum)
);

CREATE TABLE fine (
 fineID int NOT NULL UNIQUE AUTO_INCREMENT,
	memberID varchar(255) NOT NULL UNIQUE,
    fineAmount int NOT NULL,
    PRIMARY KEY (fineID),
    FOREIGN KEY (loanID) REFERENCES loan(loanID),
    FOREIGN KEY (memberID) REFERENCES member(memberID)
);