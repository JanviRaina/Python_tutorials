
fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"
fh = open(fname)

hcount=dict()
lst=[]

count = 0
lst=[]
for lines in fh:
    if lines.startswith("From") and len(lines.split())>2:
        words=lines.split()
        hour=words[5].split(':')
        hcount[hour[0]]=hcount.get(hour[0],0)+1
    else:
        continue

for k,v in hcount.items():
    lst.append((k,v))
        
        
lst.sort()
for k,v in lst:
    print(k,v)