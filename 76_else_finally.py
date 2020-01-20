f1=open("harry.txt")
try:
    f=open("does.txt")
except Exception as e:
    print(e)
# except EOFError as e:
#     print("eof error is there",e)
# except IOError as e:
#     print(e)

else:
    print("runs only whe except doesnt run")
finally:
    print("run this anyway")
    print("it is used for clean up..if we want our code to eecute no matter it enters try or except block")
    f1.close()