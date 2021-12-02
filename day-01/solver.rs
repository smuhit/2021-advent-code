use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;


fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
where P: AsRef<Path>, {
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}

fn read_data() -> Vec<i32> {
    let mut data = Vec::new();

    if let Ok(lines) = read_lines("./input") {
        for line in lines {
            if let Ok(raw_datum) = line {
                data.push(raw_datum.parse::<i32>().unwrap());
            }
        }
    }
    data
}

fn main() {
    let data = read_data();

    // Part 1
    let mut count = 0;
    for (i, datum) in data.iter().skip(1).enumerate() {
        if datum > &data[i] {
            count += 1;
        }
    }
    println!("{}", count);

    // Part 2
    count = 0;
    for (i, datum) in data.iter().skip(3).enumerate() {
        if datum + &data[i+1] + &data[i+2] > &data[i] + &data[i+1] + &data[i+2] {
            count += 1;
        }
    }
    println!("{}", count);

}