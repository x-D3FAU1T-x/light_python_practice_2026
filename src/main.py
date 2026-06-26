from pathlib import Path
from scanner import collect_items
from report import make_report

def main():
    folder_input = input("Введите путь к папке: ").strip()
    folder_path = Path(folder_input)
    if not folder_path.exists():
        print("Ошибка: указанная папка не существует.")
        return

    if not folder_path.is_dir():
        print("Ошибка: путь должен указывать на папку, а не на файл.")
        return

    files, dirs = collect_items(folder_path)
    make_report(files, dirs)

if __name__ == "__main__":
    main()
