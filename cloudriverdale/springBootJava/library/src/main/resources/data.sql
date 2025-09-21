  INSERT INTO users (email, password, name, role, is_active, created_at,
  updated_at)
  VALUES
  ('admin@test.com', '$2a$10$...', 'Admin User', 'ADMIN', true, NOW(), NOW()),
  ('user@test.com', '$2a$10$...', 'Test User', 'USER', true, NOW(), NOW());

