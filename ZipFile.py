import os
import shutil
from zipfile import ZipFile
from os import path
from shutil import make_archive

    # Check if file exists
       if path.exists("ZipFile.py"):
    # get the path to the file in the current directory
        src = path.realpath("ZipFile.py");
    # rename the original file
        os.rename("career.FirstProject","ZipFile.py")
    # now put things into a ZIP archive
        root_dir,tail = path.split(src)
        shutil.make_archive("FirstProject archive","zip",root_dir)
    # more fine-grained control over ZIP files
        with ZipFile("FirstProject.zip", "w") as newzip:
            newzip.write("ZipFile.py")
            newzip.write("ZipFile.py.bak")