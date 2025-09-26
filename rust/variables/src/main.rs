fn main() {
    let tup = (500, 6.4, 1);
    let (_x, _y, z) = tup;
    println!("The value of y is : {z}");
}