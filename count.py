def counting():
    result = 0
    f = open("j.txt","r")
    for i in f :
        words = i.split()
        result = result + len(words)
    print(result)

counting()