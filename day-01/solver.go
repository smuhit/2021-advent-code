package main

import (
    "bufio"
    "os"
    "strconv"
    "fmt"
)


func readData() []int {
    f, _ := os.Open("input")
    defer f.Close()

    data := make([]int, 0)

    scanner := bufio.NewScanner(f)

    for scanner.Scan() {
    	rawData, _ := strconv.Atoi(scanner.Text())
    	data = append(data, rawData)
    }

    return data
}


func main() {
	data := readData()

	// Part 1
	count := 0
	for i, datum := range data[1:] {
		if datum > data[i] {
			count++
		}
	}
	fmt.Println(count)

	// Part 2
	count = 0
	for i, datum := range data[3:] {
		if datum + data[i + 2] + data[i + 1] > data[i] + data[i + 1] + data[i + 2] {
			count++
		}
	}
	fmt.Println(count)
}