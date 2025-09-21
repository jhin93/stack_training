## 실습 프로젝트: 도서 관리 REST API

### 프로젝트 개요
**"Simple Book Library API"** - JWT 인증을 사용하는 도서 관리 시스템 REST API
- 기술 스택: Spring Boot + Spring Security + Spring Data JPA + PostgreSQL + JWT
- 핵심 기능: 회원가입, 로그인, 도서 CRUD (간소화됨)
- 학습 중점: Spring Boot 핵심 개념 체험

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

#### Step 2: 설정 파일 관리 (45분)
1. **application.yml (YAML 설정)**
   ```yaml
   spring:
     datasource:
       url: jdbc:postgresql://localhost:5432/librarydb
       username: ${DB_USERNAME:defaultuser}
       password: ${DB_PASSWORD:defaultpass}
     jpa:
       hibernate:
         ddl-auto: update
       properties:
         hibernate:
           dialect: org.hibernate.dialect.PostgreSQLDialect
       show-sql: true

   jwt:
     secret: ${JWT_SECRET:your-secret-key}
     expiration: 3600000
   ```

2. **환경별 설정 파일**
   - `application-dev.yml` (개발 환경)
   - `application-prod.yml` (운영 환경)
   - 실행 시: `java -jar app.jar --spring.profiles.active=dev`

3. **IoC와 Dependency Injection**
   - @Component, @Service, @Repository 차이점 이해
   - @Autowired vs 생성자 주입

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

3. **Repository 계층 구조 이해**
   ```java
   // CrudRepository 기본 메서드 이해
   public interface BookRepository extends CrudRepository<Book, Long> {
       // save(), findById(), findAll(), deleteById() 등 기본 제공
   }

   // JpaRepository 확장 (페이징, 정렬 추가)
   public interface UserRepository extends JpaRepository<User, Long> {
       Optional<User> findByEmail(String email);  // Query Method
   }
   ```

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

#### Step 5: Controller와 REST API 구현 (1시간)
1. **매핑 어노테이션 상세 학습**
   ```java
   @RestController  // @Controller + @ResponseBody
   @RequestMapping("/api/books")  // 기본 경로 설정
   public class BookController {

       @GetMapping  // GET /api/books
       public List<Book> getAllBooks() { }

       @GetMapping("/{id}")  // GET /api/books/{id}
       public Book getBook(@PathVariable Long id) { }

       @PostMapping  // POST /api/books
       public Book createBook(@RequestBody BookDto bookDto) { }

       @PutMapping("/{id}")  // PUT /api/books/{id}
       public Book updateBook(@PathVariable Long id, @RequestBody BookDto bookDto) { }

       @DeleteMapping("/{id}")  // DELETE /api/books/{id}
       public void deleteBook(@PathVariable Long id) { }
   }
   ```

2. **간소화된 엔드포인트** (복잡도 감소)
   - POST /api/auth/register - 회원가입
   - POST /api/auth/login - 로그인
   - GET /api/books - 도서 목록 조회
   - POST /api/books - 도서 추가 (인증 필요)
   - GET /api/books/{id} - 도서 상세 조회
   - DELETE /api/books/{id} - 도서 삭제 (인증 필요)

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

#### Step 7: 테스트 및 검증 (30분)
1. **간단한 테스트 시나리오**
   - 회원가입 → 로그인 → JWT 토큰 획득
   - 토큰 없이 API 호출 (401 에러 확인)
   - 토큰으로 도서 조회/추가/삭제

2. **환경별 실행 테스트**
   ```bash
   # 개발 환경 실행
   mvn spring-boot:run -Dspring.profiles.active=dev

   # 운영 환경 실행
   java -jar target/book-library.jar --spring.profiles.active=prod
   ```

### 학습 포인트 체크리스트

#### 1. Spring Boot 기초 개념
- [x] 1-1. IoC와 DI 원리 이해
  🎯 IoC/DI를 아주 쉽게 다시 설명

  🍕 피자집 비유로 이해하기

  전통적인 방식 (IoC 없이):
  // 주방장이 직접 모든 재료를 준비
  public class 주방장 {
  public void 피자만들기() {
  도우 myDough = new 도우();      // 직접 만듦
  치즈 myCheese = new 치즈();      // 직접 만듦  
  토마토소스 mySauce = new 토마토소스(); // 직접 만듦

          // 피자 만들기...
      }
  }

  Spring 방식 (IoC/DI 사용):
  @Service
  public class 주방장 {
  private final 도우 dough;        // Spring이 준비해줌
  private final 치즈 cheese;       // Spring이 준비해줌
  private final 토마토소스 sauce;   // Spring이 준비해줌

      // Spring이 자동으로 재료를 주입해줌!
      public 주방장(도우 dough, 치즈 cheese, 토마토소스 sauce) {
          this.dough = dough;
          this.cheese = cheese;
          this.sauce = sauce;
      }
  }

  🔍 우리 프로젝트로 보기

  BookController는 BookService가 필요해요:

  @RestController
  public class BookController {
  private final BookService bookService;

      // Spring아, BookService 좀 줘!
      // Spring: OK! 내가 만들어서 줄게!
  }

  Spring이 하는 일:
    1. 앱 시작 → "어? @Service 붙은 BookService 발견!"
    2. BookService 객체 만들어서 창고(Container)에 보관
    3. "어? @RestController가 BookService 필요하네?"
    4. 창고에서 꺼내서 자동으로 연결!

  💡 핵심 정리

  IoC = 제어의 역전
    - Before: 내가 직접 new 해서 객체 만듦
    - After: Spring이 알아서 만들어줌

  DI = 의존성 주입
    - Before: 내가 필요한 거 직접 만듦
    - After: Spring이 필요한 거 자동으로 넣어줌

  왜 좋은가?
    1. 코드가 깔끔해짐 (new 안 써도 됨)
    2. 테스트하기 쉬워짐 (가짜 객체로 바꿔치기 가능)
    3. 유지보수 편함 (한 곳만 수정하면 됨)

- [ ] 1-2. Spring Boot 주요 Annotation 활용 (@RestController, @Service, @Repository)

#### 2. 프로젝트 설정 및 구성
- [ ] 2-1. Maven을 통한 의존성 관리
- [ ] 2-2. YAML 설정 파일 작성
- [ ] 2-3. Spring Profiles를 통한 환경별 설정 관리

#### 3. 데이터 계층 (JPA/Repository)
- [ ] 3-1. CrudRepository vs JpaRepository 계층 구조
- [ ] 3-2. Query Method 작성법

#### 4. 비즈니스 로직 계층
- [ ] 4-1. Service 계층의 역할과 책임

#### 5. Web/API 계층
- [ ] 5-1. HTTP 매핑 어노테이션 완벽 이해 (@GetMapping, @PostMapping 등)
- [ ] 5-2. REST API 설계 원칙 적용

#### 6. 보안 및 인증
- [ ] 6-1. Spring Security 동작 방식
- [ ] 6-2. JWT 토큰 기반 인증 구현

#### 7. 예외 처리
- [ ] 7-1. @ControllerAdvice를 통한 예외 처리

### 예상 완성 시간: 5-6시간 (복잡도 감소)

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