package main

import (
    "bufio"
    "os"
    "strings"
    "strconv"
    "fmt"
)


func readData() []string {
    f, _ := os.Open("input.txt")
    defer f.Close()

    data := make([]string, 0)

    scanner := bufio.NewScanner(f)

    for scanner.Scan() {
        data = append(data, scanner.Text())
    }

    return data
}

func partOne(horiz int, depth int, line string) (int, int) {
    pieces := strings.Fields(line)
    verb := pieces[0]
    amount, _ := strconv.Atoi(pieces[1])
    switch verb {
    case "forward":
        horiz += amount
    case "down":
        depth += amount
    case "up":
        depth -= amount
    }
    return horiz, depth
}

func partTwo(horiz int, depth int, aim int, line string) (int, int, int) {
    pieces := strings.Fields(line)
    verb := pieces[0]
    amount, _ := strconv.Atoi(pieces[1])
    switch verb {
    case "forward":
        horiz += amount
        depth += aim * amount
    case "down":
        aim += amount
    case "up":
        aim -= amount
    }
    return horiz, depth, aim
}

func main() {
    data := readData()

    // Part 1
    horiz := 0
    depth := 0
    for _, line := range data {
        horiz, depth = partOne(horiz, depth, line)
    }
    fmt.Println(horiz * depth)

    // Part 2
    horiz = 0
    depth = 0
    aim := 0
    for _, line := range data {
        horiz, depth, aim = partTwo(horiz, depth, aim, line)
    }
    fmt.Println(horiz * depth)

}