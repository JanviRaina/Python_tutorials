# Use the file name mbox-short.txt as the file name
count=0
fname = input("Enter file name: ")
fh = open(fname)
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    else:
        count=count+1
        f=line.find('0')
        l=line[f:]
        r=float(l)
print(r/count)




