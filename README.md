# Smart File Organizer v1

A Python-based file organization tool that scans a selected folder, identifies files by their extensions, creates category folders, and moves supported files into the appropriate folders.

## Features

* Scan a selected source folder
* Recursively scan files inside subfolders
* Identify files by extension
* Automatically create category folders
* Move supported files into their categories
* Ignore folders during file processing
* Skip the destination folder during recursive scanning
* Handle common file-operation errors
* Track moved, skipped, failed, and unknown files

## Supported File Types

| File Type               | Destination |
| ----------------------- | ----------- |
| `.pdf`                  | `PDF`       |
| `.txt`, `.doc`          | `Documents` |
| `.xls`, `.xlsx`         | `Excel`     |
| `.png`, `.jpg`, `.jpeg` | `Images`    |
| `.mp4`, `.webm`         | `Videos`    |
| `.py`                   | `Python`    |

Unsupported file types are left untouched and counted as unknown files.

## Technologies

* Python
* `os`
* `shutil`

## How It Works

```text
Select Source Folder
        ↓
Scan Folder Recursively
        ↓
Identify File Extension
        ↓
Determine Category
        ↓
Create Category Folder
        ↓
Move File
        ↓
Show Final Report
```

## Example

Before:

```text
Downloads/
├── report.pdf
├── photo.jpg
├── notes.txt
└── script.py
```

After:

```text
Downloads/
├── PDF/
│   └── report.pdf
├── Images/
│   └── photo.jpg
├── Documents/
│   └── notes.txt
└── Python/
    └── script.py
```

## Error Handling

The program handles common file-system errors such as:

* File already exists
* File not found
* Permission errors
* Other operating-system file errors

## Version

**v1.0**

This version represents the first working prototype of the Smart File Organizer project.

## Future Development

Future versions will improve the organizer with more flexible file-category rules, cleaner project structure, and additional automation features.
