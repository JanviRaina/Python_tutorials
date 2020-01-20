#used for storing which can be used later
import pickle
#PICKLING A PYTHON OBJECT
# cars=["Audi","Maruti suzuki","haruti tuzuki"]
# file="mycar.pkl"
# fileobj=open(file,"wb")
# pickle.dump(cars,fileobj)
# fileobj.close()


# To get from pickled one

file="mycar.pkl"
fileobj=open(file,"rb")
mycar=pickle.load(fileobj)
print(mycar)
print(type(mycar))