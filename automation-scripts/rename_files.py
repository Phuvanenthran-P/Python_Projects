import os

path = input("Folder path: ")

for i, file in enumerate(os.listdir(path)):
    ext = file.split('.')[-1]
    new_name = f"file_{i+1}.{ext}"
    os.rename(os.path.join(path, file), os.path.join(path, new_name))

print("Files renamed.")
