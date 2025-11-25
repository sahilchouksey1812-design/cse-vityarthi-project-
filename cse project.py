import os
import shutil
import glob
from pathlib import Path
from datetime import datetime

BASE = Path.cwd()


def clear_screen():
    # cross-platform clear
    os.system('cls' if os.name == 'nt' else 'clear')


def prompt_path(prompt_text="Enter path (relative or absolute): ") -> Path:
    p = input(prompt_text).strip()
    if not p:
        return Path(BASE)
    return (Path(p).expanduser()).resolve()


def list_dir():
    p = prompt_path("List directory (leave empty for current dir): ")
    if not p.exists():
        print("Path does not exist.")
        return
    if p.is_file():
        print(f"{p} is a file. Showing file info:")
        show_info(p)
        return
    print(f"Contents of: {p}\n")
    for item in sorted(p.iterdir()):
        t = '<DIR>' if item.is_dir() else 'FILE '
        size = f"{item.stat().st_size} bytes" if item.is_file() else ''
        print(f"{t:5}  {item.name:40}  {size}")


def show_info(p: Path = None):
    if p is None:
        p = prompt_path("Enter file path to show info: ")
    if not p.exists():
        print("Path does not exist.")
        return
    st = p.stat()
    print(f"Path: {p}")
    print(f"Type: {'Directory' if p.is_dir() else 'File'}")
    print(f"Size: {st.st_size} bytes")
    print(f"Created: {datetime.fromtimestamp(st.st_ctime)}")
    print(f"Modified: {datetime.fromtimestamp(st.st_mtime)}")
    print(f"Accessed: {datetime.fromtimestamp(st.st_atime)}")


def create_file():
    p = prompt_path("Create file path (will create parents if needed): ")
    if p.exists() and p.is_dir():
        print("A directory exists at that path. Choose a file path.")
        return
    p.parent.mkdir(parents=True, exist_ok=True)
    if p.exists():
        print("File already exists. Use write/append to update it.")
        return
    p.write_text('')
    print(f"Created file: {p}")


def read_file():
    p = prompt_path("Enter file path to read: ")
    if not p.exists() or not p.is_file():
        print("File does not exist.")
        return
    print('\n--- File content start ---')
    print(p.read_text())
    print('--- File content end ---\n')


def write_file():
    p = prompt_path("Enter file path to write to (will overwrite): ")
    p.parent.mkdir(parents=True, exist_ok=True)
    print("Enter text. Finish with a single line containing only <END>.")
    lines = []
    while True:
        line = input()
        if line.strip() == '<END>':
            break
        lines.append(line)
    p.write_text('\n'.join(lines))
    print(f"Wrote {len(lines)} lines to {p}")


def append_file():
    p = prompt_path("Enter file path to append to: ")
    p.parent.mkdir(parents=True, exist_ok=True)
    print("Enter text. Finish with a single line containing only <END>.")
    lines = []
    while True:
        line = input()
        if line.strip() == '<END>':
            break
        lines.append(line)
    with p.open('a', encoding='utf-8') as f:
        f.write('\n'.join(lines) + '\n')
    print(f"Appended {len(lines)} lines to {p}")


def delete_path():
    p = prompt_path("Enter file/directory path to delete: ")
    if not p.exists():
        print("Path does not exist.")
        return
    confirm = input(f"Are you sure you want to delete '{p}'? (yes/no): ")
    if confirm.lower() != 'yes':
        print('Aborted.')
        return
    if p.is_dir():
        shutil.rmtree(p)
    else:
        p.unlink()
    print(f"Deleted {p}")


def rename_path():
    p = prompt_path("Enter file/directory path to rename: ")
    if not p.exists():
        print("Path does not exist.")
        return
    new = prompt_path("Enter new path/name: ")
    new.parent.mkdir(parents=True, exist_ok=True)
    p.rename(new)
    print(f"Renamed {p} -> {new}")


def copy_path():
    src = prompt_path("Enter source file path to copy: ")
    if not src.exists():
        print("Source does not exist.")
        return
    dst = prompt_path("Enter destination path (file or directory): ")
    if dst.exists() and dst.is_dir():
        dst = dst / src.name
    dst.parent.mkdir(parents=True, exist_ok=True)
    if src.is_dir():
        shutil.copytree(src, dst)
    else:
        shutil.copy2(src, dst)
    print(f"Copied {src} -> {dst}")


def move_path():
    src = prompt_path("Enter source path to move: ")
    if not src.exists():
        print("Source does not exist.")
        return
    dst = prompt_path("Enter destination path: ")
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.move(str(src), str(dst))
    print(f"Moved {src} -> {dst}")


def make_dir():
    p = prompt_path("Enter directory path to create: ")
    p.mkdir(parents=True, exist_ok=True)
    print(f"Created directory: {p}")


def search_files():
    base = prompt_path("Search base path (leave empty for current): ")
    pattern = input("Enter glob pattern (e.g. *.txt or **/*.py): ").strip() or '*'
    matches = list(base.glob(pattern)) if pattern.find('**') >= 0 else list(base.glob(pattern))
    if not matches:
        print("No matches found.")
        return
    print(f"Found {len(matches)} matches:")
    for m in matches:
        print(m)


def show_menu():
    print("""
Basic File Management System - Menu
1) List directory
2) Show file/directory info
3) Create file
4) Read file
5) Write (overwrite) file
6) Append to file
7) Delete file/directory
8) Rename file/directory
9) Copy file/directory
10) Move file/directory
11) Create directory
12) Search files (glob)
0) Exit
""")


def main():
    while True:
        try:
            show_menu()
            choice = input("Choose an option: ").strip()
            if choice == '1':
                list_dir()
            elif choice == '2':
                show_info()
            elif choice == '3':
                create_file()
            elif choice == '4':
                read_file()
            elif choice == '5':
                write_file()
            elif choice == '6':
                append_file()
            elif choice == '7':
                delete_path()
            elif choice == '8':
                rename_path()
            elif choice == '9':
                copy_path()
            elif choice == '10':
                move_path()
            elif choice == '11':
                make_dir()
            elif choice == '12':
                search_files()
            elif choice == '0':
                print('Goodbye!')
                break
            else:
                print('Invalid choice. Try again.')
        except KeyboardInterrupt:
            print('\nInterrupted. Type 0 to exit or press Enter to continue.')
        except Exception as e:
            print(f"Error: {e}")
        input('\nPress Enter to continue...')
        clear_screen()


if __name__ == '__main__':
    clear_screen()
    main()
