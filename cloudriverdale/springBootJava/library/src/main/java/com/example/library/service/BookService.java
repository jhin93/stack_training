package com.example.library.service;

import com.example.library.dto.BookDto;
import com.example.library.entity.Book;
import com.example.library.repository.BookRepository;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
@RequiredArgsConstructor
public class BookService {

    private final BookRepository bookRepository;

    public Book createBook(BookDto bookDto) {
        Book book = new Book();
        book.setIsbn(bookDto.getIsbn());
        book.setTitle(bookDto.getTitle());
        book.setAuthor(bookDto.getAuthor());
        return bookRepository.save(book);
    }

    public Book getBookById(Long id) {
        return bookRepository.findById(id)
            .orElseThrow(() -> new RuntimeException("Book not found"));
    }

    public List<Book> getAllBooks() {
        return (List<Book>) bookRepository.findAll();
    }

    public void deleteBook(Long id) {
        bookRepository.deleteById(id);
    }
}