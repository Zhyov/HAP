use std::fs::File;
use std::fs::create_dir_all;
use std::path::Path;
use serde::{Deserialize, Serialize};
use serde_json;
use crate::constants::CONFIG_PATH;

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
    let file = match File::open(CONFIG_PATH) {
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
    let path = Path::new(CONFIG_PATH);

    if let Some(directory) = path.parent() {
        match create_dir_all(directory) {
            Ok(()) => {},
            Err(e) => return Err(Error::Io(e)),
        }
    }

    let file = match File::create(CONFIG_PATH) {
        Ok(file) => file,
        Err(e) => return Err(Error::Io(e)),
    };

    if let Err(e) = serde_json::to_writer_pretty(file, config) {
        return Err(Error::Json(e));
    }

    Ok(())

}

// if let Err(e) = save(&config) {
//    eprintln!("Failed to save config file: {e}");
// }