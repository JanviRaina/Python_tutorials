
fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"
fh = open(fname)
count = 0
lst=[]
for lines in fh:
    if lines.startswith("From") and len(lines.split())>2:
        temp=lines.split()
        lst.append(temp[1])
for lines in lst:
    count=count+1
    print(lines)
print("There were",count, "lines in the file with From as the first word")