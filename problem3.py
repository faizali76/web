import os
# Specify the directory you want to list
directory_path = '/Users'
# list all file and directory in the specified path
contents = os.listdir(directory_path)
# print each file and directory name
for item in contents:
    print(item)