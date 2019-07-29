import os
#import shutil
from os import path


def main():
# make a duplicate of an existing file
    if path.exists("Projectmohan1678.py"):

# get the path to the file in the current directory
        src = path.realpath("Projectmohan1678.py")

# rename the original file
        os.rename("Projectmohan1678.py", "RenameMohan1678.py")


if __name__ == "__main__":
    main()
