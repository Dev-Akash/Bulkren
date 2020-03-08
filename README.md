# Bulkren
[![PyPI version](https://badge.fury.io/py/Bulkren.svg)](https://badge.fury.io/py/Bulkren)
![GitHub Releases](https://img.shields.io/github/downloads/Dev-Akash/Bulkren/v1.0.2/total?color=yellow&label=Downloads&style=plastic)

A simple PYPI package for bulk renaming files inside a folder. 

## How to Install

`pip install Bulkren `

## How to Use 

- Open Terminal.
- Install **Bulkren** using the above command.
- Run `python -m Bulkren -h` for help.

### Usage

The package can be used as follows:

`python -m Bulkren -i <input_folder_path> -o <output_folder_path> -p <patter_to_rename>`

### Example

`python -m Bulkren -i C:\User\Akash\Desktop\input_folder -o C:\User\Akash\Desktop\output_folder -p images_XYZ`

This above example will take all the files in `C:\User\Akash\Desktop\input_folder` and then rename it with pattern `images_XYZ` where **XYZ** would be replaced number count of file (remember to add XYZ in end only) and will save it to the `C:\User\Akash\Desktop\output_folder` folder.

**Note :** If the -o argument is not passed then it will automatically create a `output` named folder in same parent directory, for above example the output folder path would be `C:\User\Akash\Desktop\output`

#### Definitions

- `-i or --input` takes input folder path
- `-o or --output` takes output folder path
- `-p or --pattern` takes pattern for renaming files.

**where**

`-i` is `required` parameter

`-o` is `optional` parameter

`-p` is `required` parameter