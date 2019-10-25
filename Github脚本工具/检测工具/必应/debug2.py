import os
dir = 'http'
files= os.walk(dir)
for files in os.walk(dir):
    filename = files[2]
print(filename)