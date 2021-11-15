ye = open(r"C:\Users\phili\OneDrive\Documents\boom.txt", "r")
read = ye.read()
split = read.split()
print(len(read) / len(split))