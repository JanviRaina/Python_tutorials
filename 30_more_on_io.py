# SEEK      USED FOR SETTING POINTER at position at which we want
# TELL      USED for knowing where our pointer is

f=open("#26_janvi.txt")
print(f.readline())
print(f.tell())
f.seek(0)
print(f.tell())
print(f.readline())
print(f.readline())
print(f.tell())
f.close()
