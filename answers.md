### 1. COMPONENTS OF A DATABASE MANAGEMENT SYSTEM
1. QUERY PROCCESOR.
Understands and optimizes the user's request.
## Subcomponents of Query Processor.
a) DDL Compiler (Data Definition Language): It processes commands that define the database structure. When you use commands like CREATE TABLE, ALTER TABLE, or DROP TABLE, this compiler translates them into a set of entries in the data dictionary.

b) DML Compiler (Data Manipulation Language): It processes commands that manipulate the data itself, like retrieving, inserting, or updating it. It converts SELECT, INSERT, UPDATE, and DELETE queries into a low-level plan that the rest of the system can execute.

c) Query Optimizer: For any given query, there are many ways to get the data. The optimizer's job is to find the most efficient execution plan.

2. STORAGE ENGINE
It's responsible for the interaction between the data stored on disk and the system's memory. It carries out the plan created by the Query Processor.
## Subcomponents of Storage Engine
a) Transaction Manager: Ensures that database transactions are executed reliably and consistently. It guarantees the famous ACID properties (Atomicity, Consistency, Isolation, Durability).

b) Buffer Manager (or Cache Manager): This is a crucial performance component. Reading from a hard drive (disk) is very slow. Reading from computer memory (RAM) is very fast. The buffer manager intelligently brings data from the slow disk into a fast "buffer" in RAM before it's needed, so the query processor can access it quickly.

c) File Manager: Manages the allocation of space on the disk. It knows exactly where the files that store the database tables are located on the hard drive.

d) Authorization and Integrity Manager: The security guard. It checks if the user has permission to execute the query (SELECT, DELETE, etc.) and ensures that any data being inserted or updated follows the defined rules (e.g., an age column cannot contain a negative number).

3. The Physical Database and Metadata
The lowest level, representing the data as it actually exists.

## Components include:
a) Data Files: The actual files on the disk (e.g., on your C: or /dev/sda drive) that hold the data.
b) Data Dictionary (or Metadata): This is "data about the data." It's a special set of tables that stores the database schema: information about all the tables in the database, their columns, data types (INTEGER, TEXT, etc.), constraints, indexes, and user permissions. The Query Processor and Storage Manager constantly refer to the Data Dictionary to know how the data is structured.


### 2. RELATIONAL DATABASE
 A relational database is a method of storing and organizing data in tables. Picture of these tables like super-powered spreadsheets. The "relational" part is the most important concept: these tables can be logically linked to each other based on the data they hold.

 Example:
 Simple Online Store -
  1. Customers Table
Here, each customer is listed only once.
(CustomerID is the Primary Key)
  2. Products Table
Here, each product is listed only once.
(ProductID is the Primary Key)
  3. Orders Table
This table brings it all together. It doesn't store any names or prices. It only stores the IDs and the information specific to the order itself.
(OrderID is the Primary Key for this table. CustomerID and ProductID are Foreign Keys)

### 3. Structured Query Language (SQL) 
It contains commands that are classified into groups based on their functions.

1. DDL (Data Definition Language)
Defines or modifies the structure of the database and its objects (like tables, indexes, etc.). DDL commands are about the schema or the blueprint of your database.
## Key commands:
a) CREATE: Used to create new objects like databases, tables, views, and indexes.
 - CREATE TABLE Students (ID INT, Name VARCHAR(100));
b) ALTER: Used to modify the structure of an existing object. You can add, delete, or modify columns in a table.
 - ALTER TABLE Students ADD Email VARCHAR(100);
c) DROP: Used to permanently delete an entire object from the database.
 - DROP TABLE Students;
d) TRUNCATE: Removes all records from a table quickly, but the table structure remains. It's faster than DELETE but cannot be rolled back in most systems.
 - TRUNCATE TABLE Students;

2. DML (Data Manipulation Language)
Manages the data within the schema objects. These commands are used for inserting, updating, deleting, and retrieving data from the tables.
## Key commands:
a) INSERT: Adds new rows (records) of data into a table.
 - INSERT INTO Students (ID, Name) VALUES (1, 'Alice');
b) UPDATE: Modifies existing records in a table.
 - UPDATE Students SET Name = 'Alicia' WHERE ID = 1;
c) DELETE: Removes one or more rows from a table.
 - DELETE FROM Students WHERE ID = 1;

3. DQL (Data Query Language)
This classification exists solely for the task of retrieving data. While technically a form of data "manipulation," querying is such a fundamental and common operation that it's often given its own category.
## Key command:
a) SELECT: The cornerstone of SQL. Used to retrieve data from one or more tables.
 - SELECT Name, Email FROM Students WHERE ID > 10;

4. DCL (Data Control Language)
Controls access to data in the database. These commands are all about user permissions and security.
## Key commands:
a) GRANT: Gives specific permissions (like SELECT, INSERT, UPDATE) on a database object to a user.
 - GRANT SELECT ON Students TO user_bob;
b) REVOKE: Takes away permissions that were previously granted.
 - REVOKE SELECT ON Students FROM user_bob; 

5. TCL (Transaction Control Language)
Manages transactions in the database. A transaction is a sequence of operations performed as a single, logical unit of work. TCL commands ensure the data integrity (ACID properties) of the database.
## Key commands:
a) COMMIT: Saves all the work done in the current transaction. The changes become permanent.
b) ROLLBACK: Undoes all the changes made in the current transaction, restoring the database to its state before the transaction began.
c) SAVEPOINT: Sets a specific point within a transaction to which you can later roll back, without undoing the entire transaction.

### 4. PRIMARY KEY AND FOREIGN KEY
- A primary key is a column (or a set of columns) that uniquely identifies each row in a table. It cannot have duplicate values and cannot be empty (NULL).
- A foreign key is a column in one table that refers to the primary key of another table. It acts as a cross-reference, linking the data between tables.

### 5. An Entity-Relation Diagram
An ERD is a visual blueprint of a database.
It's a type of flowchart that illustrates how "entities" (like people, objects, or concepts) relate to each other within a system. Before you write a single line of CREATE TABLE in SQL, you draw an ERD to plan the structure of your data.

## Components of an ERD
1. Entity
An entity is a real-world object or concept that can be distinctly identified. It's a "noun." In a diagram, it's represented by a rectangle.
+-----------+
|  Student  |
+-----------+
2. Attribute
An attribute is a property or characteristic of an entity. It describes the entity.
 - Examples: For the Student entity, attributes could be StudentID, FirstName, LastName, DateOfBirth.
 - Primary Key: One attribute is always designated as the Primary Key. This is a unique identifier for each record in the entity (e.g., StudentID). It is often underlined.
Attributes are typically written inside the entity's rectangle.
+-----------------------------------+
|  Student                          |
+-----------------------------------+
|  _StudentID_                      |  <-- Primary Key (underlined)
|  FirstName                        |
|  LastName                         |
|  Email                            |
+-----------------------------------+
3. Relationship
A relationship shows how two or more entities are associated with each other. It's a "verb." In traditional diagrams, it's represented by a diamond, but in modern notation (like Crow's Foot), it's just the line connecting them.

### 6. Advantages of a Relational Database
 1. Data Integrity and Accuracy (ACID Compliance): This is their biggest strength. They enforce rules (constraints) to ensure data is reliable. They follow ACID properties (Atomicity, Consistency, Isolation, Durability), which guarantees that transactions (like transferring money) are either fully completed or not at all, preventing data corruption.
 2. Reduced Data Redundancy: By splitting data into separate tables (a process called normalization), you avoid repeating information.
 3. Simplicity and Ease of Use: The table/row/column model is intuitive and easy to understand. SQL is a powerful, declarative language—you describe what you want, and the database figures out how to get it.
 4. Flexibility and Powerful Querying: The use of JOINs allows you to ask complex questions and retrieve data in countless combinations, all without having to restructure the database itself.
 5. Security: The DBMS provides fine-grained access control. You can grant permissions to specific users for specific tables or even specific columns.


### 7. Data types used to store data in tables.
1. Numeric Types
Used for storing numbers. You choose the specific type based on whether you need whole numbers or numbers with decimal points, and how large the number might get.
 - Include:
    - INTEGER or INT	A whole number (no decimal points). Can be positive or negative.
    - SMALLINT	A smaller whole number. Uses less storage than INT.
    - BIGINT	A very large whole number.
    - DECIMAL(p, s) or NUMERIC(p, s)	A fixed-point number with exact precision. Crucial for financial data. p is the total number of digits; s is the number of digits after the decimal point.
    - FLOAT or REAL	A floating-point (approximate value) number. Good for scientific calculations where absolute precision is not required.

2. String (Character) Types
Used for storing text. The main difference is whether the length is fixed or variable.
 - Include:
    - VARCHAR(n)	Variable-length string with a maximum length of n characters. It only uses storage for the characters you actually enter. This is the most common string type.
    - CHAR(n)	Fixed-length string that is always n characters long. If you store a shorter string, it will be padded with spaces to fill the length.
    - TEXT	A variable-length string for holding very large amounts of text. The maximum length is very large and system-dependent.

3. Date and Time Types
Used for storing date and/or time values. Storing them in these types allows you to perform calculations, like finding the difference between two dates.
  - Include:
      - DATE	Stores only the date (year, month, day).
      - TIME	Stores only the time of day (hours, minutes, seconds).
      - TIMESTAMP or DATETIME	Stores both date and time. TIMESTAMP is often timezone-aware and is great for tracking when a record was created or modified.

4.  Boolean Type
Used for storing true/false values.
  - Include:
      - BOOLEAN	Stores TRUE or FALSE. Some systems (like SQL Server) use a BIT type, where 1 represents true and 0 represents false.

### 8. Purpose of a Database Management System
1. To Abstract Complexity from the User
Problem: If you stored data in raw files, you would have to write complex code to handle exactly where on the disk the data is, how to read it byte-by-byte, and how to find anything.
DBMS Purpose: The DBMS provides a simple, high-level language (like SQL) to ask for what you want. You say, "Get me all customers from California," and the DBMS handles the thousands of low-level operations required to find and present that data.

2. To Enforce Data Integrity
Problem: Without rules, you could store an age as "blue" or an order_date as "tomorrow." This "bad data" makes the database useless.
DBMS Purpose: The DBMS enforces rules (constraints) on the data. You can specify that the age column must be an INTEGER, the email column must be unique, and a product_id in the Orders table must correspond to a real product in the Products table.

3. To Provide Concurrent Access
Problem: In a bank, what happens if two people try to withdraw money from the same joint account at the exact same millisecond from two different ATMs? Without a system, they could both get the money, leaving the account with a negative balance.
DBMS Purpose: The DBMS manages concurrency, allowing multiple users to read and write to the database simultaneously without interfering with each other or corrupting the data. It uses sophisticated locking mechanisms to ensure transactions are handled safely and in order.

4. To Control Data Redundancy
Problem: If you store a customer's address in the Customers table, the Orders table, and the Invoices table, you have redundant data. If they move, you have to update it in three places. If you miss one, the data is now inconsistent.
DBMS Purpose: The relational model, managed by the DBMS, allows you to normalize your data. You store the address in one place (Customers table) and link to it using a customer_id. This minimizes redundancy, saves space, and ensures consistency.

5. To Ensure Security
Problem: Anyone with access to the server could potentially read or delete your sensitive data files.
DBMS Purpose: The DBMS provides robust security and authorization features. You can create users and grant them specific permissions (e.g., the sales team can SELECT from the Customers table but cannot DELETE from it, while accountants can UPDATE the Invoices table).

6. To Provide Backup and Recovery
Problem: What if the server's hard drive fails? Or a user accidentally deletes the entire Orders table? Without a system, your data is gone forever.
DBMS Purpose: A DBMS provides tools for creating regular backups of the database. More importantly, it maintains a log of all transactions, which allows it to recover the database to a consistent state right before a failure occurred.