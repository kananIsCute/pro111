import os
import shutil

from_dir = "/Users/your_username/Downloads"
to_dir = "/Users/your_username/Documents/Document_Files"

list_of_files = os.listdir(from_dir)
print(list_of_files)  # uncomment to see the list of files

# print(list_of_files)  # comment this line

for file in list_of_files:
    name, extension = os.path.splitext(file)
    print(f"File Name: {name}, Extension: {extension}")