#getting file attribute(getting modified date of the files
import os
from datetime import datetime

def get_date(timestamp):
    return datetime.utcfromtimestamp(timestamp).strftime('%d %b %Y')

def get_file_att(fld):
    with os.scandir(fld) as dir:
        for f in dir:
            if f.is_file():
                inf = f.stat()
                print(f'Modified{get_date(inf.st_mtime)}: {f.name}')

#traversing a directory

def traverse(fld):
    for fldpath,dirs,fls in os.walk(fld):
        print(fldpath)
        for f in fls:
            print(f)

traverse('..')

#copying files
import shutil

def copy_file(fld,dst):
    shutil.copy(fld,dst)

def copy_dir(fld,dst):
    shutil.copytree(fld,dst)

copy_file('..''..')
copy_dir('..''..')

#moving files

def mv_files(src,dst):
    shutil.move(src,dst)

mv_files('..','..')

#renaming files
def rename1(src,dst):
    os.rename(src,dst)

def rename2(src,dst):
    f = Path(src)
    f.rename(dst)

rename1('..','..')
rename2('..','..')

#deleting files

def deleting_file(fld):
    if os.path.isfile(fld):
        try:
            os.remove(fld)
        except OSError as e:
            print(e)
    else:
        print('File not found')

deleting_file('..')
