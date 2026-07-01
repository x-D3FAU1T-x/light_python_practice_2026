from pathlib import Path

def show_tree(root: Path, level=0):
    indent = "    " * level
    print(f"{indent}{root.name}")

    for item in root.iterdir():
        if item.is_dir():
            show_tree(item, level + 1)
        else:
            print(f"{indent}    {item.name}")


def collect_items(root: Path):
    files = []
    dirs = []

    def scan(path: Path):
        dirs.append(path)
        for item in path.iterdir():
            if item.is_dir():
                scan(item)
            else:
                files.append(item)

    scan(root)
    return files, dirs
