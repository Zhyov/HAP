use serde::Deserialize;
use serde_json;
use std::fs::File;
use indexmap::IndexMap;
use crate::paths::get_scripts_path;

#[derive(Deserialize)]
pub struct ScriptManifest {
    pub name: String,
    pub file: String,
}

#[derive(Clone, Debug, Deserialize)]
pub struct IPA {
    pub xsampa: String,
    pub info: Option<String>,
}

#[derive(Clone, Debug, Deserialize)]
pub struct Variant {
    #[serde(rename = "char")]
    pub character: String,
    pub change: String,
    pub ipa: Vec<IPA>,
}

#[derive(Clone, Debug, Deserialize)]
pub struct Character {
    #[serde(rename = "char")]
    pub character: String,
    pub native: Option<String>,
    pub upper: bool,
    pub ipa: Vec<IPA>,
    pub variations: Vec<Variant>,
}

#[derive(Debug)]
pub enum ScriptError {
    Io(std::io::Error),
    Json(serde_json::Error),
}

pub fn load_scripts_manifest() -> Result<Vec<ScriptManifest>, ScriptError> {
    let scripts_path = match get_scripts_path() {
        Ok(path) => path,
        Err(e) => {
            eprintln!("Failed to get scripts manifest path: {e}");
            return Err(ScriptError::Io(e))
        }
    };

    let file = match File::open(scripts_path) {
        Ok(file) => file,
        Err(e) => {
            eprintln!("Failed to open scripts manifest file: {e}");
            return Err(ScriptError::Io(e));
        }
    };

    let manifest: Vec<ScriptManifest> = match serde_json::from_reader(file) {
        Ok(manifest) => manifest,
        Err(e) => {
            eprintln!("Failed to parse scripts manifest file: {e}");
            return Err(ScriptError::Json(e));
        }
    };

    Ok(manifest)
}

pub fn load_scripts(filename: &str) -> Result<IndexMap<String, Character>, ScriptError> {
    let scripts_path = match get_scripts_path() {
        Ok(path) => path,
        Err(e) => {
            eprintln!("Failed to get scripts manifest path: {e}");
            return Err(ScriptError::Io(e))
        }
    };

    let path = scripts_path.parent().expect("Manifest path has no parent directory");

    let file = match File::open(path.join(filename)) {
        Ok(file) => file,
        Err(e) => {
            eprintln!("Failed to open script file for '{}': {e}", filename);
            return Err(ScriptError::Io(e));
        }
    };

    let characters = match serde_json::from_reader(file) {
        Ok(characters) => characters,
        Err(e) => {
            eprintln!("Failed to parse script file for '{}': {e}", filename);
            return Err(ScriptError::Json(e));
        }
    };

    Ok(characters)
}