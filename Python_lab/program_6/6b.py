import os
import sys
import pathlib
import zipfile

dirName=input("enter the directory name that you want to backup:")
if not os.path.isdir(dirName):
    print("Directory",directory,"does not exists")
    sys.exit(0)
    
curDirectory=pathlib.Path(dirName)
    
with zipfile.ZipFile("C:\\Users\\jaswa\\Desktop\\7"C:\Users\jaswa\Desktop\lab"b.zip","w") as f:
    for file_path in curDirectory.rglob("*"):
        f.write(file_path,arcname=file_path.relative_to(curDirectory))
print(file_path)

if os.path.isfile("C:\\Users\\jaswa\\Desktop\\6b.zip"):
    print("Zip file created successfully")
else:
    print("Zip file not created")
    
