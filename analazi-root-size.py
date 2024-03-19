import os

def get_folder_size(folder_path):
    total_size = 0
    for path, dirs, files in os.walk(folder_path):
        for f in files:
            fp = os.path.join(path, f)
            total_size += os.path.getsize(fp)
    return total_size

def get_largest_files(folder_path, num_files):
    file_sizes = []
    for path, dirs, files in os.walk(folder_path):
        for f in files:
            fp = os.path.join(path, f)
            file_sizes.append((fp, os.path.getsize(fp)))
    sorted_files = sorted(file_sizes, key=lambda x: x[1], reverse=True)
    return sorted_files[:num_files]

def main():
    folder_path = input("Введите путь к папке: ")
    size_in_bytes = get_folder_size(folder_path)
    size_in_mb = size_in_bytes / (1024 * 1024)
    print(f"Размер папки: {size_in_mb:.2f} MB")

    num_files = int(input("Введите количество файлов для вывода: "))
    largest_files = get_largest_files(folder_path, num_files)
    print(f"Самые большие файлы:")
    for file_path, file_size in largest_files:
        print(f"{file_path}: {file_size} байт")

if __name__ == "__main__":
    main()
