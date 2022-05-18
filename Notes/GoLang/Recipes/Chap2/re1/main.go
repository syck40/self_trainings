package main

import (
	"fmt"
	"strings"
)

const refString = "Mary had a_little lamb"

func main() {
	lookFor := "lamab"
	contain := strings.ContainsAny(refString, lookFor)
	fmt.Println(contain)
	ab := strings.Split(refString, "_")
	for i, v := range ab {
		fmt.Printf("id: %v, v: %v\n", i, v)
	}
	splitFunc := func(r rune) bool {
		return strings.ContainsRune("*%,_", r)
	}
	words := strings.FieldsFunc(refString, splitFunc)
	for i, v := range words {
		fmt.Printf("Word is %v is %v\n", i, v)
	}
	ab = strings.Fields(refString)
	for _, v := range ab {
		fmt.Printf("Value is %v\n", v)
	}
}
