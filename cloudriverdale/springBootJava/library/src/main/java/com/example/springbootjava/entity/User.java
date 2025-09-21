package com.example.springbootjava.entity;

import jakarta.persistence.*;
import lombok.*;

@Entity // "이 클래스는 DB 테이블과 매핑되는 엔티티야"
@Table(name = "springBootJavaUsers")  // DB 테이블명을 'users'로 지정
@Getter // 모든 필드의 getter 메서드 자동 생성
@Setter // 모든 필드의 setter 메서드 자동 생성. 어노테이션이 없다면 직접 작성해야 함
@NoArgsConstructor // 기본 생성자: User()
@AllArgsConstructor // 모든 필드 생성자: User(id, email, password...)
@Builder // 빌더 패턴 자동 생성
public class User extends BaseEntity {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(nullable = false, unique = true, length = 50)
    private String email;

    @Column(nullable = false)
    private String password;

    @Column(nullable = false, length = 30)
    private String name;

    @Enumerated(EnumType.STRING)
    @Column(nullable = false)
    private UserRole role = UserRole.USER;

    @Column(nullable = false)
    private Boolean isActive = true;
}
