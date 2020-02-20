import os
import sys
import shutil

extension = input("Enter the file extension to be searched throught the device and copied:")
root_directory = input("Enter the root directory from which you want to start the sreach:")
dumping_folder_directory = input("Enter the dumping folder direcoty:");

print("\nExtension: "+extension)
print("Root: "+root_directory)
print("Dump: "+dumping_folder_directory)

file_list = []
count = 0
for root, sub_folders, files in os.walk(root_directory):
    for file in files:
       if file.endswith(extension):
           if file not in file_list:
               file_list.append(file)
               new_file = root+'/'+str(file)
               shutil.copy(new_file,dumping_folder_directory)




           