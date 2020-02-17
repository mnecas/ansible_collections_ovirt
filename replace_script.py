#!/usr/bin/env python3

from optparse import OptionParser
import os
import fileinput


def get_path():
    parser = OptionParser()
    parser.add_option("-p", "--path", dest="path",
                      help="path", metavar="PATH")
    (options, args) = parser.parse_args()
    if options.path:
        path = options.path
    else:
        path = args[0]
    return path

def main():
    path = get_path()
    files = [path+"/"+file for file in os.listdir(path) if file[-3:]==".py"]
    search_text= "ansible.module_utils.ovirt"
    new_text= "ansible_collections.mnecas.ovirt.plugins.module_utils.ovirt"

    f = fileinput.input(files, inplace=True)
    for line in f:
        new_line = line.replace(search_text, new_text)
        print(new_line, end="")
    f.close()

    search_text2= "version_added"
    for file in files:
        with open(file, "r") as f:
            lines = f.readlines()
        with open(file, "w") as f:
            for line in lines:
                if search_text2 not in line.strip("\n"):
                    f.write(line)
    print("FINISHED")


if __name__ == "__main__":
    main()
