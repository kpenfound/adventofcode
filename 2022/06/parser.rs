use std::fs::File;
use std::io::prelude::*;
use std::path::Path;
use std::convert::TryInto;

fn main() {
    // Create a path to the desired file
    let path = Path::new("/input.txt");
    let display = path.display();

    // Open the path in read-only mode, returns `io::Result<File>`
    let mut file = match File::open(&path) {
        Err(why) => panic!("couldn't open {}: {}", display, why),
        Ok(file) => file,
    };

    // Read the file contents into a string, returns `io::Result<usize>`
    let mut s = String::new();
    match file.read_to_string(&mut s) {
        Err(why) => panic!("couldn't read {}: {}", display, why),
        Ok(_) => print!("{}", parser(s)),
    }

    // `file` goes out of scope, and the "hello.txt" file gets closed
}

fn parser(input: String) -> u32 {
  let mut n = 3;
  let window = 4;
  while n < input.chars().count() {
    let mut substr: Vec<char> = input.chars().skip(n-3).take(window).collect();
    substr.sort();
    substr.dedup();
    if substr.len() == window {
      return (n+1).try_into().unwrap();
    }
    n+=1;
  }
  return 0;
}
