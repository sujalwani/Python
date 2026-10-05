with open("file.txt") as f:
    content1=f.read()

with open("file_copy.txt") as f:
    content2=f.read()

if(content1 == content2):
    print("Yes files content are identical.")
else:
    print("No files content are not identical.")