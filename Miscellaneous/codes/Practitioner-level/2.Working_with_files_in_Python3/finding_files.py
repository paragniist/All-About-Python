#listing directory

import os,fnmatch
from pathlib import Path


def finding_files(fld):
    for fn in os.listdir(fld):
        print(fn)

finding_files('..')

#how to use string methods:

def search_string(fld,search):
    for fn in os.listdir(fld):
        if fn.endswith(search):
            print(fn)

search_string('..','.txt')

def search_string2(fld,search):
    for fn in os.listdir(fld):
        if fn.startswith(search):
            print(fn)

search_string2('..','..')

#pattern matching by using fnmatch function

def pattern_matching(fld,search):
    for fn in os.listdir(fld):
        if fnmatch.fnmatch(fn,search):
            print(fn)

pattern_matching('..','.txt')
pattern_matching('..','*_file_*.*')

#pattern by using glob

def glob_function(fld,search):
    p=Path(fld)
    for n in p.glob(search):
        print(n)

glob_function('..','*_file_*')
