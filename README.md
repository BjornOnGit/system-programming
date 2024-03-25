# Introduction

This project is an assignment for the course ECE 529 - 'System Programming' at Nnamdi Azikwe University, Awka. The project is an implementation of the various methods in Python's os module.

## Table of Content

- [Introduction](#introduction)
  - [Table of Content](#table-of-content)
  - [Methods Implemented](#methods-implemented)
  - [Code Examples](#code-examples)
  - [Team Members](#team-members)
  - [Conclusion](#conclusion)

## Methods Implemented

| Method   | Description| Usage  |
| -------- | -------- | -------- |
| os.stat()| A method in Python's os module that retrieves information about a file or directory specified by the path.  | `import os``<br>``stat_info = os.stat('path_to_file')``<br>``print(stat_info)` |
| os.fsencode() | A function in Python's os module that encodes a filename or a path to the filesystem encoding with 'surrogateescape' error handler, returns bytes unchanged. | import os `<br>`path = os.fsencode('path_to_file')`<br>``print(path)` |
| os.getenv() | A function in Python's os module that retrieves the value of an environment variable. If the environment variable is not present, it returns the default value provided. | import os `<br>`path = os.getenv('PATH')`<br>``print(path)` |
| os.makedirs() | a function in Python's os module that creates a directory recursively. This means that while making a new directory, if the subdirectories do not exist, then os.makedirs will create them as well. | import os`<br>``os.makedirs('dir/subdir')` |
| os.truncate() | a function in Python's os module that resizes a file to a specified size. If the file previously was larger than this size, the extra data is lost. | import os`<br>``os.truncate('path_to_file', size)` |

## Code Examples

os.stat()

```python
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

```

And it returns:

``` bash
bjorn@bjorn-IdeaPad-3-15IML05:~/Desktop/system-programming$ ./code-example_1.py README.md
File Details
Name: README.md
Size: 1650 B
Created: 10:21AM 25-03-2024
```

os.fsencode()

``` python
import os
import sys
"""encodes a given filename and decodes it"""
if (len(sys.argv) < 2):
    print ("USAGE: ./fsencode [filepath]")
else:
    pth = os.fsencode(sys.argv[1])
    print("encoded path: {}".format(pth))
    print("decoded path: {}".format(os.fsdecode(pth)))
```

returns:

``` bash
bjorn@bjorn-IdeaPad-3-15IML05:~/Desktop/system-programming$ ./code-test_2.py test.txt
encoded path: b'test.txt'
decoded path: test.txt
```

os.getenv()

``` python
import os
""" prints a couple of environmental variables """
print ("Home dir: {}".format(os.getenv("HOME")))
print ("Shell: {}".format(os.getenv("SHELL")))
print ("Working dir: {}".format(os.getenv("PWD")))
print ("Username: {}".format(os.getenv("USER")))
```

returns:

``` bash
bjorn@bjorn-IdeaPad-3-15IML05:~/Desktop/system-programming$ ./code-test_3.py
Home dir: /home/bjorn
Shell: /bin/bash
Working dir: /home/bjorn/Desktop/system-programming
Username: bjorn
```

os.makedirs()

``` python
import os
import sys
"""generates a directory in your cwd"""
if (len(sys.argv) < 2):
    print ("USAGE: ./makedirs [filepath]")
else:
    os.makedirs(sys.argv[1])
```

returns:

``` bash
bjorn@bjorn-IdeaPad-3-15IML05:~/Desktop/system-programming$ ./code-test_4.py test_folder
bjorn@bjorn-IdeaPad-3-15IML05:~/Desktop/system-programming$ ls
code-test_1.py  code-test_2.py  code-test_3.py  code-test_4.py  code-test_5.py  README.md  `test_folder`  test.txt
```

os.truncate()

``` python
import os
import sys
"""truncates a file to a certain number of bytes"""
if (len(sys.argv) < 3):
    print ("USAGE: ./trunc [filepath] [length]")
else:
    fl = os.open(sys.argv[1], os.O_RDWR)
    os.ftruncate(fl, int(sys.argv[2]))
    os.close(fl)
```

returns:

``` bash
bjorn@bjorn-IdeaPad-3-15IML05:~/Desktop/system-programming$ ./code-test_5.py test.txt 20
bjorn@bjorn-IdeaPad-3-15IML05:~/Desktop/system-programming$ cat test.txt
This is 15bjorn@bjorn-IdeaPad-3-15IML05:~/Desktop/system-programming
```

## Team Members

| Name     | Reg No.  |
| -------- | -------- |
| Eze Francis Ogonnaya  | 2019364049  |
| Igwilo Chidiebere Donatus  | 2019364050  |
| Okeke Tobenna Denning | 2019364052 |
| Ojocha Francis Chukwuemeka | 2019364055 |
| Okorie Michael Chukwuemeka | 2019364056 |
| Okolie Ronald | 2019364057 |
| Onwuezumma Tochukwu | 2019364058 |
| Odika Uchenna Favour | 2019364059 |
| Ajokubi Stephen C. | 2019364060 |
| Chukwu Emmanuel | 2019364061 |
| Ekwugha Nnaemeka ThankGod | 2019364064 |
| Ezealor Chinedum Miracle | 2019364066 |
| Obi Oluebube Faithfulness | 2019364067 |
| Obika Onyedika Nnachebe | 2019364068 |
| Ukokwele Helen Chisom | 2019364069 |
| Ezeonyeka Kosisochukwu | 2019364070 |
| Ogo Bright Chukwudi | 2019364071 |
| Nkwoemezie Godwin Chinedu | 2019364072 |
| Ibeabuchi Chiemelie Emmanuel | 2019364074 |
| Ozoemena Paschal Chiemerie | 2019364075 |
| Njike Beluchukwu Francis | 2018364056 |

## Conclusion

The os module in Python is a powerful module that provides a lot of functionalities for interacting with the operating system. The methods implemented in this project are just a few of the many methods available in the os module. The os module is a very useful module for system programming tasks and can be used to perform a wide range of operations on files, directories, and the operating system in general.
