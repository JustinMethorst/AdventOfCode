use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;

fn process_arrays(first_data_array: &mut Vec<i32>, second_data_array: &mut Vec<i32>) -> Vec<i32> {
    // Sort both arrays in ascending order
    first_data_array.sort();
    second_data_array.sort();

    let mut result = Vec::new();

    // Continue processing while there are at least two elements left in both arrays
    while first_data_array.len() > 1 && second_data_array.len() > 1 {
        // Take the lowest two elements from each array
        let lowest_first_array = first_data_array.remove(0);
        let lowest_second_array = second_data_array.remove(0);

        // Calculate the difference and store it in the result array
        let difference = (lowest_first_array - lowest_second_array).abs();
        result.push(difference);
    }

    result
}

fn main() -> io::Result<()> {
    // Initialize the arrays for storing the data
    let mut first_part_data = Vec::new();
    let mut second_part_data = Vec::new();

    // Open the file and read it
    let path = Path::new("C:\\Projects\\AdventOfCode\\2024\\day1data.txt");
    let file = File::open(path)?;

    let reader = io::BufReader::new(file);
    
    // Read each line in the file
    for line in reader.lines() {
        if let Ok(line) = line {
            let parts: Vec<&str> = line.split_whitespace().collect();

            if parts.len() >= 2 {
                // Parse the first and second part and store them in the arrays
                if let (Ok(first), Ok(second)) = (parts[0].parse::<i32>(), parts[1].parse::<i32>()) {
                    first_part_data.push(first);
                    second_part_data.push(second);
                }
            }
        }
    }

    // Process the arrays and get the differences
    let differences = process_arrays(&mut first_part_data, &mut second_part_data);

    // Sum up all the differences to get one big integer
    let total_difference: i32 = differences.iter().sum();

    // Output the result
    println!("Total difference: {}", total_difference);

    Ok(())
}
