from sys import argv
import os

def main():
    name = argv[1]
    os.system("kaggle competitions download -c {}".format(name))
    os.system("mkdir {}".format(name))
    os.system("mkdir {}/data".format(name))
    os.system("mv {}.zip {}/data/".format(name, name))
    os.system("unzip '{}/data/{}.zip' -d {}/data/".format(name, name, name))
    print("Competition structure created")
    
    # can't just touch, need to insert some json into this file as well.
    os.system("touch {}/{}.ipynb".format(name, name))
    notebook = open("{}/{}.ipynb".format(name, name),"w")
    notebook.write("""{
     "cells": [],
      "metadata": {},
       "nbformat": 4,
        "nbformat_minor": 2
        }""")
    notebook.close()

    print("Notebook file created")

if __name__ == "__main__":
    print("Creating new competition for {}".format(argv[1]))
    main()
