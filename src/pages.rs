use crate::menu::{Window, MenuOption, MenuAction, Page};
use crate::language::LanguageManager;
use crate::scripts::load_scripts_manifest;

pub fn create_page<'a>(page: Page, manager: &'a LanguageManager, next_window_id: &mut usize) -> Window<'a> {
    match page {
        Page::Settings => {
            Window::new(
                next_window_id,
                vec![
                    MenuOption {
                        text: String::from("settingsLanguage"),
                        action: MenuAction::OpenPage(Page::LanguageSelection),
                    },
                ],
                vec![
                    String::from("whatDo")
                ],
                manager,
                false,
                true,
            )
        },
        Page::LanguageSelection => {
            let language_options = manager.get_languages();

            let options = language_options
                .into_iter()
                .map(|language| MenuOption {
                    text: language.text,
                    action: MenuAction::SetLanguage(language.code),
                })
                .collect();

            Window::new(
                next_window_id,
                options,
                vec![
                    String::from("selectLanguage")
                ],
                manager,
                false,
                true,
            )
        },
        Page::Check => {
            let manifest = match load_scripts_manifest() {
                Ok(manifest) => manifest,
                Err(e) => {
                    eprintln!("Failed to load scripts manifest file: {e:?}");
                    Vec::new()
                }
            };

            let options = manifest
                .into_iter()
                .map(|script| MenuOption {
                    text: script.name,
                    action: MenuAction::OpenScript(script.file),
                })
                .collect();

            Window::new(
                next_window_id,
                options,
                vec![
                    String::from("whatCheck")
                ],
                manager,
                false,
                true,
            )
        },
    }
}