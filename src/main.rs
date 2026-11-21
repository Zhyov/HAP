mod language;
mod scripts;
mod config;
mod ipa;
mod menu;
mod constants;
mod utils;
mod pages;

use language::{LanguageManager, load_languages};
use menu::Window;
use crate::menu::{MenuOption, MenuAction, Page};

fn main() {
    let mut next_window_id: usize = 0;
    let mut window_stack: Vec<Window> = Vec::new();

    let config = config::load();
    let language_manager = LanguageManager::new(config.language, load_languages());

    let options: Vec<MenuOption> = vec![
        MenuOption { text: String::from("menuCheck"), action: MenuAction::OpenPage(Page::Check) },
        MenuOption { text: String::from("menuSettings"), action: MenuAction::OpenPage(Page::Settings) },
        MenuOption { text: String::from("exit"), action: MenuAction::Exit }
    ];

    let content: Vec<String> = vec![
        String::from("whatDo")
    ];

    let menu = Window::new(&mut next_window_id, options, content, &language_manager, true, true);
    menu.load(&mut window_stack, &mut next_window_id);
}