# create an object and serialize it .then write it to a file 
# a file object
# using pickle to make it serialization
# 



import pickle 

obj={'Python':3,'KDE':5,'Windows':10}


fileobj=open('data.obj','wb')

pickle.dump(obj,fileobj)

fileobj.close()