import os
os.chdir("C:/Users/Admin/Desktop/krutarth/python")
filename = input("enter filename: ")
if os.path.isfile
f = open("demo.txt","r+")
line = f.readlines()
total_count = 0
for i in line:
    words = i.split()
    print(words)
    total_count += len(words)
print(total_count)

