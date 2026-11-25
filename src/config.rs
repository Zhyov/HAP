use std::fs::File;
use std::fs::create_dir_all;
use serde::{Deserialize, Serialize};
use serde_json;
use crate::paths::get_config_path;

#[derive(Debug)]
pub enum Error {
    Io(std::io::Error),
    Json(serde_json::Error),
}

#[derive(Deserialize, Serialize)]
#[serde(default)]
pub struct Config {
    pub language: String,
}

impl Default for Config {
    fn default() -> Self {
        Self {
            language: String::from("en"),
        }
    }
}

pub fn load() -> Config {
    let config_path = match get_config_path() {
        Ok(path) => path,
        Err(e) => {
            eprintln!("Failed to get config path: {e}");
            return Config::default();
        }
    };

    let file = match File::open(config_path) {
        Ok(file) => file,
        Err(e) => {
            eprintln!("Failed to open config file: {e}");
            return Config::default();
        }
    };

    let config: Config = match serde_json::from_reader(file) {
        Ok(config) => config,
        Err(e) => {
            eprintln!("Failed to parse config file: {e}");
            return Config::default();
        }
    };

    config
}

pub fn save(config: &Config) -> Result<(), Error> {
    let config_path = match get_config_path() {
        Ok(path) => path,
        Err(e) => {
            eprintln!("Failed to get config path: {e}");
            return Err(Error::Io(e));
        }
    };

    if let Some(directory) = config_path.parent() {
        match create_dir_all(directory) {
            Ok(()) => {},
            Err(e) => return Err(Error::Io(e)),
        }
    }

    let file = match File::create(config_path) {
        Ok(file) => file,
        Err(e) => return Err(Error::Io(e)),
    };

    if let Err(e) = serde_json::to_writer_pretty(file, config) {
        return Err(Error::Json(e));
    }

    Ok(())

}