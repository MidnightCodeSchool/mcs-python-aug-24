"""
cp: copy file
mv: move file, rename file
ls: list files
touch: create file
cd: change directory
pwd: current work directory
"""
import os
import shutil

with open("files/01.txt", "r") as file:
    print(file.read())

shutil.copy("files/01.txt", "files/05.txt")
shutil.move("files/05.txt", "files/temp/05.txt")

folder = "files"
files = os.listdir(folder)
for file in files:
    file_path = f"{folder}/{file}"
    new_file_path = f"{folder}/0{file}"
    os.rename(file_path, new_file_path)