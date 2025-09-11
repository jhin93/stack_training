  package com.cloudriverdale.crm.entity;

  import jakarta.persistence.*;

  @Entity  // 이 클래스가 JPA 엔티티임을 표시 (customer 테이블로 매핑됨)
  @Table(name = "customers")  // 테이블 이름 명시적 지정 (선택사항)
  public class Customer extends BaseEntity {  // BaseEntity 상속받아 id, createdAt, updatedAt 자동 포함

      // Customer만의 고유 필드들
      @Column(nullable = false, length = 100)
      private String name;  // 고객 이름

      @Column(unique = true, nullable = false)
      private String email;  // 고객 이메일 (중복 불가)

      @Column(length = 20)
      private String phoneNumber;  // 전화번호

      @Column(columnDefinition = "TEXT")
      private String address;  // 주소 (긴 텍스트)

      // 기본 생성자 (JPA 필수)
      public Customer() {
      }

      // 생성자 (선택사항)
      public Customer(String name, String email) {
          this.name = name;
          this.email = email;
      }

      public String getName() { return name; }
      public void setName(String name) { this.name = name; }
    
      public String getEmail() { return email; }
      public void setEmail(String email) { this.email = email; }
    
      public String getPhoneNumber() { return phoneNumber; }
      public void setPhoneNumber(String phoneNumber) {
      this.phoneNumber = phoneNumber; }
    
      public String getAddress() { return address; }
      public void setAddress(String address) { this.address = address; }
  }

