from pathlib import Path 
import shutil

SOURCE_FOLDER = Path("textfile")

FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".webp", ".svg"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".rtf"],
    "Spreadsheets": [".xls", ".xlsx", ".csv"],
    "Presentations": [".ppt", ".pptx"],
    "Videos": [".mp4", ".mkv", ".mov", ".avi"],
    "Audio": [".mp3", ".wav", ".m4a"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Code": [".py", ".js", ".html", ".css", ".java"]
}

def organize_files():
    if not SOURCE_FOLDER.is_dir():
        print("Source folder does not exist.")
        return

    moved = 0
    skipped = 0

    for file in SOURCE_FOLDER.iterdir():
        if not file.is_file() or file.name == Path(__file__).name:
            continue

        category = "Others"

        for folder, extensions in FILE_TYPES.items():
            if file.suffix.lower() in extensions:
                category = folder
                break

        destination_folder = SOURCE_FOLDER / category
        destination_folder.mkdir(exist_ok=True)

        destination = destination_folder / file.name

        if destination.exists():
            print(f"Skipped duplicate name: {file.name}")
            skipped += 1
            continue

        shutil.move(str(file), str(destination))

        print(f"Moved: {file.name} -> {category}/")
        moved += 1

    print("\nOrganization complete!")
    print(f"Files moved: {moved}")
    print(f"Files skipped: {skipped}")

if __name__ == "__main__":
    organize_files()