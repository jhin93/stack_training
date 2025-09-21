package com.example.library.entity;

import jakarta.persistence.*;
import lombok.Data;
import java.util.Date;

@Entity
@Table(name = "books")
@Data
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