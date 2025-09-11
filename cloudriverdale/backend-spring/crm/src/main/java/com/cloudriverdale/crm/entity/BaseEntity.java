package com.cloudriverdale.crm.entity;
import jakarta.persistence.*;
import org.springframework.data.annotation.CreatedDate;
import org.springframework.data.annotation.LastModifiedDate;
import org.springframework.data.jpa.domain.support.AuditingEntityListener;
import java.time.LocalDateTime;


// Entity 패키지와 BaseEntity 클래스의 역할
// 
//   1. Entity 패키지의 역할
// 
//   Entity 패키지는 데이터베이스 테이블과 매핑되는 Java 클래스들을 모아두는 
//   곳입니다.
// 
//   - 데이터베이스 테이블 = Java 클래스 매핑
//     - 예: Customer 클래스 → customer 테이블
//     - 예: Order 클래스 → order 테이블
//   - 왜 별도 패키지로 분리?
//     - 코드 구조화: 데이터베이스 관련 클래스들을 한 곳에 모음
//     - 유지보수 용이: 테이블 구조 변경 시 찾기 쉬움
//     - 계층 분리: MVC 패턴에서 Model 역할
// 
//   2. BaseEntity 클래스의 역할
// 
//   BaseEntity는 모든 엔티티가 공통으로 가져야 할 필드들을 정의한 부모 
//   클래스입니다.
// 
//   공통 필드들:
//   - id: 모든 테이블의 기본키 (Primary Key)
//   - createdAt: 레코드 생성 시간 (언제 만들어졌나?)
//   - updatedAt: 레코드 수정 시간 (언제 수정되었나?)
// 
//   왜 필요한가?
//   // BaseEntity 없이 작성하면:
//   @Entity
//   public class Customer {
//       @Id
//       private Long id;          // 중복 코드
//       private LocalDateTime createdAt;  // 중복 코드
//       private LocalDateTime updatedAt;  // 중복 코드
//       private String name;
//       private String email;
//   }
// 
//   @Entity
//   public class Order {
//       @Id
//       private Long id;          // 또 중복
//       private LocalDateTime createdAt;  // 또 중복
//       private LocalDateTime updatedAt;  // 또 중복
//       private BigDecimal amount;
//   }
// 
//   // BaseEntity 사용하면:
//   @Entity
//   public class Customer extends BaseEntity {
//       private String name;      // 고유 필드만 작성
//       private String email;
//   }
// 
//   @Entity
//   public class Order extends BaseEntity {
//       private BigDecimal amount;  // 고유 필드만 작성
//   }
// 
//   실무적 이점:
//   1. 코드 중복 제거: DRY (Don't Repeat Yourself) 원칙
//   2. 일관성: 모든 테이블이 동일한 audit 필드 보유
//   3. 유지보수: 공통 필드 변경 시 한 곳만 수정
//   4. 감사(Audit): 누가, 언제 데이터를 생성/수정했는지 추적
// 
//   이런 이유로 거의 모든 Spring Boot 프로젝트에서 BaseEntity를 만들어 사용합니다!


// @MappedSuperclass: 이 클래스 자체는 테이블로 만들지 않고, 다른 엔티티들이 상속받아 사용할 부모 클래스임을 표시
// 즉, BaseEntity 테이블은 생성되지 않고, Customer/Order 등이 이 필드들을 상속받아 각자의 테이블에 포함시킴
@MappedSuperclass

// @EntityListeners: 엔티티의 생명주기 이벤트(생성/수정/삭제 등)를 감지하는 리스너 등록
// AuditingEntityListener.class: Spring이 제공하는 감사(Audit) 기능 리스너
// 이 리스너가 @CreatedDate, @LastModifiedDate 어노테이션을 찾아서 자동으로 날짜를 입력해줌
@EntityListeners(AuditingEntityListener.class)

// abstract class: 추상 클래스로 선언하여 직접 인스턴스 생성 방지 (new BaseEntity() 불가능)
// BaseEntity는 오직 상속용으로만 사용됨
public abstract class BaseEntity {
    
    // @Id: 이 필드가 테이블의 기본키(Primary Key)임을 표시
    @Id
    // @GeneratedValue: 기본키 값을 자동으로 생성
    // GenerationType.IDENTITY: 데이터베이스의 AUTO_INCREMENT(MySQL) 또는 SERIAL(PostgreSQL) 기능 사용
    // 즉, 새 레코드 저장 시 1, 2, 3... 순서대로 자동 증가
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;  // 모든 테이블의 고유 식별자 (Primary Key)
    
    // @CreatedDate: JPA Auditing 기능으로 엔티티 최초 생성 시 현재 시간 자동 입력
    // 한 번 설정되면 변경되지 않음
    @CreatedDate
    // @Column: 데이터베이스 컬럼의 속성 정의
    // nullable = false: NULL 값 허용 안 함 (필수 값)
    // updatable = false: UPDATE 쿼리에서 이 컬럼은 수정 불가 (생성 시간은 변경되면 안 되므로)
    @Column(nullable = false, updatable = false)
    private LocalDateTime createdAt;  // 레코드 생성 시간 (예: 2024-12-27 10:30:00)
    
    // @LastModifiedDate: JPA Auditing 기능으로 엔티티 수정 시마다 현재 시간으로 자동 갱신
    // 처음 생성 시에도 값이 설정되고, 이후 수정할 때마다 갱신됨
    @LastModifiedDate
    private LocalDateTime updatedAt;  // 마지막 수정 시간 (예: 2024-12-27 15:45:30)
    
    // 1. id 필드의 getter/setter
    public Long getId() { // id 필드가 private Long id;로 선언되어 있으므로, getter도 같은 타입 Long을 반환
      return id;  // 현재 id 값을 반환
    }
    
    public void setId(Long id) {
        this.id = id;  // 전달받은 값을 id 필드에 저장
    }
    
    // 2. createdAt 필드의 getter/setter
    public LocalDateTime getCreatedAt() {
        return createdAt;  // 생성 시간 반환
    }
    
    public void setCreatedAt(LocalDateTime createdAt) {
        this.createdAt = createdAt;  // 생성 시간 설정
    }
    
    // 3. updatedAt 필드의 getter/setter
    public LocalDateTime getUpdatedAt() {
        return updatedAt;  // 수정 시간 반환
    }
    
    public void setUpdatedAt(LocalDateTime updatedAt) {
        this.updatedAt = updatedAt;  // 수정 시간 설정
    }


}