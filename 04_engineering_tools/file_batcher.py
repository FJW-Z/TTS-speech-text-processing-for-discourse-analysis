import os
import shutil
import math

def batch_files(path, folder_path, files_per_folder):
    # 中文注释：按数量拆分文件夹中的文件到子文件夹
    # English note: Split files in a folder into sub-folders by quantity
    path = path.strip()
    folder_path = folder_path.strip()
    file_list = os.listdir(path)
    num_folders = math.ceil(len(file_list) / files_per_folder)
    # 创建子文件夹
    for folder_num in range(num_folders):
        new_folder = os.path.join(folder_path, f"{folder_num}")
        if not os.path.exists(new_folder):
            os.makedirs(new_folder)
    # 移动文件
    for i, file in enumerate(file_list):
        old_file = os.path.join(path, file)
        if os.path.isdir(old_file) or not os.path.exists(old_file):
            continue
        folder_num = i // files_per_folder
        new_file = os.path.join(folder_path, f"{folder_num}", file)
        shutil.move(old_file, new_file)
        print(f"文件 {file} 已移动到 {new_file}")

# 示例调用
batch_files(r"C:\Users\total", r"C:\Users\fz\needed", 100)
