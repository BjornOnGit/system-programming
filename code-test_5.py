#!/usr/bin/python3
import os
import sys
"""truncates a file to a certain number of bytes"""
if (len(sys.argv) < 3):
    print ("USAGE: ./trunc [filepath] [length]")
else:
    fl = os.open(sys.argv[1], os.O_RDWR)
    os.ftruncate(fl, int(sys.argv[2]))
    os.close(fl)
