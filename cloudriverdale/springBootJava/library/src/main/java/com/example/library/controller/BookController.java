package com.example.library.controller;

import com.example.library.dto.BookDto;
import com.example.library.entity.Book;
import com.example.library.service.BookService;
import lombok.RequiredArgsConstructor;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/api/books")
@RequiredArgsConstructor
public class BookController {

    private final BookService bookService;

    @GetMapping
    public List<Book> getAllBooks() {
        return bookService.getAllBooks();
    }

    @GetMapping("/{id}")
    public Book getBook(@PathVariable Long id) {
        return bookService.getBookById(id);
    }

    @PostMapping
    public Book createBook(@RequestBody BookDto bookDto) {
        return bookService.createBook(bookDto);
    }

    @PutMapping("/{id}")
    public Book updateBook(@PathVariable Long id, @RequestBody BookDto bookDto) {
        Book book = bookService.getBookById(id);
        book.setIsbn(bookDto.getIsbn());
        book.setTitle(bookDto.getTitle());
        book.setAuthor(bookDto.getAuthor());
        return book;
    }

    @DeleteMapping("/{id}")
    public void deleteBook(@PathVariable Long id) {
        bookService.deleteBook(id);
    }
}