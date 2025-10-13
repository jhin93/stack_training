package main

import "fmt"

type hotdog int

var a int
var b hotdog

func main() {
	b = 13
	a = int(b)            // convert to int. Because b is hotdog
	fmt.Printf("%T\n", b) // main.hotdog
	fmt.Printf("%d\n", a) // 13
	fmt.Printf("%d\n", b) // 13
}
