import os

def get_folder_size(folder_path):
    total_size = 0
    for path, dirs, files in os.walk(folder_path):
        for f in files:
            fp = os.path.join(path, f)
            if os.path.exists(fp):  # Проверяем наличие файла
                total_size += os.path.getsize(fp)
    return total_size

def get_subfolder_sizes(folder_path):
    subfolder_sizes = {}
    for root, dirs, files in os.walk(folder_path):
        for d in dirs:
            folder = os.path.join(root, d)
            size = get_folder_size(folder)
            subfolder_sizes[folder] = size
        break  # Прерываем обход подпапок на первом уровне
    return subfolder_sizes

def print_folder_sizes(folder_sizes):
    for folder, size in folder_sizes.items():
        size_in_mb = size / (1024 * 1024)
        print(f"{folder}: {size_in_mb:.2f} MB")

def main():
    folder_path = input("Введите путь к папке: ")
    
    size_in_bytes = get_folder_size(folder_path)
    size_in_mb = size_in_bytes / (1024 * 1024)
    print(f"Размер папки: {size_in_mb:.2f} MB")
    
    subfolder_sizes = get_subfolder_sizes(folder_path)
    print("Размеры подпапок:")
    print_folder_sizes(subfolder_sizes)

if __name__ == "__main__":
    main()
