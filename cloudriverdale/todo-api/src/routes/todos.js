const express = require('express');
  const pool = require('../config/database');
  const authenticateToken = require('../middleware/auth');

  const router = express.Router();

  // 모든 to-do 라우트에 JWT 인증 적용
  router.use(authenticateToken);

  // 1. 내 할일 목록 조회 - GET /api/todos
  router.get('/', async (req, res) => {
    try {
      const todos = await pool.query(
        'SELECT * FROM todos WHERE user_id = $1 ORDER BY created_at DESC',
        [req.user.userId]
      );

      res.json({
        message: 'Todos retrieved successfully',
        todos: todos.rows
      });

    } catch (error) {
      console.error('Get todos error:', error);
      res.status(500).json({ error: 'Internal server error' });
    }
  });

  // 2. 새 할일 생성 - POST /api/todos
  router.post('/', async (req, res) => {
    try {
      const { title } = req.body;

      if (!title) {
        return res.status(400).json({ error: 'Title is required' });
      }

      const newTodo = await pool.query(
        'INSERT INTO todos (user_id, title) VALUES ($1, $2) RETURNING *',
        [req.user.userId, title]
      );

      res.status(201).json({
        message: 'Todo created successfully',
        todo: newTodo.rows[0]
      });

    } catch (error) {
      console.error('Create todo error:', error);
      res.status(500).json({ error: 'Internal server error' });
    }
  });

  // 3. 할일 수정 - PUT /api/todos/:id
  router.put('/:id', async (req, res) => {
    try {
      const { id } = req.params;
      const { title, completed } = req.body;

      // 해당 to-do가 현재 사용자의 것인지 확인
      const existingTodo = await pool.query(
        'SELECT * FROM todos WHERE id = $1 AND user_id = $2',
        [id, req.user.userId]
      );

      if (existingTodo.rows.length === 0) {
        return res.status(404).json({ error: 'Todo not found' });
      }

      // 업데이트할 필드만 동적으로 처리
      const fieldsToUpdate = [];
      const values = [];
      let paramCount = 1;

      if (title !== undefined) {
        fieldsToUpdate.push(`title = $${paramCount++}`);
        values.push(title);
      }

      if (completed !== undefined) {
        fieldsToUpdate.push(`completed = $${paramCount++}`);
        values.push(completed);
      }

      if (fieldsToUpdate.length === 0) {
        return res.status(400).json({ error: 'No fields to update' });
      }

      // WHERE 조건을 위한 파라미터 추가
      values.push(id, req.user.userId);

      const updateQuery = `
        UPDATE todos 
        SET ${fieldsToUpdate.join(', ')} 
        WHERE id = $${paramCount++} AND user_id = $${paramCount++} 
        RETURNING *
      `;

      const updatedTodo = await pool.query(updateQuery, values);

      res.json({
        message: 'Todo updated successfully',
        todo: updatedTodo.rows[0]
      });

    } catch (error) {
      console.error('Update todo error:', error);
      res.status(500).json({ error: 'Internal server error' });
    }
  });

  // 4. 할일 삭제 - DELETE /api/todos/:id
  router.delete('/:id', async (req, res) => {
    try {
      const { id } = req.params;

      const deletedTodo = await pool.query(
        'DELETE FROM todos WHERE id = $1 AND user_id = $2 RETURNING *',
        [id, req.user.userId]
      );

      if (deletedTodo.rows.length === 0) {
        return res.status(404).json({ error: 'Todo not found' });
      }

      res.json({
        message: 'Todo deleted successfully',
        todo: deletedTodo.rows[0]
      });

    } catch (error) {
      console.error('Delete todo error:', error);
      res.status(500).json({ error: 'Internal server error' });
    }
  });

  module.exports = router;
