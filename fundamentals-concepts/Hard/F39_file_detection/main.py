'''

'''

import os
from pathlib import Path

BASE = Path(__file__).resolve().parent # we obtain exact directory of the program folder
file_path = BASE / "test" #basic file in same folder
file1_path = "/Users/coderafnan2824/Documents/test.txt" #absolute path: Independent and error free


if os.path.exists(file_path): # Check if file exists in filepath
    if os.path.isfile(file_path):   # check if given path is a file or not
        print("Its a file")
    elif os.path.isdir(file_path):
        print("It's a folder")
    else:
        print("Its not a file/folder")

else:
    print("It doesn't exist")


