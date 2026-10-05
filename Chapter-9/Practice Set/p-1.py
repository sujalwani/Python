with open("poem.txt") as f:

    content = f.read()

    if("twinkle" in content):
        print("Twinkle word is present in the content.")
    else:
        print("Twinkle word is not present in the content.")
