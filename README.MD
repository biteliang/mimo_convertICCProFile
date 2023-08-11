# ConvertICCProFile

ConvertICCProFile 是一个用于批量转换图像文件格式并应用 ICC 配置文件的 Python 程序。

## 功能

- 监视指定文件夹中的图像文件，并将其转换为指定的输出格式。
- 支持 JPEG 和 PNG 图像文件的转换。
- 应用指定的 ICC 配置文件以确保颜色准确性。
- 保持输出文件与原文件夹结构一致。

## 使用方法

1. 在程序中设置输入文件夹、输出文件夹和 ICC 配置文件路径。
2. 确保已安装 ImageMagick，并将 `magick` 命令添加到系统的 PATH 环境变量中。
3. 运行 `convertICCProFile.py` 文件。

## 注意事项

- 请根据实际情况修改代码中的文件夹路径和 ICC 配置文件路径。
- 请确保已安装 ImageMagick 并设置了正确的环境变量。
- 程序将监视输入文件夹，并在发现新的图像文件时进行转换，转换后的文件保存在输出文件夹中。

## 依赖

- Python 3.x
- ImageMagick

