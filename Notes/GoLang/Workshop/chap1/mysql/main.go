package main

import (
	"database/sql"
	"fmt"

	_ "github.com/go-sql-driver/mysql"
)

type Post struct {
	Id int
	Content string
	Author string
	Comments []Comment
}

type Comment struct {
	Id int
	Content string
	Author string
	Post *Post
}

var Db *sql.DB

func init(){
	var err error
	Db, err = sql.Open("mysql", "root:password@/gwp")
	if err != nil {
		panic(err)
	}
}

func GetPosts(){
	r, _ := Db.Query("select * from comments")
	fmt.Println(r.Columns())
	for r.Next() {
		fmt.Println(r)
	}
}

func main(){
	GetPosts()
}