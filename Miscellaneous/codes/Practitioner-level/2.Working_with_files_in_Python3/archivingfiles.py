import zipfile
#creating a ZIP files
to_zip =[]

def create_file(zipf,files,opt):
    with zipfile.ZipFile(zipf,opt,allowZip64=True) as zip:
        for file in files:
            zip.write(file)

create_file('archive.zip',to_zip,'w')

# Adding files to ZIP file

to_add =[]
def add_file(zipf,files,opt):
    with zipfile.ZipFile(zipf,opt,allowZip64=True) as zip:
        for f in files:
            lst = zip.namelist()
            if not f in lst:
                zip.write(f)
            else:
                print('file exist in zip')


#Reading a ZIP file

def read_zip(zipf):
    with zipfile.ZipFile(zipf,'r') as zip:
         lst = zip.namelist()
         for i in lst:
             zfinfo = zip.getinfo(i)
            print('{i} => {zfinfo.file_size}bytes, {zfinfo.filename}'.format(zfinfo=zfinfo)

read_zip('archive.zip')

#extracting a ZIP file

def extracting_zip_file(zipf,fn,path):
    with zipfile.ZipFile(zipf,'r') as zip:
        zip.extract(fn,path)

def extract_zip(zipf,path):
    with zipfile.ZipFile(zipf,'r') as zip:
        zip.extractall(path)

extracting_zip_file('..')
extract_zip('archive')

