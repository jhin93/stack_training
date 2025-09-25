use std::io; // input output library 'io' in a standard library 'std'

fn main() {
    println!("Guess the number!");

    println!("Please input your guess.");

    let mut guess = String::new();
    // 'mut' makes a mutable variable. The variable in Rust can't be changed after it's been declared.
    // 'String::new()' creates a new empty string.

    io::stdin() // std::io::stdin() can be used instead of use std::io;
        .read_line(&mut guess)
        // '&' is also immutable. '&mut' makes a mutable reference.
        // 'read_line()' returns a Result. The result is an enum that can be either Ok or Err.
        .expect("Failed to read line");
        // If the result is Err, expect() will print the error message and exit the program.

    println!("You guessed: {guess}");
}