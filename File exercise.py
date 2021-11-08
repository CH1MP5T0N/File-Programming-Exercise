myDict = {}
file = open(r"C:\Users\phili\OneDrive\Documents\oof.txt", "r")
read = file.read()
list = []
punc = '''!()-[]{};:'",<>./?@#$%^&*_~'''


for i in read:
    if i in punc:
        read = read.replace(i, "")

book = read.split()

for i in book:
    if i not in myDict:
        myDict[i] = 1
    else:
        myDict[i] += 1



for i in myDict:
    if myDict[i] == 1:
        list.append(i)

for words in list:
    print(words)