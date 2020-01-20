import os
# print(dir(os))      #shows all the attributes and methods inside os in built module ,we can also see using documentation
print(os.getcwd())      # current working directory
# os.chdir   ("C://")            #to change current working directory
# print(os.getcwd()) 
# f=open("harry.txt")         #shows file not found
# print(os.listdir())
# print(os.listdir("C://"))       #gives list
#TO MAKE  A FOLDER:
# os.mkdir("This")
# os.makedirs("This/that")
#  os.rename("harry.txt", "larry.txt")
# print(os.environ.get('Path'))
# print(os.path.join("C:/", "/harry.txt"))
# print(os.path.exists("C://Program Files2"))
print(os.path.isfile("C://Program Files"))
# print(os.path.isdir("C://Program Files"))