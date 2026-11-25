mod language;
mod scripts;
mod config;
mod ipa;
mod menu;
mod constants;
mod utils;
mod pages;
mod paths;
mod data;

use std::io::stdin;
use language::{LanguageManager, load_languages};
use menu::Window;
use crate::menu::{MenuAction, MenuOption, Page};

fn main() {
    let mut next_window_id: usize = 0;
    let mut window_stack: Vec<Window> = Vec::new();

    let mut warnings: Vec<String> = Vec::new();

    if crate::constants::FORCE_UPDATE {
        match data::load_online_data_manifest() {
            Ok(manifest) => {
                match data::is_hap_update_available(&manifest) {
                    Ok(true) => warnings.push(String::from("hapUpdateAvailable")),
                    Ok(false) => {},
                    Err(e) => warnings.push(e.translation_key().to_string()),
                }

                if let Err(e) = data::update_data_with_manifest(&manifest) {
                    warnings.push(e.translation_key().to_string());
                }
            },
            Err(e) => warnings.push(e.translation_key().to_string()),
        }
    } else {
        warnings.push(String::from("test"));
    }


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

    let mut menu = Window::new(&mut next_window_id, options, content, &language_manager, true, true);
    menu.warning = warnings;

    // This is for debugging errors
    /* let mut input = String::new();
    stdin().read_line(&mut input).expect("temp"); */

    menu.load(&mut window_stack, &mut next_window_id);
}