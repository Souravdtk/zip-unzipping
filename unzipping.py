from zipfile import ZipFile
import os

path=input('provide the directory path\n').strip().strip('\\')
dest=input('provide the destination path\n').strip().strip('\\')
#path=path.replace()
l=os.listdir(path)
# specifying the zip file name
#file_name = "my_python_files.zip"

# opening the zip file in READ mode
for i in l:
    if i.find('.zip') > -1:
        with ZipFile(path+'\\'+i, 'r') as zip:
                # printing all the contents of the zip file
                zip.printdir()

                # extracting all the files
                print('Extracting all the files now...')
                zip.extractall(dest)
                print('Done!')

