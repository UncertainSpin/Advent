package main

import (
	"fmt"
	"io/ioutil"
)

func check(e error) {
	if e != nil {
		panic(e)
	}
}

func read() {

	data, err := ioutil.ReadFile("input.txt")
	check(err)
	// fmt.Println(reflect.TypeOf(data)) # Yields uint8 Array
	fmt.Print(string(data))
}

func main() {

	fmt.Println("Day 1")
	read()
}
