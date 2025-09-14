const express = require('express');
require('dotenv').config();

const authRoutes = require('./routes/auth');
const todoRoutes = require('./routes/todos');

const app = express();
const PORT = process.env.PORT || 3000;

//Middleware
app.use(express.json());

//Routes
app.use('/api/auth', authRoutes);
app.use('/api/todos', todoRoutes);

//Health check
app.get('/health', (req, res) => res.json({ status: 'Server is running' }));

app.listen(PORT, () => console.log(`Server is running on port ${PORT}`));