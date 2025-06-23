import os
from os import path

def main():
    print(os.name)
    print(path.realpath("textfile.txt"))
main()