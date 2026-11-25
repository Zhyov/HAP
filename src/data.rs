use std::fs::{File, write, read, create_dir_all, remove_dir_all, remove_file, rename};
use serde::{Deserialize, Serialize};
use crate::paths::{get_data_dir, get_temp_data_dir, get_backup_data_dir};
use crate::constants::{VERSION, REMOTE_DATA_BASE_URL};
use std::path::Path;
use sha2::{Digest, Sha256};

#[derive(Debug)]
pub enum Error {
    Io(std::io::Error),
    Json(serde_json::Error),
    Http(reqwest::Error),
    Semver(semver::Error),
    ChecksumMismatch(String),
    IncompatibleVersion(String),
}

impl Error {
    pub fn translation_key(&self) -> &str {
        match self {
            Error::Io(_) => "ioError",
            Error::Json(_) => "jsonError",
            Error::Http(_) => "httpError",
            Error::Semver(_) => "semverError",
            Error::ChecksumMismatch(_) => "checksumError",
            Error::IncompatibleVersion(_) => "incompatibleVersion",
        }
    }
}

impl From<std::io::Error> for Error {
    fn from(error: std::io::Error) -> Self {
        Error::Io(error)
    }
}

#[derive(Deserialize, Serialize)]
pub struct DataFile {
    name: String,
    sha256: String,
}

#[derive(Deserialize, Serialize)]
pub struct DataFiles {
    manifest: DataFile,
    files: Vec<DataFile>,
}

#[derive(Deserialize, Serialize)]
pub struct DataManifest {
    version: String,
    min_hap_version: String,
    latest_hap_version: String,
    scripts: DataFiles,
    translations: DataFiles,
}

pub fn load_data_manifest() -> Result<DataManifest, Error> {
    let data_path = match get_data_dir() {
        Ok(path) => path.join("manifest.json"),
        Err(e) => {
            eprintln!("Failed to get data manifest path: {e}");
            return Err(Error::Io(e));
        }
    };

    let file = match File::open(data_path) {
        Ok(file) => file,
        Err(e) => {
            eprintln!("Failed to open data manifest file: {e}");
            return Err(Error::Io(e));
        }
    };

    let manifest: DataManifest = match serde_json::from_reader(file) {
        Ok(manifest) => manifest,
        Err(e) => {
            eprintln!("Failed to parse data manifest file: {e}");
            return Err(Error::Json(e));
        }
    };

    Ok(manifest)
}

pub fn load_online_data_manifest() -> Result<DataManifest, Error> {
    let response = reqwest::blocking::get(format!("{REMOTE_DATA_BASE_URL}manifest.json"))
        .map_err(Error::Http)?.error_for_status().map_err(Error::Http)?;
    let online_file = response.text().map_err(Error::Http)?;

    let manifest = match serde_json::from_str::<DataManifest>(&online_file) {
        Ok(manifest) => manifest,
        Err(e) => {
            eprintln!("Failed to parse data manifest file: {e}");
            return Err(Error::Json(e));
        }
    };

    Ok(manifest)
}

pub fn get_data_version() -> Result<String, Error> {
    let data = load_data_manifest()?;

    Ok(data.version)
}

pub fn is_update_available(manifest: &DataManifest) -> Result<bool, Error> {
    let online_version = semver::Version::parse(&manifest.version).map_err(Error::Semver)?;

    let local_manifest = get_data_dir()?.join("manifest.json");
    if !local_manifest.exists() {
        return Ok(true);
    }

    let local_version = semver::Version::parse(&get_data_version()?).map_err(Error::Semver)?;

    Ok(online_version > local_version)
}

pub fn is_compatible(manifest: &DataManifest) -> Result<bool, Error> {
    let local_hap_version = semver::Version::parse(VERSION).map_err(Error::Semver)?;
    let min_hap_version = semver::Version::parse(&manifest.min_hap_version).map_err(Error::Semver)?;

    Ok(local_hap_version >= min_hap_version)
}

pub fn download_file(url: &str, destination: &Path) -> Result<(), Error> {
    let response = reqwest::blocking::get(url).map_err(Error::Http)?.error_for_status().map_err(Error::Http)?;
    let contents = response.bytes().map_err(Error::Http)?;

    write(destination, contents).map_err(Error::Io)?;
    Ok(())
}

pub fn download_and_verify(url: &str, destination: &Path, expected_checksum: &str, filename: &str) -> Result<(), Error> {
    download_file(url, destination)?;

    let contents = read(destination).map_err(Error::Io)?;
    let checksum = calculate_checksum(&contents);

    if checksum != expected_checksum {
        return Err(Error::ChecksumMismatch(filename.to_string()));
    }

    Ok(())
}

pub fn download_script_files(manifest: &DataManifest) -> Result<(), Error> {
    let scripts_path = match get_temp_data_dir() {
        Ok(path) => path.join("scripts"),
        Err(e) => {
            eprintln!("Failed to get data manifest path for scripts: {e}");
            return Err(Error::Io(e));
        }
    };

    create_dir_all(&scripts_path).map_err(Error::Io)?;

    let manifest_online_path = format!("{REMOTE_DATA_BASE_URL}scripts/manifest.json");
    let manifest_path = scripts_path.join("manifest.json");

    download_and_verify(&manifest_online_path, &manifest_path, &manifest.scripts.manifest.sha256, &manifest.scripts.manifest.name)?;

    for file in &manifest.scripts.files {
        let name = &file.name;
        let file_online_path = format!("{REMOTE_DATA_BASE_URL}scripts/{name}");
        let file_path = scripts_path.join(name);

        download_and_verify(&file_online_path, &file_path, &file.sha256, name)?;
    }

    Ok(())
}

pub fn download_translation_files(manifest: &DataManifest) -> Result<(), Error> {
    let translations_path = match get_temp_data_dir() {
        Ok(path) => path.join("translations"),
        Err(e) => {
            eprintln!("Failed to get data manifest path for translations: {e}");
            return Err(Error::Io(e));
        }
    };

    create_dir_all(&translations_path).map_err(Error::Io)?;

    let manifest_online_path = format!("{REMOTE_DATA_BASE_URL}translations/manifest.json");
    let manifest_path = translations_path.join("manifest.json");

    download_and_verify(&manifest_online_path, &manifest_path, &manifest.translations.manifest.sha256, &manifest.translations.manifest.name)?;

    for file in &manifest.translations.files {
        let name = &file.name;
        let file_online_path = format!("{REMOTE_DATA_BASE_URL}translations/{name}");
        let file_path = translations_path.join(name);

        download_and_verify(&file_online_path, &file_path, &file.sha256, name)?;
    }

    Ok(())
}

pub fn download_data_files(manifest: &DataManifest) -> Result<(), Error> {
    let temp_dir = get_temp_data_dir()?;

    let scripts = temp_dir.join("scripts");
    let translations = temp_dir.join("translations");

    if scripts.exists() {
        remove_dir_all(&scripts)?;
    }

    if translations.exists() {
        remove_dir_all(&translations)?;
    }

    download_script_files(manifest)?;
    download_translation_files(manifest)?;

    Ok(())
}

pub fn update_data() -> Result<bool, Error> {
    let manifest = load_online_data_manifest()?;
    update_data_with_manifest(&manifest)
}

pub fn update_data_with_manifest(manifest: &DataManifest) -> Result<bool, Error> {
    if !is_compatible(manifest)? {
        return Err(Error::IncompatibleVersion(manifest.min_hap_version.clone()));
    }

    let update = is_update_available(manifest)?;

    if update {
        if let Err(e) = download_data_files(manifest) {
            cleanup_downloads()?;
            return Err(e);
        }

        if let Err(e) = backup_data() {
            cleanup_downloads()?;
            return Err(e);
        }

        match apply_data_update() {
            Ok(()) => {},
            Err(e) => {
                restore_data()?;
                cleanup_temp_data()?;
                return Err(e);
            }
        }

        match save_data_manifest(manifest) {
            Ok(()) => {},
            Err(e) => {
                restore_data()?;
                cleanup_temp_data()?;
                return Err(e);
            }
        }

        cleanup_temp_data()?;
        Ok(true)
    } else {
        Ok(false)
    }
}

pub fn calculate_checksum(contents: &[u8]) -> String {
    let mut hasher = Sha256::new();
    hasher.update(contents);
    let hash = hasher.finalize();

    format!("{:x}", hash)
}

pub fn apply_scripts_update() -> Result<(), Error> {
    let temp_scripts = get_temp_data_dir()?.join("scripts");
    let scripts = get_data_dir()?.join("scripts");

    rename(&temp_scripts, &scripts)?;

    Ok(())
}

pub fn apply_translations_update() -> Result<(), Error> {
    let temp_translations = get_temp_data_dir()?.join("translations");
    let translations = get_data_dir()?.join("translations");

    rename(&temp_translations, &translations)?;

    Ok(())
}

pub fn apply_data_update() -> Result<(), Error> {
    apply_scripts_update()?;
    apply_translations_update()?;

    Ok(())
}

 pub fn save_data_manifest(manifest: &DataManifest) -> Result<(), Error> {
    let data_dir = get_data_dir()?;
    let manifest_path = data_dir.join("manifest.json");
    let temp_manifest_path = data_dir.join("manifest.json.tmp");

    let file = File::create(&temp_manifest_path)?;

    match serde_json::to_writer_pretty(file, manifest) {
        Ok(()) => {},
        Err(e) => {
            remove_file(&temp_manifest_path)?;
            return Err(Error::Json(e));
        }
    }

    rename(&temp_manifest_path, &manifest_path)?;

    Ok(())
}

pub fn backup_scripts() -> Result<(), Error> {
    let scripts = get_data_dir()?.join("scripts");
    let backup_scripts = get_backup_data_dir()?.join("scripts");

    if scripts.exists() {
        rename(&scripts, &backup_scripts)?;
    }

    Ok(())
}

pub fn backup_translations() -> Result<(), Error> {
    let translations = get_data_dir()?.join("translations");
    let backup_translations = get_backup_data_dir()?.join("translations");

    if translations.exists() {
        rename(&translations, &backup_translations)?;
    }

    Ok(())
}

pub fn backup_manifest() -> Result<(), Error> {
    let manifest = get_data_dir()?.join("manifest.json");
    let backup_manifest = get_backup_data_dir()?.join("manifest.json");

    if manifest.exists() {
        rename(&manifest, &backup_manifest)?;
    }

    Ok(())
}

pub fn backup_data() -> Result<(), Error> {
    let backup_dir = get_backup_data_dir()?;

    if backup_dir.read_dir()?.next().is_some() {
        return Err(Error::Io(std::io::Error::other("Backup directory is not empty")));
    }

    match backup_scripts() {
        Ok(()) => {},
        Err(e) => return Err(e)
    };

    match backup_translations() {
        Ok(()) => {},
        Err(e) => {
            let scripts = get_data_dir()?.join("scripts");
            let backup_scripts = get_backup_data_dir()?.join("scripts");

            if backup_scripts.exists() {
                rename(&backup_scripts, &scripts)?;
            }

            return Err(e);
        }
    };

    match backup_manifest() {
        Ok(()) => {},
        Err(e) => {
            let scripts = get_data_dir()?.join("scripts");
            let backup_scripts = get_backup_data_dir()?.join("scripts");

            if scripts.exists() {
                remove_dir_all(&scripts)?;
            }

            if backup_scripts.exists() {
                rename(&backup_scripts, &scripts)?;
            }

            let translations = get_data_dir()?.join("translations");
            let backup_translations = get_backup_data_dir()?.join("translations");

            if translations.exists() {
                remove_dir_all(&translations)?;
            }

            if backup_translations.exists() {
                rename(&backup_translations, &translations)?;
            }

            return Err(e);
        }
    }

    Ok(())
}

pub fn restore_data() -> Result<(), Error> {
    let scripts = get_data_dir()?.join("scripts");
    let backup_scripts = get_backup_data_dir()?.join("scripts");

    if scripts.exists() {
        remove_dir_all(&scripts)?;
    }

    if backup_scripts.exists() {
        rename(&backup_scripts, &scripts)?;
    }

    let translations = get_data_dir()?.join("translations");
    let backup_translations = get_backup_data_dir()?.join("translations");

    if translations.exists() {
        remove_dir_all(&translations)?;
    }

    if backup_translations.exists() {
        rename(&backup_translations, &translations)?;
    }

    let manifest = get_data_dir()?.join("manifest.json");
    let backup_manifest = get_backup_data_dir()?.join("manifest.json");

    if manifest.exists() {
        remove_file(&manifest)?;
    }

    if backup_manifest.exists() {
        rename(&backup_manifest, &manifest)?;
    }

    Ok(())
}

pub fn cleanup_temp_data() -> Result<(), Error> {
    let temp_dir = get_data_dir()?.join(".temp");

    if temp_dir.exists() {
        remove_dir_all(&temp_dir)?;
    }

    Ok(())
}

pub fn cleanup_downloads() -> Result<(), Error> {
    let temp_dir = get_data_dir()?.join(".temp");

    let scripts = temp_dir.join("scripts");
    let translations = temp_dir.join("translations");

    if scripts.exists() {
        remove_dir_all(&scripts)?;
    }

    if translations.exists() {
        remove_dir_all(&translations)?;
    }

    Ok(())
}

pub fn is_hap_update_available(manifest: &DataManifest) -> Result<bool, Error> {
    let current_version = semver::Version::parse(VERSION).map_err(Error::Semver)?;
    let latest_version = semver::Version::parse(&manifest.latest_hap_version).map_err(Error::Semver)?;

    Ok(latest_version > current_version)
}