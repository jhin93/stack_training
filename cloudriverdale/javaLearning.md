## 실습 프로젝트: 도서 관리 REST API

### 프로젝트 개요
**"Simple Book Library API"** - JWT 인증을 사용하는 도서 관리 시스템 REST API
- 기술 스택: Spring Boot + Spring Security + Spring Data JPA + PostgreSQL + JWT
- 최소 기능: 회원가입, 로그인, 도서 CRUD, 도서 대출/반납

### 실습 진행 순서

#### Step 1: 프로젝트 초기 설정 (30분)
1. Spring Initializr 사용 (https://start.spring.io)
   - Project: Maven
   - Language: Java  
   - Spring Boot: 3.x.x
   - Dependencies:
     - Spring Web
     - Spring Data JPA
     - PostgreSQL Driver
     - Spring Security
     - Lombok
     - Validation

2. 프로젝트 구조:
   ```
   book-library-api/
   ├── src/main/java/com/example/library/
   │   ├── BookLibraryApplication.java
   │   ├── config/
   │   │   ├── SecurityConfig.java
   │   │   └── JwtAuthenticationFilter.java
   │   ├── controller/
   │   │   ├── AuthController.java
   │   │   └── BookController.java
   │   ├── dto/
   │   │   ├── LoginRequest.java
   │   │   ├── RegisterRequest.java
   │   │   └── BookDto.java
   │   ├── entity/
   │   │   ├── User.java
   │   │   └── Book.java
   │   ├── repository/
   │   │   ├── UserRepository.java
   │   │   └── BookRepository.java
   │   ├── service/
   │   │   ├── AuthService.java
   │   │   ├── BookService.java
   │   │   └── JwtService.java
   │   └── exception/
   │       └── GlobalExceptionHandler.java
   └── src/main/resources/
       └── application.properties
   ```

#### Step 2: 기초 개념 구현 (1시간)
1. **IoC와 Dependency Injection 실습**
   - @Component, @Service, @Repository 어노테이션 사용
   - @Autowired로 의존성 주입

2. **application.properties 설정**
   ```properties
   # 데이터베이스 설정
   spring.datasource.url=jdbc:postgresql://localhost:5432/librarydb
   spring.datasource.username=your-username
   spring.datasource.password=your-password

   # JPA 설정
   spring.jpa.hibernate.ddl-auto=update
   spring.jpa.properties.hibernate.dialect=org.hibernate.dialect.PostgreSQLDialect
   spring.jpa.show-sql=true

   # JWT 설정
   jwt.secret=your-secret-key
   jwt.expiration=3600000
   ```

#### Step 3: 엔티티와 Repository 구현 (45분)
1. **User 엔티티**
   ```java
   @Entity
   @Table(name = "users")
   public class User {
       @Id
       @GeneratedValue(strategy = GenerationType.IDENTITY)
       private Long id;

       @Column(unique = true, nullable = false)
       private String email;

       @Column(nullable = false)
       private String password;

       private String role = "USER";

       @Temporal(TemporalType.TIMESTAMP)
       private Date createdAt;
   }
   ```

2. **Book 엔티티**
   ```java
   @Entity
   @Table(name = "books")
   public class Book {
       @Id
       @GeneratedValue(strategy = GenerationType.IDENTITY)
       private Long id;

       private String isbn;
       private String title;
       private String author;
       private Boolean available = true;

       @ManyToOne
       @JoinColumn(name = "borrowed_by")
       private User borrowedBy;

       @Temporal(TemporalType.TIMESTAMP)
       private Date borrowedAt;
   }
   ```

3. **JpaRepository 인터페이스 구현**
   - UserRepository: findByEmail() 메서드
   - BookRepository: findByAvailable(), findByBorrowedBy() 메서드

#### Step 4: Service 계층 구현 (1시간)
1. **AuthService**
   - 회원가입: BCrypt로 비밀번호 암호화
   - 로그인: 비밀번호 검증 및 JWT 토큰 발급

2. **JwtService**
   - JWT 토큰 생성
   - 토큰 검증
   - 토큰에서 사용자 정보 추출

3. **BookService**
   - 도서 CRUD 작업
   - 도서 대출/반납 로직

#### Step 5: Controller와 REST API 구현 (1시간 30분)
1. **AuthController**
   - POST /api/auth/register - 회원가입
   - POST /api/auth/login - 로그인

2. **BookController** (모든 엔드포인트 JWT 인증 필요)
   - GET /api/books - 모든 도서 조회
   - GET /api/books/available - 대출 가능한 도서 조회
   - GET /api/books/{id} - 특정 도서 조회
   - POST /api/books - 새 도서 등록 (ADMIN 권한)
   - PUT /api/books/{id} - 도서 정보 수정 (ADMIN 권한)
   - DELETE /api/books/{id} - 도서 삭제 (ADMIN 권한)
   - POST /api/books/{id}/borrow - 도서 대출
   - POST /api/books/{id}/return - 도서 반납

#### Step 6: Spring Security와 JWT 설정 (1시간 30분)
1. **SecurityConfig**
   - Spring Security 설정
   - JWT 필터 등록
   - 엔드포인트별 권한 설정

2. **JwtAuthenticationFilter**
   - JWT 토큰 검증 필터
   - SecurityContext에 인증 정보 설정

3. **예외 처리**
   - @ControllerAdvice로 전역 예외 처리
   - 표준화된 에러 응답 형식

#### Step 7: 테스트 및 검증 (45분)
1. **Postman으로 API 테스트**
   - 회원가입 → 로그인 → JWT 토큰 획득
   - Authorization 헤더에 Bearer 토큰 설정
   - 도서 CRUD 작업 테스트
   - 도서 대출/반납 테스트

2. **테스트 시나리오**
   - 일반 사용자: 도서 조회, 대출, 반납
   - 관리자: 도서 등록, 수정, 삭제
   - 인증 실패 케이스
   - 이미 대출된 도서 대출 시도

### 학습 포인트 체크리스트
- [ ] IoC와 DI 원리 이해
- [ ] Spring Boot Annotation 활용
- [ ] JPA Entity와 Repository 패턴
- [ ] Service 계층의 역할과 책임
- [ ] REST API 설계 원칙 적용
- [ ] Spring Security 동작 방식
- [ ] JWT 토큰 기반 인증 구현
- [ ] @ControllerAdvice를 통한 예외 처리
- [ ] Maven을 통한 의존성 관리
- [ ] application.properties 설정 관리

### 예상 완성 시간: 7시간

### 고급 학습 과제 (선택사항)
1. **Query Method와 @Query 활용**
   - 복잡한 검색 조건 구현
   - JPQL 쿼리 작성

2. **페이징과 정렬**
   - Pageable 인터페이스 활용
   - 대량 데이터 처리

3. **DTO 패턴 적용**
   - MapStruct 또는 ModelMapper 사용
   - Entity와 DTO 분리

4. **Validation 강화**
   - @Valid 어노테이션 활용
   - 커스텀 Validator 구현

5. **API 문서화**
   - Swagger/OpenAPI 적용
   - API 문서 자동 생성

6. **Microservices 준비**
   - 서비스 분리 설계
   - Spring Cloud 기초 적용

### 학습 팁
1. 각 어노테이션의 역할을 명확히 이해
2. Spring의 자동 설정이 어떻게 동작하는지 파악
3. 로그를 활용해 Spring의 동작 과정 추적
4. 에러 스택 트레이스를 차근차근 읽고 해결
5. Spring Boot DevTools로 개발 생산성 향상