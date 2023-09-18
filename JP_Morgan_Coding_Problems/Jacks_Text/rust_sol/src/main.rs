use std::collections::HashSet;
use std::io;

/// Runs the implementation for the Jack's text problem 
/// which is described in the python_sol `main.py` file
/// 
/// Arguments: 
/// - None
/// 
/// Returns:
/// - None
/// 
/// Helpful Resources: 
/// - `HashSet` help: [link](https://doc.rust-lang.org/std/collections/struct.HashSet.html)
/// - `to_lowercase()` reference: [link](https://doc.rust-lang.org/std/char/struct.ToLowercase.html)
fn main() {
    let mut sentence = String::new();
    io::stdin()
        .read_line(&mut sentence)
        .expect("Failed to read line");
    // must shadow sentence here because .trim() returns
    // &str type
    let sentence = sentence.trim();
    let sentence: Vec<&str> = sentence.split(" ").collect();
    let mut new_sentence = String::new();

    // deal with the first word
    let mut seen_words = HashSet::new();
    seen_words.insert(sentence[0].to_lowercase());

    new_sentence.push_str(sentence[0]);
    new_sentence.push_str(" ");

    for i in 1..sentence.len() {
        if seen_words.contains(sentence[i]) {
            continue;
        }
        else {
            new_sentence.push_str(sentence[i]);
            new_sentence.push_str(" ");
        }
    }
    println!("{}", new_sentence);
}

