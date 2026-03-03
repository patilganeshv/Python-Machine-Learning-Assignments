import hashlib
import os

def calculate_checksum(file_name):
    fobj = open(file_name, "rb")
    hobj = hashlib.md5()

    buffer = fobj.read(1024)  # 1024 Means (1MB)

    while len(buffer) > 0:
        hobj.update(buffer)
        buffer = fobj.read(1024)
    
    fobj.close()
    return hobj.hexdigest()

def is_exists(name):
    return os.path.exists(name)

def is_directory(dir_name):
    return os.path.isdir(dir_name)