import pickle
import requests
url='https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
response=requests.get(url)
respons_txt=response.text
data=respons_txt.splitlines()
red=[[i] for i in data ]
# Pickling the python objects
fileobj=open('irisData.pkl','wb')
pickle.dump(red,fileobj)
fileobj.close()

# Reading of Pickle File:
fileobj=open('irisData.pkl','rb')
data=pickle.load(fileobj)
print(data)