package main

import (
	"fmt"
	"net"
)

func main() {
	i, _ := net.Interfaces()
	//fmt.Println(i)
	for _, v := range(i) {
		ad, _ := v.Addrs()
		for _, v := range ad {
			if ip, ok := v.(*net.IPNet); ok {
				fmt.Printf("\t%v\n",ip)
			}
		}
	}
}
