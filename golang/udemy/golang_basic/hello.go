package main

import "fmt"

var a int = 42

type hotdog int

var b hotdog

func main() {
	b = 13
	fmt.Printf("%T\n", b) // main.hotdog
	fmt.Printf("%d\n", b) // 43
}
