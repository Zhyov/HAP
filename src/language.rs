use std::collections::HashMap;
use indexmap::IndexMap;
use serde::{Serialize, Deserialize};
use std::fs::{read_dir, File};
use std::path::Path;
use std::cell::RefCell;
use crate::config::Config;
use crate::config::save;
use crate::constants::LANGUAGES_PATH;

#[derive(Debug)]
pub enum Error {
    Io(std::io::Error),
    Json(serde_json::Error),
}

impl From<std::io::Error> for Error {
    fn from(error: std::io::Error) -> Self {
        Self::Io(error)
    }
}

impl From<serde_json::Error> for Error {
    fn from(error: serde_json::Error) -> Self {
        Self::Json(error)
    }
}

// Struct for each language, containing the key (identifier for LanguageManager[self]), the code (own translation key for the name), and translations (key to translation mapping)
pub struct Language {
    key: String,
    code: String,
    translations: HashMap<String, String>,
}

impl Language {
    pub fn get_translation(&self, key: &str) -> Option<&String> {
        self.translations.get(key)
    }
}

// Struct for the language options, containing the text (a translation key for the desired text) and the code (the language code to select when this option is chosen)
pub struct LanguageOption {
    pub text: String,
    pub code: String,
}

pub struct LanguageManager {
    current: RefCell<String>,
    languages: IndexMap<String, Language>,
}

impl LanguageManager {
    pub fn new(current: String, languages: IndexMap<String, Language>) -> Self {
        Self {
            current: RefCell::new(current),
            languages,
        }
    }
    
    pub fn get_translation(&self, key: &str) -> String {
        let current = self.current.borrow();
        let current_language = self.languages.get(&*current).expect("Current language not found");

        match current_language.get_translation(key) {
            Some(translation) => translation.clone(),
            _ => {
                match current_language.get_translation("noTranslationText") {
                    Some(fallback) => format!("{fallback} {key}"),
                    _ => String::from("The language file is missing a 'noTranslationText' key."),
                }
            }
        }
    }

    pub fn set_language(&self, code: &str) {
        if self.languages.contains_key(code) {
            *self.current.borrow_mut() = code.to_string();

            let config = Config {
                language: code.to_string(),
            };

            match save(&config) {
                Ok(()) => {}
                Err(e) => eprintln!("Error saving config: {e:?}"),
            }
        } else {
            eprintln!("Language code '{code}' not found.");
        }
    }

    pub fn get_languages(&self) -> Vec<LanguageOption> {
        let mut languages = Vec::new();

        for language in self.languages.values() {
            languages.push(LanguageOption {
                text: language.key.clone(),
                code: language.code.clone(),
            });
        }

        languages
    }
}

#[derive(Debug, Deserialize, Serialize)]
struct LanguageManifest {
    name: String,
    key: String,
    code: String,
    file: String,
}

pub fn create_languages_manifest() -> Result<Vec<LanguageManifest>, Error> {
    let path = Path::new(LANGUAGES_PATH).parent().expect("Manifest path has no parent directory");
    let languages_dir_content = match read_dir(path) {
        Ok(content) => content,
        Err(e) => {
            eprintln!("Failed to read languages directory: {e}");
            return Err(Error::Io(e));
        }
    };

    let mut manifest: Vec<LanguageManifest> = Vec::new();

    for entry in languages_dir_content {
        let entry = entry?;
        let path = entry.path();

        let file_name = path.file_name().and_then(|name| name.to_str());
        let extension = path.extension().and_then(|name| name.to_str());
        let file_stem = path.file_stem().and_then(|name| name.to_str());

        if path.is_file() && extension == Some("json") {
            if let (Some(file_stem), Some(file_name)) = (file_stem, file_name) && file_stem != "manifest" {
                let mut chars = file_stem.chars();

                let name = match chars.next() {
                    Some(first) => first.to_uppercase().to_string() + chars.as_str(),
                    None => String::new(),
                };
                let code = file_stem.chars().take(2).collect::<String>();

                manifest.push(LanguageManifest { name, key: file_stem.to_string(), code, file: file_name.to_string() });
            }
        }
    }

    manifest.sort_by(|a, b| a.name.cmp(&b.name));

    let file = File::create(LANGUAGES_PATH)?;
    serde_json::to_writer_pretty(file, &manifest)?;

    Ok(manifest)
}

fn load_languages_manifest() -> Vec<LanguageManifest> {
    let file = match File::open(LANGUAGES_PATH) {
        Ok(file) => file,
        Err(e) => {
            eprintln!("Failed to open languages manifest file: {e}");
            return Vec::new();
        }
    };

    let manifest: Vec<LanguageManifest> = match serde_json::from_reader(file) {
        Ok(manifest) => manifest,
        Err(e) => {
            eprintln!("Failed to parse languages manifest file: {e}");
            return Vec::new();
        }
    };

    manifest
}

pub fn load_languages() -> IndexMap<String, Language> {
    let manifest = load_languages_manifest();
    let mut languages = IndexMap::new();

    let path = Path::new(LANGUAGES_PATH).parent().expect("Manifest path has no parent directory");

    for language in manifest {

        let file = match File::open(path.join(&language.file)) {
            Ok(file) => file,
            Err(e) => {
                eprintln!("Failed to open language file for '{}': {e}", language.name);
                continue;
            }
        };

        let translations: HashMap<String, String> = match serde_json::from_reader(file) {
            Ok(translations) => translations,
            Err(e) => {
                eprintln!("Failed to parse language file for '{}': {e}", language.name);
                continue;
            }
        };

        languages.insert(
            language.code.clone(),
            Language {
                key: language.key,
                code: language.code,
                translations,
            }
        );
    }

    languages
}