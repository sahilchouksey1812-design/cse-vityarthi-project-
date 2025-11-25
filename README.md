# Basic File Management System

## Overview
A simple, interactive command-line file manager implemented in Python. The tool provides common file and directory operations via a menu-driven interface so users can list directories, create/read/write files, move/copy/delete resources, and search using glob patterns.

> Note: The main script file is expected to be named `basic_file_manager.py`.

## Features
- List directory contents (files and directories)
- Display file/directory info (size, timestamps, type)
- Create files (with parent directories)
- Read files
- Write (overwrite) and append to files
- Delete files and directories (recursive for directories)
- Rename files and directories
- Copy and move files/directories
- Create directories
- Search files using glob patterns
- Simple interactive, menu-driven CLI

## Technologies / Tools Used
- Python 3.8+ (standard library)
  - pathlib, os, shutil, glob, datetime
- Works cross-platform (Windows, macOS, Linux) using native commands for clearing the screen

## Installation & Run
1. Install Python 3.8 or newer (https://www.python.org/downloads/).
2. Open a terminal (Command Prompt / PowerShell on Windows).
3. Navigate to the project folder:
   - cd "c:\Users\Santhosh\OneDrive\Desktop\New folder (2)"
4. Run the script:
   - python basic_file_manager.py
5. Follow the on-screen menu to perform file operations.

Optional (recommended):
- Create a virtual environment:
  - python -m venv .venv
  - .venv\Scripts\activate  (Windows)
  - pip install -r requirements.txt  (no external deps required for this project)

## Testing / Usage Instructions
- The application is interactive; test by choosing menu options:
  - 1: List a directory (leave empty for current)
  - 3: Create a file (will create parent directories)
  - 4: Read a file
  - 5/6: Write or append (finish multi-line input with a single line `<END>`)
  - 7: Delete (type `yes` to confirm)
  - 9/10: Copy or move files/directories
  - 12: Search using glob patterns (e.g., `**/*.py`)
- Manual test checklist:
  - Create a nested directory and file, write text, read it back
  - Copy a file to a directory and verify content
  - Rename and then delete a directory
  - Search with wildcard and recursive patterns
- Automated tests: none included. To add tests, use `pytest` and create temporary filesystem fixtures (tmp_path) to assert behavior of individual functions.

## Known Issues / Notes
- Ensure the main script uses the correct Python entry check:
  - It should be `if __name__ == '__main__':` (fix if different).
- Use caution with the delete option (recursive removal).
- Glob pattern input expects standard Python glob syntax.

## Screenshots
(Optionally add screenshots of the CLI here — e.g., save images in `/docs` and reference them.)

## License
Include a license file if you plan to share the project publicly (e.g., MIT).