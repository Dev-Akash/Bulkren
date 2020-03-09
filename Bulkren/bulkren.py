import os
import sys
import argparse
import shutil
from tqdm import tqdm

def run():
    ap = argparse.ArgumentParser(description="Bulkren can reduce your finger pains, just rename files in bulk by using following command:  'bulkren -i <input_folder> ' for more help run 'bulkren -h'")
    ap.add_argument("-i", "--input", required=True, help="Absolute path of input folder")
    ap.add_argument("-o", "--output", help="Path to output folder for renamed files (default = 'output')")
    ap.add_argument("-p", "--pattern", help="Pattern for renaming such as 'file_XYZ' or 'input_file_XYZ' where XYZ will be file number")
    
    args = vars(ap.parse_args())

    input_path = args["input"]
    output_path = args["output"]
    pattern = args["pattern"]
    pattern = pattern[:-3]

    if output_path == None:
        #Create output folder
        parent = os.path.dirname(input_path)
        output_path =  os.path.join(parent, "output")
        try:
            os.mkdir(output_path)
        except:
            print("%s directory already exists"%(output_path))
            sys.exit()
    
    print("OUTPUT FOLDER: %s"%(output_path))

    file_list = os.listdir(input_path)

    for e,i in enumerate(tqdm(file_list)):
        file_path = os.path.join(input_path, i)
        if not os.path.isdir(file_path):
            index = i.index('.')
            ext = i[index:]
            paste_path = os.path.join(output_path, pattern+str(e)+ext)
            shutil.copy(file_path, paste_path)