package main

import (
	"fmt"
	"os"
	"text/tabwriter"
)
type person struct {
	name string
	age int
}
func main() {
	p := person{"jonnh", 32}
	fmt.Fprintln(os.Stdout, p)
	fmt.Printf("this is %#v\n", p)
	w := tabwriter.NewWriter(os.Stdout, 15, 0, 1, ' ', tabwriter.AlignRight)
	fmt.Fprintln(w, "username\tfirename\tlastname\t")
	w.Flush()
	args := os.Args
	for idx, arg := range args {
		fmt.Printf("Arg %v and %v \n", idx, arg)
	}
}
