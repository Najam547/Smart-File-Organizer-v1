import os 
import shutil

move =0
skip =0
fail =0
unknown =0

def move_file(Folder,m,s,f) :
    if not os.path.isdir(Folder) :
        os.mkdir(Folder)
    try:
        shutil.move(file,Folder)
        print("File Successfully moved.")
        m+=1
    except FileExistsError :
        s+=1
        print("File already exists. Skipping.....")
    except FileNotFoundError :
        f+=1
        print("File not found.")
    except PermissionError :
        f+=1
        print("We dont have permission to move.")
    except OSError as e :
        f+=1
        print("System File failed because ",e)
    return m,s,f
        
source = input("Enter your source path : ")

if not os.path.exists(source) :
    print("Source folder does not exists.")
    exit()

os.chdir(source)
destination= input("Enter your destination path : ")

for root,dirs,files in os.walk(source) :
    for file in files :
        file = os.path.join(root,file)
        base,extension= os.path.splitext(file)
        if not os.path.isdir(destination):
            os.mkdir(destination)
        for dir in dirs :
            if os.path.basename(destination) == dir :
                dirs.remove(dir)
        if extension == ".pdf":
            move,skip,fail = move_file("PDF",move,skip,fail)
        elif extension == ".txt"or extension == ".doc":
            move,skip,fail = move_file("Documents",move,skip,fail)
        elif extension == ".xls"or extension == ".xlsx":
            move,skip,fail = move_file("Excel",move,skip,fail)
        elif extension == ".png" or extension == ".jpeg" or extension == ".jpg" :
            move,skip,fail = move_file("Images",move,skip,fail)
        elif extension ==".mp4" or extension ==".webm":
            move,skip,fail = move_file("Videos",move,skip,fail)
        elif extension == ".py" :
            move,skip,fail=move_file("Python",move,skip,fail)
        else :
            unknown+=1

print("File moved : ",move)
print("File skipped : ",skip)
print("File failed : ",fail)
print("Unknown files : ",unknown)