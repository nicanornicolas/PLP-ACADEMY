-- Drop the database if it already exists to ensure a fresh start.
DROP DATABASE IF EXISTS LibraryDB;

-- Create the new database.
CREATE DATABASE LibraryDB;

-- Select the database to use for the subsequent commands.
USE LibraryDB;

/*
Table: Genres
Purpose: Stores book categories.
Relationship: One Genre can have many Books.
*/

CREATE TABLE Genres (
    GenreID INT AUTO_INCREMENT PRIMARY KEY,
    GenreName VARCHAR(100) NOT NULL UNIQUE,
    Description TEXT
);


/*
Table: Authors
Purpose: Stores information about book authors.
Relationship: An Author can write many Books (via BookAuthors).
*/

CREATE TABLE Authors (
    AuthorID INT AUTO_INCREMENT PRIMARY KEY,
    FirstName VARCHAR(100) NOT NULL,
    LastName VARCHAR(100) NOT NULL,
    BirthDate DATE
);


/*
Table: Members
Purpose: Stores information about library members.
Relationship: One Member can have many Loans.
*/
CREATE TABLE Members (
    MemberID INT AUTO_INCREMENT PRIMARY KEY,
    FirstName VARCHAR(100) NOT NULL,
    LastName VARCHAR(100) NOT NULL,
    Email VARCHAR(255) NOT NULL UNIQUE,
    PhoneNumber VARCHAR(20),
    MembershipDate DATE NOT NULL DEFAULT (CURDATE())
);


/*
Table: Books
Purpose: Stores the library's book collection.
Relationships:
   - Foreign Key to Genres (One-to-Many).
   - Connected to Authors via BookAuthors (Many-to-Many).
*/
CREATE TABLE Books (
    BookID INT AUTO_INCREMENT PRIMARY KEY,
    Title VARCHAR(255) NOT NULL,
    ISBN VARCHAR(20) NOT NULL UNIQUE,
    PublishedDate DATE,
    TotalCopies INT NOT NULL DEFAULT 1,
    AvailableCopies INT NOT NULL DEFAULT 1,
    GenreID INT,

    CONSTRAINT fk_book_genre
        FOREIGN KEY (GenreID)
        REFERENCES Genres(GenreID)
        ON DELETE SET NULL -- If a genre is deleted, don't delete the book, just nullify the genre link.
);


/*
Table: BookAuthors (Junction Table)
Purpose: Manages the many-to-many relationship between Books and Authors.
*/

CREATE TABLE BookAuthors (
    BookID INT,
    AuthorID INT,

    -- Composite Primary Key to ensure a book-author pair is unique.
    PRIMARY KEY (BookID, AuthorID),

    -- Foreign Key constraints
    CONSTRAINT fk_bookauthors_book
        FOREIGN KEY (BookID)
        REFERENCES Books(BookID)
        ON DELETE CASCADE, -- If a book is deleted, remove its author associations.

    CONSTRAINT fk_bookauthors_author
        FOREIGN KEY (AuthorID)
        REFERENCES Authors(AuthorID)
        ON DELETE CASCADE -- If an author is deleted, remove their book associations.
);


/*
Table: Loans
Purpose: Tracks which member has borrowed which book.
Relationships:
   - Foreign Key to Books (One Book can have many Loans).
   - Foreign Key to Members (One Member can have many Loans).
*/
CREATE TABLE Loans (
    LoanID INT AUTO_INCREMENT PRIMARY KEY,
    BookID INT NOT NULL,
    MemberID INT NOT NULL,
    LoanDate DATE NOT NULL DEFAULT (CURDATE()),
    DueDate DATE NOT NULL,
    ReturnDate DATE, -- NULL if the book has not been returned yet.

    CONSTRAINT fk_loan_book
        FOREIGN KEY (BookID)
        REFERENCES Books(BookID)
        ON DELETE RESTRICT, -- Prevent deleting a book if it's currently on loan.

    CONSTRAINT fk_loan_member
        FOREIGN KEY (MemberID)
        REFERENCES Members(MemberID)
        ON DELETE CASCADE -- If a member is deleted, their loan history is also removed.
);

