## 실습 프로젝트: 미니 할일 관리 API

### 프로젝트 개요
**"Simple Todo API"** - JWT 인증을 사용하는 개인 할일 관리 REST API
- 기술 스택: Node.js + Express + PostgreSQL + JWT
- 최소 기능: 회원가입, 로그인, 할일 CRUD

### 실습 진행 순서

#### Step 1: 프로젝트 초기 설정 (30분)
1. 폴더 생성: `todo-api`
2. `npm init -y`로 package.json 생성
3. 필수 패키지 설치:
   ```bash
   npm install express pg bcrypt jsonwebtoken dotenv
   npm install -D nodemon
   ```
4. 기본 폴더 구조 생성:
   ```
   todo-api/
   ├── src/
   │   ├── server.js
   │   ├── config/
   │   │   └── database.js
   │   ├── routes/
   │   │   ├── auth.js
   │   │   └── todos.js
   │   └── middleware/
   │       └── auth.js
   ├── .env
   └── package.json
   ```

#### Step 2: PostgreSQL 데이터베이스 설정 (20분)
1. 데이터베이스 생성: `CREATE DATABASE todoapp;`
2. 테이블 2개만 생성:
   ```sql
   -- users 테이블
   CREATE TABLE users (
     id SERIAL PRIMARY KEY,
     email VARCHAR(255) UNIQUE NOT NULL,
     password_hash VARCHAR(255) NOT NULL,
     created_at TIMESTAMP DEFAULT NOW()
   );

   -- todos 테이블
   CREATE TABLE todos (
     id SERIAL PRIMARY KEY,
     user_id INTEGER REFERENCES users(id),
     title VARCHAR(255) NOT NULL,
     completed BOOLEAN DEFAULT false,
     created_at TIMESTAMP DEFAULT NOW()
   );
   ```

#### Step 3: Express 서버 기본 설정 (15분)
1. `server.js`에 Express 서버 설정
2. `.env` 파일에 환경변수 설정:
   ```
   PORT=3000
   DATABASE_URL=postgresql://user:password@localhost:5432/todoapp
   JWT_SECRET=your-secret-key
   ```
3. `database.js`에 PostgreSQL 연결 설정

#### Step 4: 인증 API 구현 (1시간)
1. **POST /api/auth/register** - 회원가입
    - 이메일, 비밀번호 받기
    - bcrypt로 비밀번호 해싱
    - DB에 저장

2. **POST /api/auth/login** - 로그인
    - 이메일, 비밀번호 검증
    - JWT 토큰 발급 (유효기간 1시간)
    - 토큰 반환

#### Step 5: JWT 인증 미들웨어 구현 (30분)
1. `middleware/auth.js` 작성
2. Authorization 헤더에서 토큰 추출
3. JWT 검증 후 user 정보를 req.user에 저장

#### Step 6: Todo CRUD API 구현 (1시간)
모든 엔드포인트는 JWT 인증 필요:
1. **GET /api/todos** - 내 할일 목록 조회
2. **POST /api/todos** - 새 할일 생성
3. **PUT /api/todos/:id** - 할일 수정
4. **DELETE /api/todos/:id** - 할일 삭제

#### Step 7: API 테스트 (30분)
1. Postman 또는 curl로 테스트
2. 테스트 시나리오:
    - 회원가입 → 로그인 → 토큰 받기
    - 토큰으로 할일 생성
    - 할일 목록 조회
    - 할일 완료 처리
    - 할일 삭제

### 학습 포인트 체크리스트
- [ ] JWT 토큰 생성과 검증 과정 이해
- [ ] 비밀번호 해싱의 중요성 이해
- [ ] REST API 설계 원칙 적용
- [ ] PostgreSQL 쿼리 작성
- [ ] 미들웨어 동작 방식 이해
- [ ] 환경변수로 민감정보 관리
- [ ] 에러 처리 구현

### 예상 완성 시간: 4시간

### 다음 단계 (선택사항)
- Refresh Token 구현
- 입력값 검증 추가 (express-validator)
- 에러 처리 개선
- Docker로 컨테이너화
- 간단한 프론트엔드 추가

## 학습 팁
1. 각 단계별로 코드를 실행하며 동작 확인
2. 에러가 발생하면 에러 메시지를 잘 읽고 해결
3. console.log()를 활용해 데이터 흐름 추적