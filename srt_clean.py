import os
from helpers import *


current_directory = os.getcwd()
# current_directory = "C:\\media\\temp"

files = read_files(current_directory)

for item in files:
    print(item)

print("")


for file in files:
    sub_list = read_file_to_list(file)

    cleaned_subs = remove_ads(sub_list)

    if not sub_list == cleaned_subs:
        index = file.find('.srt')
        if "_FIXED" not in file:
            new_file_name = file[:index] + "_FIXED" + file[index:]
            write_file(cleaned_subs, new_file_name)
