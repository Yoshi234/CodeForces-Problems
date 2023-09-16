use std::io;

fn print_value(test_case: i32) {
    let value:i32 = (test_case-1)*10 + 2;
    println!("{}",value);
}

fn read_int32() -> i32 {
    let mut value = String::new();
    io::stdin()
        .read_line(&mut value)
        .expect("Failed to read line");
    let value = match value.trim().parse() {
        Ok(num) => num,
        Err(_) => -1,
    };
    if value < 0 {
        panic!("A positive integer value must be entered");
    } 
    value
}

fn handle_input() -> Vec<i32> {
    let num_tests = read_int32();
    let num_tests = num_tests as usize;

    let mut tests_vector = Vec::new();
    for _i in 0..num_tests {
        let test_case = read_int32();
        tests_vector.push(test_case);
    }

    tests_vector
}

fn main() {
    let test_cases = handle_input();

    for test in test_cases {
        print_value(test);
    }
}