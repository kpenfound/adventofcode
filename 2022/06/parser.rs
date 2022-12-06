use std::fs::File;
use std::io::prelude::*;
use std::path::Path;
use std::convert::TryInto;

fn main() {
    let path = Path::new("/input.txt");
    let display = path.display();

    let mut file = match File::open(&path) {
        Err(why) => panic!("couldn't open {}: {}", display, why),
        Ok(file) => file,
    };

    let mut s = String::new();
    match file.read_to_string(&mut s) {
        Err(why) => panic!("couldn't read {}: {}", display, why),
        Ok(_) => print!("{}", parser(s)),
    }
}

fn parser(input: String) -> u32 {
  let window = 14;
  let mut n = window - 1;
  while n < input.chars().count() {
    let mut substr: Vec<char> = input.chars().skip(n-(window-1)).take(window).collect();
    substr.sort();
    substr.dedup();
    if substr.len() == window {
      return (n+1).try_into().unwrap();
    }
    n+=1;
  }
  return 0;
}
