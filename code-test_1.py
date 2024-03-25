#!/usr/bin/python3
import os
import sys
from pathlib import Path
import datetime

def getfileinfo(file: str):
   if not Path(file).exists():
       return f"{file} does not exist"
   elif Path(file).is_dir():
       return f"{file} is directory"
   if Path(file).is_file():
       file_info = os.stat(file)
       creation_time = (datetime.datetime.
                        fromtimestamp(file_info.st_ctime).strftime("%H:%M%p %d-%m-%Y"))
       stripped = (f"File Details\n"
                   f"Name: {file}\n"
                   f"Size: {file_info.st_size} B\n"
                   f"Created: {creation_time}"
                   )
       return stripped

if len(sys.argv) > 1:
   print(getfileinfo(sys.argv[1]))
else:
   print("No file specified")