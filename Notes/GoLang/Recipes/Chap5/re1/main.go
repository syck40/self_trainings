package main

import (
	"fmt"
	"io"
	"io/ioutil"
	"os"
	"os/exec"
)

func main() {
	// var name string
	// fmt.Println("What's your name?")
	// fmt.Scanf("%s\n", &name)
	// fmt.Println("Age?")
	// var age int
	// fmt.Scanf("%d\n", &age)
	// fmt.Printf("Name is %v, Age is %v\n", name, age)

	// sc := bufio.NewScanner(os.Stdin)
	// for sc.Scan() {
	// 	txt := sc.Text()
	// 	fmt.Printf("Echo: %v\n", txt)
	// }
	// for {
	// 	data := make([]byte, 8)
	// 	n, err := os.Stdin.Read(data)
	// 	if err != nil {
	// 		panic(err)
	// 	}
	// 	if n > 0 {
	// 		fmt.Printf("Received %v %v\n", data, string(data))
	// 	}
	// }

	f, err := os.Open("temp/file.txt")
	if err != nil {
		panic(err)
	}
	fi, _ := f.Stat()
	fmt.Printf("File is %v\n", fi.Size())

	c, err := ioutil.ReadAll(f)
	if err != nil {
		panic(err)
	}
	fmt.Printf("Content is: \"%v \n", string(c))
	f.Close()
	ff, _ := os.Create("testfile")
	defer ff.Close()
	io.WriteString(ff, "Creating new file content.\n")

	dr, _ := ioutil.TempDir(".", "goat")
	defer os.Remove(dr)
	fmt.Println(dr)
	fff, _ := ioutil.TempFile(".", "goatfile-")
	defer os.Remove(fff.Name())
	fmt.Println(fff.Name())
	fff.WriteString("This is in tmp file")
	cc, _ := ioutil.ReadAll(fff)
	fmt.Println(string(cc))

	pR, pW := io.Pipe()
	cmd := exec.Command("/bin/zsh","-c", "ls -al")
	//cmd.Stdout = os.Stdout
	cmd.Stdout = pW
	go func() {
		defer pR.Close()
		io.Copy(os.Stdout, pR)
	}()
	cmd.Run()
}
