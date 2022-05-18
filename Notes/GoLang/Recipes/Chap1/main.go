package main

import (
	"flag"
	"fmt"
	"log"
	"os"
	"strings"
)
type ArrayValue []string
func (s *ArrayValue) String() string{
	return fmt.Sprintf("%v", *s)
}
func (a *ArrayValue) Set(s string) error {
	*a = strings.Split(s, ",")
	return nil
}
func main() {
	retry := flag.Int("retry", -1, "Max retry count")
	var logPrefix string
	flag.StringVar(&logPrefix, "prefix","", "Logger prefix")
	var arr ArrayValue
	flag.Var(&arr, "array", "Input array to iterate")
	flag.Parse()
	logger := log.New(os.Stdout, logPrefix, log.Ldate)
	retryCount := 0
	for *retry > retryCount {
		logger.Println("Retrying connection")
		logger.Printf("Sending array %v\n", arr)
		retryCount++
	}
}
