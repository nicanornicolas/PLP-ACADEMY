# Library Management API

A robust and simple-to-use CRUD REST API for managing books and members in a library system. This API is built with Node.js, Express, and MySQL, providing a solid foundation for a library management application.

## Features

- **Book Management:** Perform CRUD operations (Create, Read, Update, Delete) for books.
- **Member Management:** Perform CRUD operations for library members.
- **Scalable Architecture:** Organized into routes, controllers, and configuration for easy maintenance.

## Technologies Used

- **Backend:** Node.js, Express.js
- **Database:** MySQL
- **Development:** `nodemon` for automatic server reloading.

## Prerequisites

Before you begin, ensure you have the following installed:

- [Node.js](https://nodejs.org/) (v16 or higher)
- [MySQL Server](https://www.mysql.com/downloads/)

## Installation & Setup

1.  **Clone the repository:**
    ```sh
    git clone <your-github-repo-url>
    cd library-api
    ```

2.  **Install dependencies:**
    ```sh
    npm install
    ```

3.  **Set up the database:**
    - Ensure your MySQL server is running.
    - Connect to MySQL and execute the `library_db.sql` script (provided in the submission) to create the required database and tables.

4.  **Configure environment variables:**
    - Create a `.env` file in the root of the project.
    - Add the following configuration, replacing the placeholder values with your MySQL credentials:
      ```
      DB_HOST=localhost
      DB_USER=your_mysql_user
      DB_PASSWORD=your_mysql_password
      DB_NAME=LibraryDB
      PORT=3000
      ```

## Running the Application

-   **For development (with auto-reloading):**
    ```sh
    npm run dev
    ```

-   **For production:**
    ```sh
    npm start
    ```

The server will be running at `http://localhost:3000`.

## API Endpoints

All endpoints are prefixed with `/api`.

### Books API (`/books`)

| Method | Endpoint | Description             | Request Body Example                                                 |
| :----- | :------- | :---------------------- | :------------------------------------------------------------------- |
| `POST` | `/`      | Create a new book.      | `{ "title": "The Great Gatsby", "isbn": "978-0743273565", "availableCopies": 5, "totalCopies": 5 }` |
| `GET`  | `/`      | Get a list of all books.| (None)                                                               |
| `GET`  | `/:id`   | Get a book by its ID.   | (None)                                                               |
| `PUT`  | `/:id`   | Update a book's details.| `{ "title": "The Great Gatsby", "availableCopies": 4 }`              |
| `DELETE`| `/:id`   | Delete a book.          | (None)                                                               |

### Members API (`/members`)

| Method | Endpoint | Description              | Request Body Example                                                 |
| :----- | :------- | :----------------------- | :------------------------------------------------------------------- |
| `POST` | `/`      | Create a new member.     | `{ "firstName": "John", "lastName": "Doe", "email": "john.doe@example.com" }` |
| `GET`  | `/`      | Get a list of all members.| (None)                                                               |
| `GET`  | `/:id`   | Get a member by ID.      | (None)                                                               |
| `PUT`  | `/:id`   | Update a member's details.| `{ "email": "j.doe@newemail.com", "phoneNumber": "123-456-7890" }` |
| `DELETE`| `/:id`   | Delete a member.         | (None)                                                               |