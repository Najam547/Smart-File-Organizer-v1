
import os 
import shutil

move =0
skip =0
fail =0
unknown =0

def move_file(moving_file,Folder,m,s,f) :
    if not os.path.isdir(Folder) :
        os.mkdir(Folder)
    try:
        shutil.move(moving_file,Folder)
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


print("Welcome to file organizer.")

source = input("Enter your source path : ")

if not os.path.isdir(source) :
    print("Source folder does not exists.")
    exit()

destination= input("Enter your destination path : ")

rules = {
        ".pdf"  : "PDF",
        ".txt"  : "Documents",
        ".doc"  : "Documents",
        ".docx" : "Documents",
        ".xls"  : "Excel",
        ".xlsx" : "Excel",
        ".jpeg" : "Images",
        ".png"  : "Images" ,
        ".jpg"  : "Images" ,
        ".mp4"  : "Videos" ,
        ".webm" : "Videos" ,
        ".py"   : "Python" ,
        ".pptx" : "Ppt" ,
        ".java" : "Java"
            }

for root,dirs,files in os.walk(source) :
    for file in files :
        file = os.path.join(root,file)
        file_size = os.path.getsize(file)
        file_name= os.path.basename(file)
        _,extension= os.path.splitext(file)

        if not os.path.isdir(destination):
            os.mkdir(destination)

        for dir in dirs :
            if os.path.basename(destination) == dir :
                dirs.remove(dir)
        
        found=0

        for key,value in rules.items():
            
            if extension == key:
                move,skip,fail=move_file(file,os.path.join(destination,value),move,skip,fail)
                found+=1
                print("File : ",file_name)
                print("Size : ",file_size)
                print("Type : ",key)

        if not found :
            unknown+=1


print("File moved : ",move)
print("File skipped : ",skip)
print("File failed : ",fail)
print("Unknown files : ",unknown)

