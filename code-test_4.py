#!/usr/bin/python3
import os
import sys
"""generates a directory in your cwd"""
if (len(sys.argv) < 2):
    print ("USAGE: ./makedirs [filepath]")
else:
    os.makedirs(sys.argv[1])
