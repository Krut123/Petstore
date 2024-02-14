import os
print("filename: ",__file__)
print("absolute path:",os.path.abspath(__file__))
print("directory name:",os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.dirname(os.path.abspath)


