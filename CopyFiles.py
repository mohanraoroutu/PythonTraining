# # Example file for working with o.s path module
#
# import os
# from os import path
# import datetime
# from datetime import date, time, timedelta
# import time
#
# def main():
#
#
# #Get the modification time
#
#     t = time.ctime(path.getmtime("CopyFiles.py"))
#     print(t)
#     print(datetime.datetime.fromtimestamp(path.getmtime("CopyFiles.py")))
#
#
# if __name__ == "__main__":
#     main()


#50% correct

# COPY File using shutil.copy(), shutil.copystat()

import os
import shutil
from os import path


def main():
# make a duplicate of an existing file
    if path.exists("guru99.txt"):
# get the path to the file in the current directory
    src = path.realpath("CopyFiles.py");

# seperate the path from the filter
    head, tail = path.split(src)
    print("path:" + head)
    print("file:" + tail)

# let's make a backup copy by appending "bak" to the name
    dst = src + ".bak"
# now use the shell to make a copy of the file
    shutil.copy(src, dst)

# copy over the permissions,modification
    shutil.copystat(src, dst)


if __name__ == "__main__":
    main()

