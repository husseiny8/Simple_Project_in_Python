# File Organizer

A simple Python utility that automatically organizes files into categorized folders based on their file extensions. The script scans a specified directory and copies files into separate folders such as Images, Documents, Videos, Audio, and Archives.

## Features

* Recursively scans all files in a target directory.
* Automatically categorizes files by extension.
* Creates category folders if they do not exist.
* Preserves original files by copying instead of moving.
* Easy to customize with additional file types and categories.

## Supported Categories

| Category  | Extensions                                        |
| --------- | ------------------------------------------------- |
| Images    | .jpg, .jpeg, .png, .gif, .bmp, .tiff, .svg, .webp |
| Documents | .pdf, .doc, .docx, .txt, .xls, .xlsx, .ppt, .pptx |
| Videos    | .mp4, .mkv, .avi, .mov, .wmv                      |
| Audio     | .mp3, .wav, .aac, .flac, .ogg                     |
| Archives  | .zip, .rar, .tar, .gz, .7z                        |

## Requirements

* Python 3.7+

No external libraries are required. The project uses only Python's standard library:

* shutil
* pathlib

## Installation

Clone the repository:

```bash
git clone https://github.com/your-username/File-Organizer.git
cd File-Organizer

```
```bash
python file_organizer.py
```

## Configuration

Modify the directory path inside the script:

```python
base_dir = Path(r"C:\Users\hussein\Downloads")
```

This directory will be scanned for files.

The organized files will be copied to:

```python
target_dir = base_dir / "sorted"
```

## Usage

Run the script:



The script will:

1. Create category folders inside the `sorted` directory.
2. Search all files recursively.
3. Copy matching files into their corresponding category folders.

## Example

Before:

```text
Downloads/
├── photo.jpg
├── report.pdf
├── music.mp3
└── movie.mp4
```

After:

```text
Downloads/
├── sorted/
│   ├── images/
│   │   └── photo.jpg
│   ├── documents/
│   │   └── report.pdf
│   ├── audio/
│   │   └── music.mp3
│   └── videos/
│       └── movie.mp4
```

## License

This project is open source and available under the MIT License.
