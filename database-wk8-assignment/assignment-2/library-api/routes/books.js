// routes/books.js
const express = require('express');
const {
  createBook,
  getAllBooks,
  getBookById,
  updateBook,
  deleteBook,
} = require('../controllers/bookController');

const router = express.Router();

router.route('/').get(getAllBooks).post(createBook);
router.route('/:id').get(getBookById).put(updateBook).delete(deleteBook);

module.exports = router;