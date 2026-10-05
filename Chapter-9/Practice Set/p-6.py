with open("log.txt","r") as f:
    content = f.read()

if("python" in content ):
    print("Python is present in the content.")
else:
    print("Python is not oresent in the content.")