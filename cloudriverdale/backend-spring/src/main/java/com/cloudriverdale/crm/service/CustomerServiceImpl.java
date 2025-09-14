package com.cloudriverdale.crm.service;

import com.cloudriverdale.crm.entity.Customer;
import com.cloudriverdale.crm.entity.CustomerStatus;
import com.cloudriverdale.crm.entity.CustomerType;
import com.cloudriverdale.crm.repository.CustomerRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.time.LocalDate;
import java.time.LocalDateTime;
import java.util.List;
import java.util.Optional;

@Service
@Transactional
public class CustomerServiceImpl implements CustomerService {

    private final CustomerRepository customerRepository;

    @Autowired
    public CustomerServiceImpl(CustomerRepository customerRepository) {
        this.customerRepository = customerRepository;
    }

    @Override
    public Customer createCustomer(Customer customer) {
        validateCustomer(customer);
        if (customerRepository.existsByEmail(customer.getEmail())) {
            throw new RuntimeException("Customer with email " + customer.getEmail() + " already exists");
        }
        return customerRepository.save(customer);
    }

    @Override
    public Customer updateCustomer(Long id, Customer customer) {
        Customer existingCustomer = customerRepository.findById(id)
                .orElseThrow(() -> new RuntimeException("Customer not found with id: " + id));

        updateCustomerFields(existingCustomer, customer);
        return customerRepository.save(existingCustomer);
    }

    @Override
    @Transactional(readOnly = true)
    public Optional<Customer> getCustomerById(Long id) {
        return customerRepository.findById(id);
    }

    @Override
    @Transactional(readOnly = true)
    public Optional<Customer> getCustomerByEmail(String email) {
        return customerRepository.findByEmail(email);
    }

    @Override
    @Transactional(readOnly = true)
    public Page<Customer> getAllCustomers(Pageable pageable) {
        return customerRepository.findAll(pageable);
    }

    @Override
    @Transactional(readOnly = true)
    public Page<Customer> searchCustomers(String keyword, Pageable pageable) {
        return customerRepository.searchCustomers(keyword, pageable);
    }

    @Override
    @Transactional(readOnly = true)
    public List<Customer> getCustomersByStatus(CustomerStatus status) {
        return customerRepository.findByStatus(status);
    }

    @Override
    @Transactional(readOnly = true)
    public List<Customer> getCustomersByType(CustomerType type) {
        return customerRepository.findByType(type);
    }

    @Override
    @Transactional(readOnly = true)
    public Page<Customer> getCustomersByStatusAndType(CustomerStatus status, CustomerType type, Pageable pageable) {
        return customerRepository.findByStatusAndType(status, type, pageable);
    }

    @Override
    @Transactional(readOnly = true)
    public List<Customer> getCustomersCreatedBetween(LocalDateTime startDate, LocalDateTime endDate) {
        return customerRepository.findCustomersCreatedBetween(startDate, endDate);
    }

    @Override
    @Transactional(readOnly = true)
    public List<Customer> getCustomersByBirthDate(LocalDate date) {
        return customerRepository.findByBirthDate(date);
    }

    @Override
    @Transactional(readOnly = true)
    public List<Customer> getCustomersByCity(String city) {
        return customerRepository.findByCity(city);
    }

    @Override
    @Transactional(readOnly = true)
    public List<Customer> getCustomersByCountry(String country) {
        return customerRepository.findByCountry(country);
    }

    @Override
    @Transactional(readOnly = true)
    public Optional<Customer> getCustomerWithOrders(Long id) {
        return customerRepository.findByIdWithOrders(id);
    }

    @Override
    @Transactional(readOnly = true)
    public Optional<Customer> getCustomerWithContactHistories(Long id) {
        return customerRepository.findByIdWithContactHistories(id);
    }

    @Override
    @Transactional(readOnly = true)
    public Optional<Customer> getCustomerBySalesforceId(String salesforceId) {
        return customerRepository.findBySalesforceId(salesforceId);
    }

    @Override
    public void deleteCustomer(Long id) {
        Customer customer = customerRepository.findById(id)
                .orElseThrow(() -> new RuntimeException("Customer not found with id: " + id));
        customer.setStatus(CustomerStatus.INACTIVE);
        customerRepository.save(customer);
    }

    @Override
    @Transactional(readOnly = true)
    public boolean existsByEmail(String email) {
        return customerRepository.existsByEmail(email);
    }

    @Override
    @Transactional(readOnly = true)
    public long countCustomersByStatus(CustomerStatus status) {
        return customerRepository.countByStatus(status);
    }

    @Override
    @Transactional(readOnly = true)
    public List<Customer> getRecentCustomers() {
        return customerRepository.findRecentCustomers();
    }

    @Override
    @Transactional(readOnly = true)
    public List<Customer> getTopCustomers(int orderCount) {
        return customerRepository.findCustomersWithMoreThanNOrders(orderCount);
    }

    @Override
    public void syncWithSalesforce(Long customerId, String salesforceId) {
        Customer customer = customerRepository.findById(customerId)
                .orElseThrow(() -> new RuntimeException("Customer not found with id: " + customerId));
        customer.setSalesforceId(salesforceId);
        customerRepository.save(customer);
    }

    private void validateCustomer(Customer customer) {
        if (customer.getFirstName() == null || customer.getFirstName().trim().isEmpty()) {
            throw new IllegalArgumentException("First name is required");
        }
        if (customer.getLastName() == null || customer.getLastName().trim().isEmpty()) {
            throw new IllegalArgumentException("Last name is required");
        }
        if (customer.getEmail() == null || customer.getEmail().trim().isEmpty()) {
            throw new IllegalArgumentException("Email is required");
        }
        if (!isValidEmail(customer.getEmail())) {
            throw new IllegalArgumentException("Invalid email format");
        }
    }

    private boolean isValidEmail(String email) {
        return email.matches("^[A-Za-z0-9+_.-]+@(.+)$");
    }

    private void updateCustomerFields(Customer existing, Customer updated) {
        if (updated.getFirstName() != null) {
            existing.setFirstName(updated.getFirstName());
        }
        if (updated.getLastName() != null) {
            existing.setLastName(updated.getLastName());
        }
        if (updated.getEmail() != null && !updated.getEmail().equals(existing.getEmail())) {
            if (customerRepository.existsByEmail(updated.getEmail())) {
                throw new RuntimeException("Email already exists: " + updated.getEmail());
            }
            existing.setEmail(updated.getEmail());
        }
        if (updated.getPhoneNumber() != null) {
            existing.setPhoneNumber(updated.getPhoneNumber());
        }
        if (updated.getDateOfBirth() != null) {
            existing.setDateOfBirth(updated.getDateOfBirth());
        }
        if (updated.getAddress() != null) {
            existing.setAddress(updated.getAddress());
        }
        if (updated.getCity() != null) {
            existing.setCity(updated.getCity());
        }
        if (updated.getState() != null) {
            existing.setState(updated.getState());
        }
        if (updated.getPostalCode() != null) {
            existing.setPostalCode(updated.getPostalCode());
        }
        if (updated.getCountry() != null) {
            existing.setCountry(updated.getCountry());
        }
        if (updated.getStatus() != null) {
            existing.setStatus(updated.getStatus());
        }
        if (updated.getType() != null) {
            existing.setType(updated.getType());
        }
        if (updated.getNotes() != null) {
            existing.setNotes(updated.getNotes());
        }
    }
}