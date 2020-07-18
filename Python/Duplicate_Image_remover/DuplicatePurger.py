import filecmp
import os

files_list=os.listdir()

"""for pics in files_list:
    if pics!= '1.png':
        if filecmp.cmp("1.png",pics):
            os.remove(pics)
            print("similar")
        else:
            print("non similar")"""
print(files_list)