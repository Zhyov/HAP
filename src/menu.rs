use indexmap::IndexMap;
use std::io::{self, Write};
use crate::language::LanguageManager;
use crate::constants::{WELCOME_MESSAGE, VERSION, SELECT};
use crate::scripts::{Character,IPA};
use crate::utils::clear_screen;
use crate::scripts::{Variant, load_scripts};
use crate::pages::create_page;
use crate::ipa::convert_xsampa;

#[derive(Clone)]
pub enum MenuAction {
    Exit,
    Back,
    SetLanguage(String),
    OpenPage(Page),
    OpenScript(String),
    OpenCharacter(String),
    LoadVariations,
    OpenVariation(Variant),
}

#[derive(Clone)]
pub enum Page {
    Settings,
    LanguageSelection,
    Check,
}

#[derive(Clone)]
pub struct MenuOption {
    pub text: String,
    pub action: MenuAction,
}

pub struct Window<'a> {
    pub id: usize,
    pub options: Vec<MenuOption>,
    pub content: Vec<String>,
    pub characters: Option<IndexMap<String, Character>>,
    pub character: Option<Character>,
    pub variation: Option<Variant>,
    pub manager: &'a LanguageManager,
    pub welcome: bool,
    pub auto_translate: bool,
}

impl<'a> Window<'a> {
    pub fn new(next_window_id: &mut usize, options: Vec<MenuOption>, content: Vec<String>, manager: &'a LanguageManager, welcome: bool, auto_translate: bool) -> Self {
        let id = *next_window_id;
        *next_window_id += 1;

        Self {
            id,
            options,
            content,
            characters: None,
            character: None,
            variation: None,
            manager,
            welcome,
            auto_translate,
        }
    }

    fn invalid_input(&self) {
        clear_screen();
        println!("{}\n{}", self.manager.get_translation("invalidOption"), self.manager.get_translation("pressEnter"));

        let mut input  = String::new();
        io::stdin().read_line(&mut input).expect("Failed to read line");
    }

    fn render_content(&self) {
        if self.welcome { println!("{WELCOME_MESSAGE}{VERSION}\n"); }
        if let Some(character) = &self.character { self.render_character(character) }
        if let Some(variation) = &self.variation { self.render_variation(variation) }
        for text in &self.content {
            println!("{}", self.manager.get_translation(text));
        }
        println!();
    }

    fn build_options(&self) -> Vec<MenuOption> {
        let mut options = self.options.clone();

        if !self.welcome {
            options.push(MenuOption {
                text: String::from("back"),
                action: MenuAction::Back,
            });
        }

        options
    }

    fn render_options(&self, options: &[MenuOption]) {
        for (i, option) in options.iter().enumerate() {
            let mut rendered_option = option.text.clone();

            if self.auto_translate || i == options.len() - 1 {
                rendered_option = self.manager.get_translation(&option.text);
            }

            println!("{}) {rendered_option}", i + 1);
        }
    }

    fn read_selection(&self, options: &[MenuOption]) -> Option<MenuAction> {
        print!("\n{SELECT}");
        io::stdout().flush().unwrap();

        let mut input = String::new();
        io::stdin().read_line(&mut input).expect("Failed to read line");

        let selection: usize = match input.trim().parse() {
            Ok(value) => value,
            Err(_) => {
                self.invalid_input();
                return None
            }
        };

        if !(1..=options.len()).contains(&selection) {
            self.invalid_input();
            return None
        }

        Some(options[selection - 1].action.clone())
    }

    fn render_character(&self, character: &Character) {
        let displayed_character = if character.upper {
            format!("{}{}", character.character.to_uppercase(), character.character)
        } else {
            character.character.clone()
        };

        println!("{displayed_character}\n");

        if let Some(native) = &character.native {
            println!("{}: {native}", self.manager.get_translation("charName"))
        }

        let pronunciations = character.ipa
            .iter()
            .map(|ipa| format_ipa(ipa, self.manager))
            .collect::<Vec<String>>()
            .join(", ");

        println!("{}: {pronunciations}", self.manager.get_translation("charIPA"))
    }

    fn render_variation(&self, variation: &Variant) {
        println!("{}\n", variation.character);
        println!("{}: {}", self.manager.get_translation("variationEffect"), format_explanation(&variation.change, self.manager));
        
        let pronunciations = variation.ipa
            .iter()
            .map(|ipa| format_ipa(ipa, self.manager))
            .collect::<Vec<String>>()
            .join(", ");
        
        println!("{}: {pronunciations}", self.manager.get_translation("charIPA"))
    }

    /* pub fn close(&self, window_stack: &mut Vec<Window<'_>>) {
        if let Some(window) = window_stack.last() && window.id == self.id {
            window_stack.pop();
        }
    } */ // Practically not used, replaced by MenuAction::Back

    pub fn load(self, window_stack: &mut Vec<Window<'a>>, next_window_id: &mut usize) {
        let id = self.id;
        let manager = self.manager;
        
        window_stack.push(self);

        while window_stack.last().is_some_and(|window| window.id == id) {
            let action = {
                let window = window_stack.last().unwrap();

                clear_screen();
            
                window.render_content();
                let options = window.build_options();
            
                window.render_options(&options);
                window.read_selection(&options)
            };

            match action {
                Some(MenuAction::Exit) => {
                    std::process::exit(0)
                },
                Some(MenuAction::Back) => {
                    window_stack.pop(); // basically Window.close()
                },
                Some(MenuAction::SetLanguage(code)) => {
                    manager.set_language(&code);
                },
                Some(MenuAction::OpenPage(page)) => {
                    let window = create_page(page, manager, next_window_id);

                    window.load(window_stack, next_window_id);
                },
                Some(MenuAction::OpenScript(file)) => {
                    match load_scripts(&file) {
                        Ok(characters) => {
                            let mut options: Vec<MenuOption> = Vec::new();

                            for (key, character) in characters.iter() {
                                let mut text = character.character.to_string();
                                if character.upper {
                                    text = format!("{}{}", character.character.to_uppercase(), text);
                                }

                                options.push(MenuOption { text, action: MenuAction::OpenCharacter(key.clone()) });
                            }

                            let mut window = Window::new(
                                next_window_id,
                                options,
                                vec![
                                    String::from("whatCharacter")
                                ],
                                manager,
                                false,
                                false,
                            );

                            window.characters = Some(characters);
                            window.load(window_stack, next_window_id);
                        },
                        Err(e) => {
                            eprintln!("Failed to load script '{}': {e:?}", file);
                        }
                    };
                },
                Some(MenuAction::OpenCharacter(character)) => {
                    let script_window = window_stack
                        .iter()
                        .rev()
                        .find(|window| window.characters.is_some());

                    let characters = script_window.and_then(|window| window.characters.as_ref());
                    let selected_character = characters.and_then(|characters| characters.get(&character));
                    
                    if let Some(character) = selected_character {
                        let mut options = Vec::new();
                        if !character.variations.is_empty() {
                            options.push(MenuOption {
                                text: String::from("variations"),
                                action: MenuAction::LoadVariations,
                            });
                        }

                        let mut window = Window::new(
                            next_window_id,
                            options,
                            Vec::new(),
                            manager,
                            false,
                            true,
                        );

                        window.character = Some(character.clone());
                        window.load(window_stack, next_window_id);
                    }
                },
                Some(MenuAction::LoadVariations) => {
                    let variations = window_stack
                        .last()
                        .and_then(|window| window.character.as_ref())
                        .map(|character| character.variations.clone())
                        .unwrap_or_default();

                    let options = variations
                        .into_iter()
                        .map(|variation| MenuOption {
                            text: variation.character.clone(),
                            action: MenuAction::OpenVariation(variation),
                        })
                        .collect();

                    let window = Window::new(
                        next_window_id,
                        options,
                        vec![String::from("variations")],
                        manager,
                        false,
                        false,
                    );

                    window.load(window_stack, next_window_id);
                },
                Some(MenuAction::OpenVariation(variation)) => {
                    let mut window = Window::new(
                        next_window_id,
                        Vec::new(),
                        Vec::new(),
                        manager,
                        false,
                        false,
                    );

                    window.variation = Some(variation);
                    window.load(window_stack, next_window_id);
                }
                None => {},
            }
        }
    }
}

fn format_explanation(text: &str, manager: &LanguageManager) -> String {
    text.split('+')
        .map(|key| manager.get_translation(key))
        .collect::<Vec<String>>()
        .join(" + ")
}

fn format_ipa(ipa: &IPA, manager: &LanguageManager) -> String {
    let pronunciation = convert_xsampa(&ipa.xsampa);

    match &ipa.info {
        Some(info) => {
            format!("{pronunciation} ({})", format_explanation(info, manager))
        },
        None => pronunciation,
    }
}