from pathlib import Path
from scanner import collect_items, show_tree
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

    print("\nДерево папок:")
    show_tree(folder_path)

    print("\nОтчёт:")
    files, dirs = collect_items(folder_path)
    make_report(files, dirs)

if __name__ == "__main__":
    main()
