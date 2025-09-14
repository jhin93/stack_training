package com.cloudriverdale.crm.service;

import com.cloudriverdale.crm.entity.Customer;
import com.cloudriverdale.crm.entity.CustomerStatus;
import com.cloudriverdale.crm.entity.CustomerType;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;

import java.time.LocalDate;
import java.time.LocalDateTime;
import java.util.List;
import java.util.Optional;

public interface CustomerService {

    Customer createCustomer(Customer customer);

    Customer updateCustomer(Long id, Customer customer);

    Optional<Customer> getCustomerById(Long id);

    Optional<Customer> getCustomerByEmail(String email);

    Page<Customer> getAllCustomers(Pageable pageable);

    Page<Customer> searchCustomers(String keyword, Pageable pageable);

    List<Customer> getCustomersByStatus(CustomerStatus status);

    List<Customer> getCustomersByType(CustomerType type);

    Page<Customer> getCustomersByStatusAndType(CustomerStatus status, CustomerType type, Pageable pageable);

    List<Customer> getCustomersCreatedBetween(LocalDateTime startDate, LocalDateTime endDate);

    List<Customer> getCustomersByBirthDate(LocalDate date);

    List<Customer> getCustomersByCity(String city);

    List<Customer> getCustomersByCountry(String country);

    Optional<Customer> getCustomerWithOrders(Long id);

    Optional<Customer> getCustomerWithContactHistories(Long id);

    Optional<Customer> getCustomerBySalesforceId(String salesforceId);

    void deleteCustomer(Long id);

    boolean existsByEmail(String email);

    long countCustomersByStatus(CustomerStatus status);

    List<Customer> getRecentCustomers();

    List<Customer> getTopCustomers(int orderCount);

    void syncWithSalesforce(Long customerId, String salesforceId);
}