import os
import shutil
SOURCE_DIR = input('Enter File Path')
DEST_DIR = input("Enter Directory / Folder Path")

for fname in os.listdir(SOURCE_DIR):
    if fname.lower().endswith('.pdf'):
        shutil.move(os.path.join(SOURCE_DIR, fname), DEST_DIR)

