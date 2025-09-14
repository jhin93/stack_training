package com.cloudriverdale.crm.repository;

import com.cloudriverdale.crm.entity.Customer;
import com.cloudriverdale.crm.entity.CustomerStatus;
import com.cloudriverdale.crm.entity.CustomerType;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;
import org.springframework.stereotype.Repository;

import java.time.LocalDate;
import java.time.LocalDateTime;
import java.util.List;
import java.util.Optional;

@Repository
public interface CustomerRepository extends JpaRepository<Customer, Long> {

    Optional<Customer> findByEmail(String email);

    List<Customer> findByStatus(CustomerStatus status);

    List<Customer> findByType(CustomerType type);

    Page<Customer> findByStatusAndType(CustomerStatus status, CustomerType type, Pageable pageable);

    @Query("SELECT c FROM Customer c WHERE c.firstName LIKE %:keyword% OR c.lastName LIKE %:keyword% OR c.email LIKE %:keyword%")
    Page<Customer> searchCustomers(@Param("keyword") String keyword, Pageable pageable);

    @Query("SELECT c FROM Customer c WHERE c.createdAt BETWEEN :startDate AND :endDate")
    List<Customer> findCustomersCreatedBetween(@Param("startDate") LocalDateTime startDate,
                                               @Param("endDate") LocalDateTime endDate);

    @Query("SELECT c FROM Customer c WHERE c.dateOfBirth = :date")
    List<Customer> findByBirthDate(@Param("date") LocalDate date);

    @Query("SELECT COUNT(c) FROM Customer c WHERE c.status = :status")
    long countByStatus(@Param("status") CustomerStatus status);

    @Query("SELECT c FROM Customer c LEFT JOIN FETCH c.orders WHERE c.id = :id")
    Optional<Customer> findByIdWithOrders(@Param("id") Long id);

    @Query("SELECT c FROM Customer c LEFT JOIN FETCH c.contactHistories WHERE c.id = :id")
    Optional<Customer> findByIdWithContactHistories(@Param("id") Long id);

    List<Customer> findByCity(String city);

    List<Customer> findByCountry(String country);

    boolean existsByEmail(String email);

    Optional<Customer> findBySalesforceId(String salesforceId);

    @Query(value = "SELECT * FROM customers WHERE created_at >= CURRENT_DATE - INTERVAL '7 days'", nativeQuery = true)
    List<Customer> findRecentCustomers();

    @Query("SELECT c FROM Customer c WHERE SIZE(c.orders) > :orderCount")
    List<Customer> findCustomersWithMoreThanNOrders(@Param("orderCount") int orderCount);

    Page<Customer> findByFirstNameContainingIgnoreCaseOrLastNameContainingIgnoreCase(
            String firstName, String lastName, Pageable pageable);
}