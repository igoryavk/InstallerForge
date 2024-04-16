from shutil import rmtree
from os import mkdir
from os.path import exists
path="C://parse//ExportFiles"
if exists(path):
    rmtree(path)
mkdir(path)