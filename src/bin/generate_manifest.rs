use sha2::{Digest, Sha256};
use std::fs::{self, File};
use std::path::Path;
use serde::{Deserialize, Serialize};

#[derive(Deserialize, Serialize)]
struct DataFile {
    name: String,
    sha256: String,
}

#[derive(Deserialize, Serialize)]
struct DataFiles {
    manifest: DataFile,
    files: Vec<DataFile>,
}

#[derive(Deserialize, Serialize)]
struct DataManifest {
    version: String,
    min_hap_version: String,
    latest_hap_version: String,
    scripts: DataFiles,
    translations: DataFiles,
}

#[derive(Serialize)]
struct ScriptManifest {
    name: String,
    file: String,
}

#[derive(Serialize)]
struct LanguageManifest {
    name: String,
    key: String,
    code: String,
    file: String,
}

#[derive(Deserialize)]
struct ManifestConfig {
    version: String,
    min_hap_version: String,
    latest_hap_version: String,
}

fn main() -> Result<(), Box<dyn std::error::Error>> {
    let config_path = std::path::Path::new(env!("CARGO_MANIFEST_DIR")).join("tools/manifest_config.json");
    let config_file = std::fs::File::open(config_path)?;
    let config: ManifestConfig = serde_json::from_reader(config_file)?;

    generate_scripts_manifest(Path::new("data/scripts"))?;
    generate_translations_manifest(Path::new("data/translations"))?;

    let scripts = DataFiles {
        manifest: DataFile {
            name: "scripts/manifest.json".to_string(),
            sha256: calculate_file_checksum(Path::new("data/scripts/manifest.json"))?,
        },
        files: scan_directory(Path::new("data/scripts"), false)?,
    };

    let translations = DataFiles {
        manifest: DataFile {
            name: "translations/manifest.json".to_string(),
            sha256: calculate_file_checksum(Path::new("data/translations/manifest.json"))?,
        },
        files: scan_directory(Path::new("data/translations"), false)?,
    };

    let manifest = DataManifest {
        version: config.version,
        min_hap_version: config.min_hap_version,
        latest_hap_version: config.latest_hap_version,
        scripts,
        translations,
    };

    let file = File::create("data/manifest.json")?;
    serde_json::to_writer_pretty(file, &manifest)?;

    Ok(())
}

fn calculate_checksum(contents: &[u8]) -> String {
    let mut hasher   = Sha256::new();
    hasher.update(contents);
    let hash = hasher.finalize();

    format!("{:x}", hash)
}

fn calculate_file_checksum(path: &Path) -> Result<String, std::io::Error> {
    let contents = fs::read(path)?;
    Ok(calculate_checksum(&contents))
}

fn scan_directory(path: &Path, include_manifest: bool) -> Result<Vec<DataFile>, std::io::Error> {
    let mut files = Vec::new();

    for entry in fs::read_dir(path)? {
        let entry = entry?;
        let file_path = entry.path();

        if file_path.is_file() && (include_manifest || entry.file_name() != "manifest.json") {
            let checksum = calculate_file_checksum(&file_path)?;
            let name = entry.file_name().into_string().map_err(|_| std::io::Error::other("Invalid filename"))?;

            files.push(DataFile {
                name,
                sha256: checksum,
            });
        }
    }

    Ok(files)
}

fn generate_scripts_manifest(path: &Path) -> Result<(), Box<dyn std::error::Error>> {
    let mut manifest = Vec::new();

    for entry in fs::read_dir(path)? {
        let entry = entry?;
        let file_path = entry.path();

        if file_path.is_file() && file_path.extension().is_some_and(|ext| ext == "json") {
            let file = entry.file_name().into_string()
                .map_err(|_| std::io::Error::other("Invalid filename"))?;

            if file == "manifest.json" {
                continue;
            }

            let name = file.strip_suffix(".json").unwrap().to_string();

            manifest.push(ScriptManifest {
                name,
                file,
            });
        }
    }

    manifest.sort_by(|a, b| a.name.cmp(&b.name));

    let file = File::create(path.join("manifest.json"))?;
    serde_json::to_writer_pretty(file, &manifest)?;

    Ok(())
}

fn generate_translations_manifest(path: &Path) -> Result<(), Box<dyn std::error::Error>> {
    let mut manifest = Vec::new();

    for entry in fs::read_dir(path)? {
        let entry = entry?;
        let file_path = entry.path();

        if file_path.is_file() && file_path.extension().is_some_and(|ext| ext == "json") {
            let file = entry.file_name().into_string().map_err(|_| std::io::Error::other("Invalid filename"))?;

            if file == "manifest.json" {
                continue;
            }

            let key = file.strip_suffix(".json").unwrap().to_string();
            let mut chars = key.chars();

            let name = match chars.next() {
                Some(first) => first.to_uppercase().to_string() + chars.as_str(),
                None => String::new(),
            };

            let code = key.chars().take(2).collect::<String>();

            manifest.push(LanguageManifest {
                name,
                key,
                code,
                file,
            });
        }
    }

    manifest.sort_by(|a, b| a.name.cmp(&b.name));

    let file = File::create(path.join("manifest.json"))?;
    serde_json::to_writer_pretty(file, &manifest)?;

    Ok(())
}