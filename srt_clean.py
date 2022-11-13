import os
from pathlib import Path
import logging
from helpers import *

logging.basicConfig(filename='error.log', filemode='w',
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')

current_directory = os.getcwd()
# current_directory = "C:\\media\\temp"

files = read_files(current_directory)

for item in files:
    print(item)

print("")

for file in files:
    try:
        original_subs = read_file_to_list(file)
        cleaned_subs = remove_ads(original_subs)

        if not original_subs == cleaned_subs:
            if ".srt" in file:
                p = Path(file)
                p.rename(p.with_suffix(".original"))
                write_file(cleaned_subs, file)
    except Exception as e:
        logging.error(f"Ran into an issue trying to deal with '{file}'! It was \n", exec_info=True)
