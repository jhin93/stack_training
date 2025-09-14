package com.cloudriverdale.crm.entity;

import jakarta.persistence.*;
import java.time.LocalDateTime;

@Entity
@Table(name = "contact_histories")
public class ContactHistory extends BaseEntity {

    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "customer_id", nullable = false)
    private Customer customer;

    @Enumerated(EnumType.STRING)
    @Column(length = 20, nullable = false)
    private ContactType contactType;

    @Column(columnDefinition = "TEXT")
    private String notes;

    @Column(length = 100)
    private String contactedBy;

    private LocalDateTime contactDate;

    public ContactHistory() {
        this.contactDate = LocalDateTime.now();
    }

    public Customer getCustomer() {
        return customer;
    }

    public void setCustomer(Customer customer) {
        this.customer = customer;
    }

    public ContactType getContactType() {
        return contactType;
    }

    public void setContactType(ContactType contactType) {
        this.contactType = contactType;
    }

    public String getNotes() {
        return notes;
    }

    public void setNotes(String notes) {
        this.notes = notes;
    }

    public String getContactedBy() {
        return contactedBy;
    }

    public void setContactedBy(String contactedBy) {
        this.contactedBy = contactedBy;
    }

    public LocalDateTime getContactDate() {
        return contactDate;
    }

    public void setContactDate(LocalDateTime contactDate) {
        this.contactDate = contactDate;
    }
}