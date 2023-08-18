import os
import time
import subprocess
import shutil

cache_folder = "E:/convertICCProFile_cache"
input_folder = "E:/convertICCProFile_input"
output_folder = "E:/convertICCProFile_output"

icc_profile = "./sRGB_IEC61966-2-1_no_black_scaling.icc"

allowed_extensions = [".jpg", ".jpeg", ".png", ".heic"]

interval_seconds = 10


def create_folders():
    # 要创建的文件夹路径列表
    folders = [cache_folder, input_folder, output_folder]

    for folder in folders:
        if not os.path.exists(folder):
            os.makedirs(folder)
            print(f"Created folder: {folder}")


def create_subfolder_cache_path(root_dir):
    for root, dirs, _ in os.walk(root_dir):
        for dir_name in dirs:
            dir_path = os.path.join(root, dir_name)
            cache_sub_folder = dir_path.replace(
                "convertICCProFile_input", "convertICCProFile_cache"
            )
            if not os.path.exists(cache_sub_folder):
                os.makedirs(cache_sub_folder, exist_ok=True)
                print(f"Created {cache_sub_folder}")


def create_subfolder_output_path(root_dir):
    for root, dirs, _ in os.walk(root_dir):
        for dir_name in dirs:
            dir_path = os.path.join(root, dir_name)
            output_sub_folder = dir_path.replace(
                "convertICCProFile_input", "convertICCProFile_output"
            )
            if not os.path.exists(output_sub_folder):
                os.makedirs(output_sub_folder, exist_ok=True)
                print(f"Created {output_sub_folder}")


def check_input_folder(root_dir):
    for root, _, files in os.walk(root_dir):
        for file_name in files:
            input_file_path = os.path.join(root, file_name)
            file_extension = os.path.splitext(file_name)[1].lower()

            if file_extension in allowed_extensions:
                # 构建 cache 文件夹中的文件路径
                cache_file_path = input_file_path
                cache_file_path = cache_file_path.replace(
                    "convertICCProFile_input", "convertICCProFile_cache"
                )

                # 构建 output 文件夹中的文件路径
                output_file_path = input_file_path
                output_file_path = output_file_path.replace(
                    "convertICCProFile_input", "convertICCProFile_output"
                )

                # 转换文件
                convert_image_format(input_file_path, output_file_path)

                # 备份文件到 cache 文件夹
                shutil.move(input_file_path, cache_file_path)
                print(f"Moved file: {input_file_path} -> {cache_file_path}")


def convert_image_format(input_path, output_path):
    try:
        # 更新输出路径
        dir_name = os.path.dirname(output_path)
        file_name = os.path.basename(output_path)  # 提取输出路径中的文件名（包含扩展名）
        file_name_prefix = os.path.splitext(file_name)[0]  # 提取文件名的前缀部分
        output_path = os.path.join(dir_name, file_name_prefix + ".JPG")  # 更新输出路径为带有 .JPG 扩展名的文件名

        # magick convert "%~1" -profile .\sRGB_IEC61966-2-1_no_black_scaling.icc "%~dpn1-output.JPG"
        command = [
            "magick",
            "convert",
            input_path,
            "-strip",
            "-profile",
            icc_profile,
            output_path,
        ]
        command = ['magick', 'convert', input_path, '-strip', '-profile', icc_profile, output_path]
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(f"Converted image: {input_path} -> {output_path}")
        print(result)
    except Exception as e:
        print(f"Failed to convert image: {input_path}\nError: {e}")


def remove_empty_folders(folder_path):
    for root, dirs, _ in os.walk(folder_path, topdown=False):
        for dir_name in dirs:
            dir_path = os.path.join(root, dir_name)
            if not os.listdir(dir_path):
                os.rmdir(dir_path)
                print(f"Removed empty folder: {dir_path}")


def main():
    create_folders()

    try:
        while True:
            create_subfolder_cache_path(input_folder)
            create_subfolder_output_path(input_folder)
            check_input_folder(input_folder)
            remove_empty_folders(input_folder)
            time.sleep(interval_seconds)
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
