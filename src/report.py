def make_report(files, dirs):
    file_count = len(files)
    dir_count = len(dirs)
    total_size = sum(f.stat().st_size for f in files)
    print(f"Файлов: {file_count}")
    print(f"Папок: {dir_count}")
    print(f"Общий размер: {total_size} байт")

    ext = ".txt"
    filtered = [f for f in files if f.suffix == ext]
    print(f"\nФайлы с расширением {ext}: найдено {len(filtered)}")
    for f in filtered:
        print(f"  {f}")
   