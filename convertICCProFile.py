import os
import time
import subprocess


cache_folder = "E:/convertICCProFile_cache"
input_folder = "E:/convertICCProFile_input"
output_folder = "E:/convertICCProFile_output"

icc_profile = "./sRGB_IEC61966-2-1_no_black_scaling.icc"

allowed_extensions = [".jpg", ".jpeg", ".png"]

interval_seconds = 10


def create_folders():
    # 要创建的文件夹路径列表
    folders = [cache_folder, input_folder, output_folder]

    for folder in folders:
        if not os.path.exists(folder):
            os.makedirs(folder)
            print(f"Created folder: {folder}")


# 转换图片格式的函数
def convert_image_format(input_path, output_path):
    try:
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
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(f"Converted image: {input_path} -> {output_path}")
        # print(result)
    except Exception as e:
        print(f"Failed to convert image: {input_path}\nError: {e}")


def check_input_folder():
    for file_name in os.listdir(input_folder):
        file_path = os.path.join(input_folder, file_name)
        file_extension = os.path.splitext(file_name)[1].lower()

        if file_extension in allowed_extensions:
            output_file_name = os.path.basename(file_name)
            output_file_path = os.path.join(output_folder, output_file_name)
            convert_image_format(file_path, output_file_path)
            os.remove(file_path)


def main():
    create_folders()

    try:
        while True:
            check_input_folder()
            time.sleep(interval_seconds)
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
