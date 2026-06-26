import sys
from pathlib import Path
from scanner import collect_items
from report import make_report

def main():
    if len(sys.argv) < 2:
        print("Ошибка: укажите путь к папке при запуске программы.")
        print("Пример: python main.py C:\\Users\\i5\\Documents")
        return

    folder_path = Path(sys.argv[1])

    if not folder_path.exists():
        print("Ошибка: указанная папка не существует.")
        return

    if not folder_path.is_dir():
        print("Ошибка: путь должен указывать на папку, а не на файл.")
        return

    files, dirs = collect_items(folder_path)
    make_report(files, dirs)

