from pathlib import Path

DOWNLOADS_FOLDER = Path.home() / "Downloads"

# Set to True to test the script without moving files
DRY_RUN = False

# destination folders
DESTINATIONS = {
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".epub", ".csv"],
    "Pictures": [".png", ".jpg", ".jpeg", ".gif", ".bmp", ".svg"],
    "Music": [".mp3", ".wav", ".aac", ".flac", ".m4a", ".aup3"],
    "Zip": [".zip", ".rar", ".tar", ".gz"],
    "Executables": [".exe", ".msi"]
}

# Convert folder names to full paths
BASE_PATH = Path("C:/")


def ensure_directories():
    """Create destination directories if they don't exist."""
    for folder in DESTINATIONS.keys():
        folder_path = BASE_PATH / folder
        folder_path.mkdir(parents=True, exist_ok=True)


def move_files():
    """Move files to appropriate folders based on their extensions."""
    for file_path in DOWNLOADS_FOLDER.iterdir():
        if file_path.is_file():
            file_ext = file_path.suffix.lower()

            for folder, extensions in DESTINATIONS.items():
                if file_ext in extensions:  # Ensure extensions is a list
                    destination = (BASE_PATH / folder) / file_path.name  # Corrected path usage
                    if DRY_RUN:
                        print(f"[DRY RUN] Would move {file_path.name} to {destination}")
                    else:
                        file_path.replace(destination)
                        print(f"Moved {file_path.name} to {destination}")
                    break


def main():
    ensure_directories()
    move_files()
    print("Downloads folder organized successfully!" if not DRY_RUN else "Dry-run completed. No files were moved.")


if __name__ == "__main__":
    main()
