# SPDX-License-Identifier: MIT

# This is a simple script which adds a suffix to any file in a folder with the selected file type.

import os

# request directory path from end user
directory = input('Please enter the folder path!: ')
fileType = input('What is the specified file type? (ex: .jpg) : ')
suffix = input('what is the suffix you wish to add? : ')

# list all files within the directory
folder = os.listdir(directory)

# loop checking all files in directory that end with variable fileType
for filename in folder:

    # Check for specified file type

    if filename.endswith(fileType):
 
        # get the current path of the file in loop
        current_path = os.path.join(directory, filename)

        # creates variable for new file name with the added suffix
        new_filename = filename.split(".")[0] + suffix + fileType
        new_path = os.path.join(directory, new_filename)

        # renames the file replacing the previous name with the newly stored variable
        os.rename(current_path, new_path)

# let the user know that the process is complete
print(f"All {fileType} files have been renamed with the suffix {suffix}")

# Ensures terminal stays open until user is ready to close it
input("Press enter to close the program.")