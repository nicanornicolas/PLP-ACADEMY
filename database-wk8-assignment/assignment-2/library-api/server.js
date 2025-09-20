// server.js
const express = require('express');
const dotenv = require('dotenv');

// Load env vars
dotenv.config();

// Route files
const bookRoutes = require('./routes/books');
const memberRoutes = require('./routes/members');

const app = express();

// Body parser middleware
app.use(express.json());

// Mount routers
app.use('/api/books', bookRoutes);
app.use('/api/members', memberRoutes);

const PORT = process.env.PORT || 3000;

app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});