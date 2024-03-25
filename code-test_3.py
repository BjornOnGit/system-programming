#!/usr/bin/python3
import os
""" prints a couple of environmental variables """
print ("Home dir: {}".format(os.getenv("HOME")))
print ("Shell: {}".format(os.getenv("SHELL")))
print ("Working dir: {}".format(os.getenv("PWD")))
print ("Username: {}".format(os.getenv("USER")))
