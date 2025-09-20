// controllers/bookController.js
const db = require('../config/db');

// @desc    Create a new book
exports.createBook = async (req, res) => {
  try {
    const { title, isbn, publishedDate, totalCopies, availableCopies, genreId } = req.body;
    const sql = 'INSERT INTO Books (Title, ISBN, PublishedDate, TotalCopies, AvailableCopies, GenreID) VALUES (?, ?, ?, ?, ?, ?)';
    const [result] = await db.execute(sql, [title, isbn, publishedDate, totalCopies, availableCopies, genreId]);
    res.status(201).json({ id: result.insertId, title, isbn });
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
};

// @desc    Get all books
exports.getAllBooks = async (req, res) => {
  try {
    const [rows] = await db.query('SELECT * FROM Books');
    res.status(200).json(rows);
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
};

// @desc    Get a single book by ID
exports.getBookById = async (req, res) => {
  try {
    const { id } = req.params;
    const [rows] = await db.query('SELECT * FROM Books WHERE BookID = ?', [id]);
    if (rows.length === 0) {
      return res.status(404).json({ message: 'Book not found' });
    }
    res.status(200).json(rows[0]);
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
};

// @desc    Update a book
exports.updateBook = async (req, res) => {
  try {
    const { id } = req.params;
    const { title, isbn, availableCopies } = req.body; // Example fields to update
    const sql = 'UPDATE Books SET Title = ?, ISBN = ?, AvailableCopies = ? WHERE BookID = ?';
    const [result] = await db.execute(sql, [title, isbn, availableCopies, id]);
    if (result.affectedRows === 0) {
      return res.status(404).json({ message: 'Book not found' });
    }
    res.status(200).json({ message: 'Book updated successfully' });
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
};

// @desc    Delete a book
exports.deleteBook = async (req, res) => {
  try {
    const { id } = req.params;
    const [result] = await db.execute('DELETE FROM Books WHERE BookID = ?', [id]);
    if (result.affectedRows === 0) {
      return res.status(404).json({ message: 'Book not found' });
    }
    res.status(200).json({ message: 'Book deleted successfully' });
  } catch (error) {
    // Handle foreign key constraint error (e.g., book is on loan)
    if (error.code === 'ER_ROW_IS_REFERENCED_2') {
        return res.status(400).json({ message: 'Cannot delete book. It is currently on loan.' });
    }
    res.status(500).json({ error: error.message });
  }
};