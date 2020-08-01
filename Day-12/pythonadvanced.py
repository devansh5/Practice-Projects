class Point(object):

    def __new__(cls,*args,**kwargs):
        print("From new")
        print(cls)
        print(args)
        print(kwargs)

        # create our object and return it
        obj = super().__new__(cls)
        return obj

    def __init__(self,x = 0,y = 0):
        print("From init")
        self.x = x
        self.y = y