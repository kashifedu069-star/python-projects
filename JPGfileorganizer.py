import os
import shutil

def move_jpg_files():
    print("================================")
    print("       JPG FILE ORGANIZER")
    print("================================")

    source=input("Enter source folder path:").strip()
    destination=input("Enter destination folder path:").strip()

    if not os.path.exists(source):
        print("Source folder does not exist.")
        return

    if not os.path.exists(destination):
        os.makedirs(destination)
        print("Destination folder created.")

    files=os.listdir(source)
    jpg_files=[]

    for file in files:
        if file.lower().endswith(".jpg"):
            jpg_files.append(file)

    if len(jpg_files)==0:
        print("No JPG files found.")
        return

    print("\nJPG files found:",len(jpg_files))

    for file in jpg_files:
        source_path=os.path.join(source,file)
        destination_path=os.path.join(destination,file)

        shutil.move(source_path,destination_path)
        print("Moved:",file)

    print("\nAll JPG files have been moved successfully.")

move_jpg_files()