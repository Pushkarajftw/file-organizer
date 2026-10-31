# Automatic File Organizer

A simple Python automation script that sorts files into folders (Images, Documents, Videos, etc.) based on their file extension.

Instead of manually moving hundreds of mixed files out of a cluttered folder, run the script once and everything lands in the right place.

## Features

- Sorts files into categories by extension: Images, Documents, Spreadsheets, Presentations, Videos, Audio, Archives and Code
- Creates category folders automatically
- Puts unrecognized file types into an `Others` folder
- **Duplicate protection**: never overwrites a file that already exists in the destination
- Prints a summary of files moved and skipped

## Tech Used

- Python 3
- `pathlib` and `shutil` (both included with Python, so there is nothing to install)

## Project Structure

```
file-organizer/
├── file_organizer.py   # the main script
├── TestFiles/          # sample files to try the script on
├── .gitignore
└── README.md
```

## How to Run

1. Make sure Python 3 is installed:
   ```
   python --version
   ```
2. Clone this repository:
   ```
   git clone https://github.com/Pushkarajftw/file-organizer.git
   cd file-organizer
   ```
3. Run the script:
   ```
   python file_organizer.py
   ```

> **Warning:** the script **moves** files instead of copying them. Always test on copies or dummy files first, never on important originals.

## Configuration

The folder to organize is set at the top of `file_organizer.py`:

```python
SOURCE_FOLDER = Path("TestFiles")
```

To add or change categories, edit the `FILE_TYPES` dictionary. For example, to support a new image format, add its extension to the `Images` list.

## Example

**Before**

```
TestFiles/
├── resume.pdf
├── photo.jpg
├── sales.xlsx
└── movie.mp4
```

**Output**

```
Moved: resume.pdf -> Documents/
Moved: photo.jpg -> Images/
Moved: sales.xlsx -> Spreadsheets/
Moved: movie.mp4 -> Videos/

Organization complete!
Files moved: 4
Files skipped: 0
```

**After**

```
TestFiles/
├── Documents/
│   └── resume.pdf
├── Images/
│   └── photo.jpg
├── Spreadsheets/
│   └── sales.xlsx
└── Videos/
    └── movie.mp4
```

## How It Works

1. Scans the files directly inside the source folder
2. Checks each file's extension against the `FILE_TYPES` map
3. Creates the matching category folder if needed
4. Moves the file, unless one with the same name already exists there

Only files directly inside the source folder are processed. Subfolders are ignored.

## Author

**Pushkaraj Raut**
GitHub: [@Pushkarajftw](https://github.com/Pushkarajftw)
