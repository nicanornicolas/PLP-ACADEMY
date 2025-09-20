// controllers/memberController.js
const db = require('../config/db');

// @desc    Create a new member
exports.createMember = async (req, res) => {
  try {
    const { name, address, phone, email } = req.body;
    const sql = 'INSERT INTO Members (Name, Address, PhoneNumber, Email) VALUES (?, ?, ?, ?)';
    const [result] = await db.execute(sql, [name, address, phone, email]);
    res.status(201).json({ id: result.insertId, name, email });
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
};

// @desc    Get all members
exports.getAllMembers = async (req, res) => {
  try {
    const [rows] = await db.query('SELECT * FROM Members');
    res.status(200).json(rows);
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
};

// @desc    Get a single member by ID
exports.getMemberById = async (req, res) => {
  try {
    const { id } = req.params;
    const [rows] = await db.query('SELECT * FROM Members WHERE MemberID = ?', [id]);
    if (rows.length === 0) {
      return res.status(404).json({ message: 'Member not found' });
    }
    res.status(200).json(rows[0]);
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
};

// @desc    Update a member
exports.updateMember = async (req, res) => {
  try {
    const { id } = req.params;
    const { name, address, phone, email } = req.body;
    const sql = 'UPDATE Members SET Name = ?, Address = ?, PhoneNumber = ?, Email = ? WHERE MemberID = ?';
    const [result] = await db.execute(sql, [name, address, phone, email, id]);
    if (result.affectedRows === 0) {
      return res.status(404).json({ message: 'Member not found' });
    }
    res.status(200).json({ message: 'Member updated successfully' });
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
};

// @desc    Delete a member
exports.deleteMember = async (req, res) => {
  try {
    const { id } = req.params;
    const [result] = await db.execute('DELETE FROM Members WHERE MemberID = ?', [id]);
    if (result.affectedRows === 0) {
      return res.status(404).json({ message: 'Member not found' });
    }
    res.status(200).json({ message: 'Member deleted successfully' });
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
};