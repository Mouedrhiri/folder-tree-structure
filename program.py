import os
from tqdm import tqdm
from time import sleep
def progress(rang):
    for i in tqdm(rang, desc ="Progress : "):
            sleep(.1)

folder = input("Enter The Folder Path : ")
for path, subdirs, files in os.walk(rf'{folder}'):
     progress(path)
     for name in files:
             print(os.path.join(path, name))