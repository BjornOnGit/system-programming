#!/usr/bin/python3
import os
import sys
"""encodes a given filename and decodes it"""
if (len(sys.argv) < 2):
    print ("USAGE: ./fsencode [filepath]")
else:
    pth = os.fsencode(sys.argv[1])
    print("encoded path: {}".format(pth))
    print("decoded path: {}".format(os.fsdecode(pth)))
