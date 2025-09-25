use std::io; // input output library 'io' in a standard library 'std'
use rand::Rng; // 'rand' is crate, 'Rng' is a trait. 'Rng' is a trait that provides a random number generator.
use std::cmp::Ordering; // 'cmp' is a module, 'Ordering' is a type. Ordering is an enum that can be either Less, Equal, or Greater.

fn main() {
    println!("Guess the number!");

    let secret_number = rand::thread_rng().gen_range(1..=100);
    // 'rand::thread_rng()' gives a random number generator that is local to the current thread of execution and seeded by the operating system.
    // 'gen_range()' generates a random number in the range of 1 to 100(start..=end). It contains the start and end.

    // println!("The secret number is : {secret_number}");

    loop {
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

        let guess: u32 = match guess.trim().parse() { // 'parse' returns a Result. And the 'Result' is an enum that can be either 'Ok' or 'Err'.
            Ok(num) => num,
            Err(_) => continue,
            // '_' is a catch-all value. It means we don't care about the error value.
            // 'continue' skips the rest of the loop and starts a new iteration of the loop.
        };
        // Shadowing means the new variable 'guess' shadows the previous variable 'guess'.
        // 'trim()' removes any whitespace characters from the beginning and end of the string.
        // 'parse()' converts a string to another type. In this case, it's 'u32'. Because the declaration of 'guess' is 'u32', the string must be a valid number.
        // If the string is not a valid number, parse() will return an Err. .expect() will print the error message and exit the program.
        // 'u32' is an unsigned 32-bit integer

        println!("You guessed: {guess}");

        match guess.cmp(&secret_number) {
            // cmp() is a method for comparing two values. The standard is 'guess' and the argument is '&secret_number'.
            // If the guess is less than the secret number, it returns Less. If the guess is greater than the secret number, it returns Greater. If the guess is equal to the secret number, it returns Equal.
            Ordering::Less => println!("Too small!"),
            Ordering::Greater => println!("Too big!"),
            Ordering::Equal => {
                println!("You win!");
                break;
            },
        }
    }
}