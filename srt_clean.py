import os
from pathlib import Path

from helpers import *


current_directory = os.getcwd()
# current_directory = "C:\\media\\temp"

files = read_files(current_directory)

for item in files:
    print(item)

print("")


for file in files:
    original_subs = read_file_to_list(file)
    cleaned_subs = remove_ads(original_subs)

    if not original_subs == cleaned_subs:
        if ".srt" in file:
            p = Path(file)
            p.rename(p.with_suffix(".original"))
            write_file(cleaned_subs, file)

