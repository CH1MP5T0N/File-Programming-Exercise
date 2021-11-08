myDict = {}
file = open(r"C:\Users\phili\OneDrive\Documents\oof.txt", "r")
read = file.read()
order = []
punctuation = """!)(-][{};:'",<>./?@#$%^&*_~"""


for i in read:
    if i in punctuation:
        read = read.replace(i, "")

page = read.split()

for i in page:
    if i not in myDict:
        myDict[i] = 1
    else:
        myDict[i] += 1

for i in myDict:
    if myDict[i] == 1:
        order.append(i)

for hapax in order:
    print(hapax)
