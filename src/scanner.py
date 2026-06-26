import os
from pathlib import Path

def show_tree(root: Path):
    for dirpath, dirnames, filenames in os.walk(root):
        current = Path(dirpath)
        depth = len(current.relative_to(root).parts)
        indent = "    " * depth

        print(f"{indent}{current.name if depth > 0 else current}")

        file_indent = "    " * (depth + 1)
        for name in filenames:
            print(f"{file_indent}{name}")

def collect_items(root: Path):
    files = []
    dirs = []
    for dirpath, dirnames, filenames in os.walk(root):
        current = Path(dirpath)
        dirs.append(current)

        for name in filenames:
            files.append(current / name)

    return files, dirs

