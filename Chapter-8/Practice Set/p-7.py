def rem(l,word):
    for i in l:
        n=[]
        for items in l:
            if not(items == word):
                n.append(items.strip(word))
        return n 

l = ["Sujal","Yash","Rohit","Sarvesh"]

print(rem(l,"Su"))
