import os

def get_folder_size(folder_path):
    total_size = 0
    for path, dirs, files in os.walk(folder_path):
        for f in files:
            fp = os.path.join(path, f)
            total_size += os.path.getsize(fp)
    return total_size

def get_subfolder_sizes(folder_path):
    subfolder_sizes = {}
    for root, dirs, files in os.walk(folder_path):
        for d in dirs:
            folder = os.path.join(root, d)
            size = get_folder_size(folder)
            subfolder_sizes[folder] = size
    return subfolder_sizes

def main():
    folder_path = input("Введите путь к папке: ")
    
    size_in_bytes = get_folder_size(folder_path)
    size_in_mb = size_in_bytes / (1024 * 1024)
    print(f"Размер папки: {size_in_mb:.2f} MB")
    
    subfolder_sizes = get_subfolder_sizes(folder_path)
    print("Размеры подпапок:")
    for subfolder, size in subfolder_sizes.items():
        size_in_mb = size / (1024 * 1024)
        print(f"{subfolder}: {size_in_mb:.2f} MB")

if __name__ == "__main__":
    main()
