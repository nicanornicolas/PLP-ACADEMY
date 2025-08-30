# Assignment 1: Designing my Own Class! 🏗️

# --- Step 1: Create a base class representing a 'Book' ---
class Book:
    """
    Represents a physical book with attributes like title, author, and page count.
    """
    
    # --- Step 2: Use a constructor to initialize each object ---
    def __init__(self, title, author, pages, genre):
        # These are the attributes of our Book class
        self.title = title
        self.author = author
        self.pages = pages
        self.genre = genre
        self.is_open = False # A book is closed by default
        self.current_page = 1

    # --- Step 3: Add methods to bring the class to life ---
    def open_book(self):
        """Sets the book's state to open."""
        if self.is_open:
            print(f"'{self.title}' is already open.")
        else:
            self.is_open = True
            print(f"You have opened '{self.title}'.")

    def close_book(self):
        """Sets the book's state to closed."""
        if not self.is_open:
            print(f"'{self.title}' is already closed.")
        else:
            self.is_open = False
            print(f"You have closed '{self.title}'.")
            
    def read_page(self, page_number):
        """Simulates reading a specific page."""
        if not self.is_open:
            print(f"You can't read '{self.title}' because it's closed!")
            return
        
        if 1 <= page_number <= self.pages:
            self.current_page = page_number
            print(f"You are now on page {self.current_page} of '{self.title}'.")
        else:
            print(f"Invalid page number! This book only has {self.pages} pages.")

    def get_summary(self):
        """Returns a summary string of the book's details."""
        return f"Title: '{self.title}', Author: {self.author}, Pages: {self.pages}, Genre: {self.genre}"


# --- Step 4: Add an inheritance layer ---
# The 'EBook' class inherits from the 'Book' class.
class EBook(Book):
    """
    Represents an electronic book, which inherits all Book properties
    but adds digital-specific attributes and methods.
    """
    
    def __init__(self, title, author, pages, genre, file_format, file_size_mb):
        # Call the constructor of the parent class ('Book') to handle the common attributes.
        super().__init__(title, author, pages, genre)
        
        # Add new attributes specific to EBooks
        self.file_format = file_format
        self.file_size_mb = file_size_mb
        # This is a "protected" attribute, a convention for encapsulation.
        # It signals that it should not be modified directly from outside the class.
        self._is_drm_protected = True 

    # --- Polymorphism: Method Overriding ---
    # We override the get_summary() method to include EBook-specific details.
    def get_summary(self):
        """
        Overrides the parent's get_summary method to add more details.
        This is an example of POLYMORPHISM.
        """
        # Get the original summary from the parent class
        book_summary = super().get_summary()
        # Add the new EBook-specific information
        return f"{book_summary}, Format: {self.file_format}, Size: {self.file_size_mb}MB"
        
    # --- New method specific to the EBook child class ---
    def send_to_device(self, device_name):
        """Simulates sending the ebook to a device."""
        print(f"Sending '{self.title}' ({self.file_format}) to {device_name}.")
        
    # --- Encapsulation Example ---
    def check_drm_status(self):
        """
        A method to safely access the 'protected' _is_drm_protected attribute.
        This is an example of ENCAPSULATION.
        """
        if self._is_drm_protected:
            print(f"'{self.title}' is protected by Digital Rights Management.")
        else:
            print(f"'{self.title}' is not DRM protected.")


# --- Let's bring our classes to life by creating objects! ---

print("--- Creating a Physical Book Object ---")
# Create an instance of the Book class
my_book = Book("The Hobbit", "J.R.R. Tolkien", 310, "Fantasy")

# Use the object's methods
print(my_book.get_summary())
my_book.open_book()
my_book.read_page(75)
my_book.close_book()

print("\n" + "="*40 + "\n")

print("--- Creating an EBook Object ---")
# Create an instance of the EBook child class
my_ebook = EBook("Dune", "Frank Herbert", 412, "Sci-Fi", "EPUB", 5.2)

# Use methods from both the parent and child classes
print(my_ebook.get_summary()) # This will call the OVERRIDDEN method in EBook
my_ebook.open_book()
my_ebook.read_page(150)
my_ebook.send_to_device("Kindle Oasis") # This method only exists in the EBook class
my_ebook.check_drm_status() # Demonstrates encapsulation