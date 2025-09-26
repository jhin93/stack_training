fn main() {
    // mut
    let mut y = 5;
    println!("mut y result : {y}");
    y = 6;
    println!("mut y result : {y}");

    // shadowing
    let x = 5;

    let x = x + 1;

    let x = x + 4;

    {
        let x = x * 2;
        println!("The value of x in the inner scope is: {x}"); // 20
    }

    println!("The value of x is: {x}"); // 10


}