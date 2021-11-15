tecca = open(r"C:\Users\phili\OneDrive\Documents\text.txt","r")
read = tecca.read()
split = read.split("\n")
mosey = 1
with open(r"C:\Users\phili\OneDrive\Documents\text.txt","r") as homie:
    for i in split:
        if i:
            for i in homie:
                print(mosey, i)
                mosey += 1

