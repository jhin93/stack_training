package com.example.springbootjava.repository;

import com.example.springbootjava.entity.User;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;
import org.springframework.stereotype.Repository;

import java.util.List;
import java.util.Optional;

@Repository
public interface UserRepository extends JpaRepository<User, Long> {

    // 이메일로 사용자 찾기
    Optional<User> findByEmail(String email);

    // 이메일 존재 여부 확인
    boolean existsByEmail(String email);

    // 활성 사용자만 조회
    List<User> findByIsActiveTrue();

    // JPQL 사용 예시
    @Query("SELECT u FROM User u WHERE u.name LIKE %:keyword%")
    List<User> searchByName(@Param("keyword") String keyword);

    // Native Query 사용 예시
    @Query(value = "SELECT * FROM users WHERE role = :role", nativeQuery =
            true)
    List<User> findByRoleNative(@Param("role") String role);
}
