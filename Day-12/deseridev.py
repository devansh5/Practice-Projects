# pickle module is used for serializing and deserializing object into file
# stream or file stream back to object repectively


import pickle

fileobj=open('data.obj','rb')

# here load is used for deserializing the file data back to object
obj=pickle.load(fileobj)
print(obj)