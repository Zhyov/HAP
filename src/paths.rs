use std::path::PathBuf;
use std::env::current_exe;
use std::fs::{create_dir, create_dir_all};

pub fn get_data_dir() -> Result<PathBuf, std::io::Error> {
    let binary_path = current_exe()?;
    let binary_dir = binary_path.parent().expect("Binary path has no parent directory");
    let data_dir = binary_dir.join("data");

    if !data_dir.exists() {
        create_dir(&data_dir)?;
    }

    Ok(data_dir)
}

pub fn get_languages_path() -> Result<PathBuf, std::io::Error> {
    Ok(get_data_dir()?.join("translations").join("manifest.json"))
}

pub fn get_scripts_path() -> Result<PathBuf, std::io::Error> {
    Ok(get_data_dir()?.join("scripts").join("manifest.json"))
}

pub fn get_config_path() -> Result<PathBuf, std::io::Error> {
    Ok(get_data_dir()?.join("config.json"))
}

pub fn get_temp_data_dir() -> Result<PathBuf, std::io::Error> {
    let temp_dir = get_data_dir()?.join(".temp");
    create_dir_all(&temp_dir)?;

    Ok(temp_dir)
}

pub fn get_backup_data_dir() -> Result<PathBuf, std::io::Error> {
    let backup_dir = get_temp_data_dir()?.join("backup");
    create_dir_all(&backup_dir)?;

    Ok(backup_dir)
}