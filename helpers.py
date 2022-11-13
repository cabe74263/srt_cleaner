import glob
import re


def read_files(current_directory):
    srt_files = []
    for file in glob.iglob(current_directory + "/**/*.srt", recursive=True):
        srt_files.append(file)
    return srt_files


def read_file_to_list(current_file):
    read_file = []
    sub_object = []
    with open(current_file, "r") as file_to_check:
        new_file = file_to_check.readlines()
        last = new_file[-1]
        file_to_check.seek(0)
        for line in new_file:
            if re.match("(^\d+\n)", line):
                sub_object = []
            sub_object.append(line)
            if line == "\n" or line is last:
                read_file.append(sub_object)
    return read_file


def remove_ads(file_list):
    count = 0
    cleaned_subs = []
    for line_object in file_list:
        count += 1

        # check if sub line should be removed
        delete_row = False
        for sub_line in line_object:
            for line in offending_lines():
                if line in sub_line:
                    delete_row = True
                    count = count - 1
        if not delete_row:
            line_object[0] = f"{count}\n"
            cleaned_subs.append(line_object)
    return cleaned_subs


def write_file(file_list, file_name):
    with open(file_name, "w") as newFile:
        for line in file_list:
            for item in line:
                # if last in file_list:
                #     continue
                newFile.write(item)


def offending_lines():
    lines = [
        "Please rate this subtitle at",
        "www.OpenSubtitles"]
    return lines
