package main

import (
	"fmt"
	"math/rand"
	"strconv"
	"time"
)

const bin = "00001"
const hex = "2f"
const intString = "12"
const floatString = "12.3"

func main() {
	res, err := strconv.Atoi(intString)
	if err != nil {
		panic(err)
	}
	fmt.Printf("Parsed int: %d, is type %T\n", res, res)
	res64, err := strconv.ParseFloat(floatString, 64)
	if err != nil {
		panic(err)
	}
	fmt.Println(res64)
	sec1 := rand.Intn(110)
	fmt.Println(rand.Intn(200))
	fmt.Println(sec1)
	fmt.Println(rand.New(rand.NewSource(time.Now().Unix())).Intn(100))

	fmt.Println(time.Now().Format("2006/01/02/15:04"))
	t, err := time.Parse("2006/01/02/15:04", "2006/01/02/15:04")
	if err != nil {
		panic(err)
	}
	fmt.Println(t)

	fmt.Println(time.Unix(0,0))
	fmt.Println(time.Now().Unix())

	tt := time.Date(2022, 5, 11, 14, 14, 14, 14, time.Local)
	fmt.Printf("Time %v, Day %v, Days %v\n", tt, tt.Day(), tt.YearDay())
	fmt.Printf("Advanced to %v\n", tt.AddDate(0,-1,-1))
	fmt.Printf("Until %v\n", time.Until(tt))
	fmt.Printf("Since %v\n", time.Since(time.Now().Add(-55)))
}
