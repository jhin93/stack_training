const express = require('express');
const bcrypt = require('bcrypt');
const jwt = require('jsonwebtoken');
const pool = require('../config/database');

const router = express.Router();

// User Registration
router.post('/register', async (req, res) => {
    try {
        const { email, password } = req.body;
        
        if(!email || !password) {
            return res.status(400).json({ error: 'Email and password are required' });
        }
        
        const existingUser = await pool.query('SELECT * FROM users WHERE email = $1', [email]);
        if(existingUser.rows.length > 0) {
            return res.status(400).json({ error: 'User already exists' });
        }
        
        // Hash the password
        const saltRounds = 10;
        const hashedPassword = await bcrypt.hash(password, saltRounds);
        
        // New User
        const newUser = await pool.query('INSERT INTO users (email, password_hash) VALUES ($1, $2) RETURNING *', [email, hashedPassword]);
        
        res.status(201).json({ 
            message: 'User registered successfully', 
            userId: newUser.rows[0].id 
        });
        
    } catch (error) {
        console.log("'Registration error: ", error);
        res.status(500).json({ error: 'Internal Server Error' });
    }
})

// User Login
router.post('/login', async (req, res) => {
    try {
        const { email, password } = req.body;
        
        // 입력값 검증
              if (!email || !password) {
                return res.status(400).json({ error: 'Email and password are required' });
              }
        
              // 사용자 찾기
              const user = await pool.query('SELECT * FROM users WHERE email = $1', [email]);
              if (user.rows.length === 0) {
                return res.status(401).json({ error: 'Invalid credentials' });
              }
        
              // 비밀번호 검증
              const isPasswordValid = await bcrypt.compare(password, user.rows[0].password_hash);
              if (!isPasswordValid) {
                return res.status(401).json({ error: 'Invalid credentials' });
              }
        
              // JWT 토큰 생성
              const token = jwt.sign(
                {
                  userId: user.rows[0].id,
                  email: user.rows[0].email
                },
                process.env.JWT_SECRET,
                { expiresIn: '1h' }
              );
        
              res.json({
                message: 'Login successful',
                token,
                user: {
                  id: user.rows[0].id,
                  email: user.rows[0].email
                }
              });
    } catch (error) {
        console.log("'Login error: ", error);
        res.status(500).json({ error: 'Internal Server Error' });
    }
})

module.exports = router;