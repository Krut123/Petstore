Python 3.11.6 (tags/v3.11.6:8b6ee5b, Oct  2 2023, 14:57:12) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import os
os.chdir("C:\Users\Admin\Desktop\krutarth\python")
SyntaxError: incomplete input
os.chdir("C:/Users/Admin/Desktop/krutarth/python")
os.getcwd()
'C:\\Users\\Admin\\Desktop\\krutarth\\python'
f = open("demo.txt",'x')
f = open("demo.txt","r+")
f.write("this is first line")
18
print(f.read())

f.seek(0)
0
print(f.read())
this is first line

print(f.read())

.
SyntaxError: incomplete input
print(f.read())

.
SyntaxError: incomplete input
print(f.read())

krutarth
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    krutarth
NameError: name 'krutarth' is not defined
print(f.read()).
SyntaxError: incomplete input
print(f.read())


hello
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    hello
NameError: name 'hello' is not defined. Did you mean: 'help'?
print(f.read())

f.close
<built-in method close of _io.TextIOWrapper object at 0x00000202A8CF9B10>
f.close()
print(f.read())
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    print(f.read())
ValueError: I/O operation on closed file.
f = open()
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    f = open()
TypeError: open() missing required argument 'file' (pos 1)
f = open("demo.txt","r")
f.wrire("hwllo")
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    f.wrire("hwllo")
AttributeError: '_io.TextIOWrapper' object has no attribute 'wrire'. Did you mean: 'write'?
print(f.write())
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    print(f.write())
TypeError: TextIOWrapper.write() takes exactly one argument (0 given)
print(f.read())
this is first line
f.close()
f = open("demo.txt","w")
print(f.read())
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    print(f.read())
io.UnsupportedOperation: not readable
f.write("hello")
5
f.close()
f = open("demo.txt","r")
print(f.read())
hello
f.close()
f = open("demo.txt","w+")
print(f.read())

f.write("this is new line")
16
f.seek(0)
0
print(f.read())
this is new line
f.close()
f.write('apple\n')
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    f.write('apple\n')
ValueError: I/O operation on closed file.
f = open("demo.txt","w+")
f.write('apple\n')
6
f.write('orange\n')
7
f.write('pear\n')
5
f.seek(5)
5
print(f.read())

orange
pear

f.seek(0)
0
print(f.read())
apple
orange
pear

f.write("hii")
3
f.write("hello")
5
f.write("\n good morning")
14
f.seek(0)
0
print(f.read())
apple
orange
pear
hiihello
 good morning












f.close()
f = open("demo.txt","a")
print(f.read())
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    print(f.read())
io.UnsupportedOperation: not readable
f.write("this is append")
14
f.close()
f = open("demo.txt","r")
print(f.read())
apple
orange
pear
hiihello
 good morningthis is append

f.close()
f.open("demo.txt","a+")
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    f.open("demo.txt","a+")
AttributeError: '_io.TextIOWrapper' object has no attribute 'open'
f = open("demo.txt","a+")
f.write("this is a+ append")
17
print(f.read())


f.close()
print(f.readline())
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    print(f.readline())
ValueError: I/O operation on closed file.
f = open("demo.txt","r")
print(f.readline())
apple

print(f.readlines())
['orange\n', 'pear\n', 'hiihello\n', ' good morningthis is appendthis is a+ append']
f.seek(0)
0
print(f.read(10))
apple
oran
>>> f.tell()
11
>>> 
>>> import os
>>> print(__file__)
Traceback (most recent call last):
  File "<pyshell#88>", line 1, in <module>
    print(__file__)
NameError: name '__file__' is not defined. Did you mean: '__name__'?
>>> print__name__)
SyntaxError: unmatched ')'
>>> print(__name__)
__main__
>>> f.seek(0)
0
>>> num_of_char = len(f.read())
>>> print("number odf character in file are:",num_of_char)
number odf character in file are: 71
>>> data = f.read()
>>> replace(" ","")
Traceback (most recent call last):
  File "<pyshell#95>", line 1, in <module>
    replace(" ","")
NameError: name 'replace' is not defined
>>> data = f.read0().replace(" "." ")
SyntaxError: invalid syntax
>>> data = f.read().replace(" "." ")
SyntaxError: invalid syntax
>>> data = f.read().replace(" "," ")
>>> f.seek(0)
0
>>> print(f.read())
apple
orange
pear
hiihello
 good morningthis is appendthis is a+ append
>>> print(data)

>>> import os
