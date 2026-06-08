import shutil
from pathlib import Path

#Here You can change the path
base_dir = Path(r"C:\Users\hussein\Downloads")
target_dir = base_dir / "sorted"

FILE_CATEGORIES = {

    "images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".svg", ".webp"],

    "documents": [".pdf", ".doc", ".docx", ".txt", ".xls", ".xlsx", ".ppt", ".pptx"],

    "videos": [".mp4", ".mkv", ".avi", ".mov", ".wmv"],

    "audio": [".mp3", ".wav", ".aac", ".flac", ".ogg"],

    "archives": [".zip", ".rar", ".tar", ".gz", ".7z"]

}

def create_categories_directories():
    for category,_ in FILE_CATEGORIES.items():
        (target_dir / category).mkdir(parents=True, exist_ok=True)

def search_and_categorize_files():
    for file in base_dir.rglob("*"):
        for category,extensions in FILE_CATEGORIES.items():
            if file.suffix in extensions:
                try:
                    shutil.copy(file,target_dir / category)
                except shutil.SameFileError:
                    print(f"File {file.name} already exists in {target_dir}")

create_categories_directories()
search_and_categorize_files()