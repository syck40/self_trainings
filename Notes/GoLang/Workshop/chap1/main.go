package main

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
	"net/http"
)
type NewsItem struct {
	Author string
	Content string
	Date string
	ImageUrl string
	ReadMoreUrl string
	Time string
	Title string
	Url string
}
type NewsRoot struct {
	Category string `json:"category"`
	Data []NewsItem `json:"data"`
	Sucess bool `json:"success"`
}

func main(){
	addr := "https://inshorts.deta.dev/news?category=technology"
	r, err := http.Get(addr)
	if err != nil {
		panic(err)
	}
	b, err := ioutil.ReadAll(r.Body)
	if err != nil {
		panic(err)
	}
	//fmt.Println(string(b))
	var obj NewsRoot
	json.Unmarshal(b, &obj)
	fmt.Println(obj.Category)
	for _, v := range obj.Data{
		fmt.Println(v.Title)
		fmt.Println(v.Content)
		fmt.Println()
	}
	//json.NewDecoder(b.)
	//bb, _ := json.MarshalIndent(obj,"","\t")
	//fmt.Println(string(bb))
}