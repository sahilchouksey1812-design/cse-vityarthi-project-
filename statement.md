# Problem Statement
Modern desktop users and developers often need a lightweight, cross-platform tool to perform common filesystem tasks from the terminal without relying on heavyweight file managers or GUIs. Existing solutions can be overkill for quick operations or for scripting simple workflows. This project provides a minimal, interactive CLI file manager to simplify routine file and directory tasks.

# Scope of the Project
In scope:
- Interactive, menu-driven CLI for common filesystem operations.
- Cross-platform support (Windows, macOS, Linux) using Python standard library.
- Operations for listing, creating, reading, writing, appending, renaming, copying, moving, deleting files and directories.
- Glob-based search and basic file metadata display.
- Safe interactive prompts (confirmation for destructive actions).

Out of scope:
- Advanced file permissions management, network filesystems, or GUI interface.
- Concurrent/multi-user access controls or complex conflict resolution.
- Robust transactional undo/redo of file operations.

# Target Users
- Developers and power users who prefer CLI tools for quick filesystem tasks.
- Students learning filesystem APIs and scripting with Python.
- System administrators who need a simple interactive utility for ad-hoc file management.
- Anyone who wants a small, self-contained tool to automate basic file operations.

# High-level Features
- Directory listing with clear file/dir indicators and sizes.
- File and directory information (size, created/modified/accessed timestamps).
- Create files and directories (automatic parent creation).
- Read, overwrite (write), and append file contents (multi-line input terminated by a sentinel).
- Delete files and recursive directories with confirmation prompt.
- Rename files and directories.
- Copy files and directories (preserving metadata for files).
- Move files and directories.
- Search files using glob patterns (including recursive patterns like **/*.py).
- Menu-driven CLI UI with simple prompts and clear feedback.