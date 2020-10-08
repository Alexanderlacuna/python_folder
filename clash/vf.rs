use std::cmp::Ordering;
fn main(){

	let mut guess=String::new();
	std::io::stdin().read_line(&mut guess).expect("Failed to readline");
	let guess:i32=guess.trim().parse().expect("error while trying to parse");
	let secret=45;
	println!("use has typed {:?}",guess);
    match guess.cmp(&secret){
    	Ordering::Less=>println!("to small"),
    	Ordering::Equal=>println!("holy cow you got it right"),
    	Ordering::Greater=>println!("to bigg")
    }
}