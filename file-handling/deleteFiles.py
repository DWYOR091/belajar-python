import os

# os.remove("test2.txt") #hapus file

if os.path.exists("test3.txt"):
    os.remove("test3.txt")
else:
    print("file not found")