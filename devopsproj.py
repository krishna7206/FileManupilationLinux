#!/usr/bin/env python3
import os
import re
import sys
import operator
import subprocess


#Checks the verison directory and extracts version number from version.txt using regex expression
version = os.listdir(sys.argv[1])
full_path_version = os.path.abspath(sys.argv[1]+"/"+version[0])
version_initial = 0
with open(full_path_version,"r") as file:
    line = file.readline()
    v = re.findall('[0-9]+',line)
    version_initial = (int)(v[0])

#opens files in shellscript creates a dictionary with the numbers in file name as key and values as the actual file name, this will help in sorting and we can execute scripts in numerical order 
script = os.listdir(sys.argv[2])
dict_filenames = {}
for file in script:
    result = ''.join(re.findall('[0-9]+',file))
    val = (int)(result)
    dict_filenames[val] = file


#from a sorted dictionary we can make sure the shellscripts are executed in numerical order using subprocess and each time a new shell script is overwritten version is also updated accordingly
for key in sorted(dict_filenames):
    if (key > version_initial):
        subprocess.run(os.path.abspath(sys.argv[2]+"/"+dict_filenames[key]),shell=True,check=True)
        
        with open(full_path_version,"w") as f:
            f.write("Version Number="+(str)(key))
