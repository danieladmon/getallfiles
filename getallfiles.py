'''
getallfiles.py by Daniel Admon

finds all files in {dir} directory + subdirectories
and move them to {newdir}

'''
import os

newdir = "E:\\Backup\\FB_ALL";
dir = "E:\\Backup\\facebook";
# -- more options:
#dir = os.getcwd()
#dir = input("Please type path to the folder:  ")

if not os.path.exists(dir):
    print(f"Error: directory \"{dir}\" doesn't exist.")
    exit()

if not os.path.exists(newdir):
    os.makedirs(newdir)

count = 0
for path, subdirs, files in os.walk(dir):
    for name in files:
        check = os.path.join(path, name)
        movedfile = os.path.join(newdir, name)
        if os.path.isfile(check):
            try:
                os.rename(check, movedfile)
            except IOError as error:
                print(error)
            except:
                print('An error occured.')
            else:
                print(f"File: {check} moved to: {newdir}")
                count += 1


print(f"total moved: {count}")
