use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;

fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
where P: AsRef<Path>, {
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}

fn read_data() -> Vec<String> {
    let mut data = Vec::new();

    if let Ok(lines) = read_lines("./input") {
        for line in lines {
            if let Ok(raw_datum) = line {
                data.push(raw_datum);
            }
        }
    }
    data
}

fn part_one(horiz: i32, depth: i32, line: &String) -> (i32, i32) {
    let mut parts = line.split_whitespace();
    let verb = parts.next().unwrap();
    let amount = parts.next().unwrap().parse::<i32>().unwrap();

    let mut t_horiz = horiz;
    let mut t_depth = depth;

    match verb {
        "forward" => t_horiz += amount,
        "down" => t_depth += amount,
        "up" => t_depth -= amount,
        _ => (),
    }

    (t_horiz, t_depth)
}

fn part_two(horiz: i32, depth: i32, aim: i32, line: &String) -> (i32, i32, i32) {
    let mut parts = line.split_whitespace();
    let verb = parts.next().unwrap();
    let amount = parts.next().unwrap().parse::<i32>().unwrap();

    let mut t_horiz = horiz;
    let mut t_depth = depth;
    let mut t_aim = aim;

    match verb {
        "forward" => {
            t_horiz += amount;
            t_depth += amount * aim;
        }
        "down" => t_aim += amount,
        "up" => t_aim -= amount,
        _ => (),
    }

    (t_horiz, t_depth, t_aim)
}

fn main() {
    let data = read_data();

    // Part 1
    let mut horiz = 0;
    let mut depth = 0;

    for line in data.iter() {
        let res = part_one(horiz, depth, line);
        horiz = res.0;
        depth = res.1;
    }
    println!("{}", horiz * depth);

    // Part 2
    horiz = 0;
    depth = 0;
    let mut aim = 0;

    for line in data.iter() {
        let res = part_two(horiz, depth, aim, line);
        horiz = res.0;
        depth = res.1;
        aim = res.2;
    }
    println!("{}", horiz * depth);

}